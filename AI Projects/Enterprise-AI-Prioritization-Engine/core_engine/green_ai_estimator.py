"""
green_ai_estimator.py
=====================
Sustainability and cloud cost estimation module for the Enterprise AI
Prioritization Engine.

Calculates projected monthly Azure OpenAI token costs and associated
data centre carbon emissions (CO2 equivalent) based on model tier and
expected inference volume — enabling organisations to assess the
environmental and financial overhead of each AI initiative before build.

Emission factors sourced from standard regional data centre averages.
Azure pricing approximated from public Azure OpenAI service rate cards.
"""

from typing import Tuple

# ─────────────────────────────────────────────────────────────────────────────
# Pricing & Carbon Registry
# In production this dataset would be dynamically pulled from the Azure
# Pricing Calculator API and Microsoft Sustainability Manager.
# ─────────────────────────────────────────────────────────────────────────────

MODEL_REGISTRY: dict = {
    "Lightweight (e.g., GPT-3.5 / Phi-3)": {
        "cost_per_million_tokens": 1.50,   # USD per 1M tokens
        "co2_per_million_tokens": 0.05,    # kg CO2e per 1M tokens
        "description": "Optimised for high-volume, lower-complexity tasks. Best Net-Zero alignment.",
    },
    "Heavyweight (e.g., GPT-4o)": {
        "cost_per_million_tokens": 15.00,  # USD per 1M tokens
        "co2_per_million_tokens": 0.45,    # kg CO2e per 1M tokens
        "description": "Maximum reasoning capability. Higher carbon and cost overhead.",
    },
}


def estimate_green_ai_impact(
    monthly_tokens: int,
    model_type: str,
) -> Tuple[float, float]:
    """
    Estimates the monthly Azure token cost and carbon footprint for a
    given AI use case based on inference volume and model tier.

    Args:
        monthly_tokens: Total estimated token count per calendar month.
        model_type:     Key from MODEL_REGISTRY selecting the model tier.

    Returns:
        Tuple of (estimated_cost_usd, estimated_co2_kg) both rounded
        to sensible decimal precision for executive reporting.

    Raises:
        ValueError: If model_type is not found in MODEL_REGISTRY.
    """
    if model_type not in MODEL_REGISTRY:
        raise ValueError(
            f"Unknown model type '{model_type}'. "
            f"Valid options: {list(MODEL_REGISTRY.keys())}"
        )

    metrics = MODEL_REGISTRY[model_type]
    millions_of_tokens = monthly_tokens / 1_000_000

    estimated_cost = round(millions_of_tokens * metrics["cost_per_million_tokens"], 2)
    estimated_co2  = round(millions_of_tokens * metrics["co2_per_million_tokens"], 3)

    return estimated_cost, estimated_co2


def get_model_options() -> list:
    """Returns the list of available model tier keys for UI rendering."""
    return list(MODEL_REGISTRY.keys())


def get_sustainability_rating(co2_kg: float) -> str:
    """
    Translates a monthly CO2e figure into an executive-readable
    sustainability rating band.

    Args:
        co2_kg: Monthly carbon footprint in kg CO2 equivalent.

    Returns:
        String sustainability band label with emoji indicator.
    """
    if co2_kg < 0.5:
        return "🟢 Excellent — Aligns with Net-Zero targets"
    elif co2_kg < 2.0:
        return "🟡 Moderate — Review against sustainability roadmap"
    elif co2_kg < 5.0:
        return "🟠 High — Carbon offset strategy recommended"
    else:
        return "🔴 Critical — Executive sustainability review required"
