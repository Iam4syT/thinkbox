"""Illustrative sensitivity scenarios. Coefficients are invented assumptions,
not vendor prices, measured emissions or evidence of net-zero alignment.
"""
import math
from numbers import Integral, Real

MODEL_REGISTRY = {
    "Scenario A (illustrative lower coefficients)": {"cost_per_million_tokens": 1.5, "co2_per_million_tokens": .05},
    "Scenario B (illustrative higher coefficients)": {"cost_per_million_tokens": 15.0, "co2_per_million_tokens": .45}
}
ASSUMPTIONS = {"reviewed": "2026-09-13", "provenance": "Hypothetical teaching inputs; not sourced vendor rates or carbon measurements", "cost_unit": "USD per million tokens", "carbon_unit": "kg CO2e per million tokens", "exclusions": "Input/output/cache rates, region, hardware, utilisation, other cloud charges and lifecycle emissions"}

def estimate_green_ai_impact(monthly_tokens: int, model_type: str):
    if isinstance(monthly_tokens, bool) or not isinstance(monthly_tokens, Integral) or monthly_tokens < 0:
        raise ValueError("monthly_tokens must be a non-negative integer")
    if model_type not in MODEL_REGISTRY: raise ValueError("Unknown scenario")
    factors = MODEL_REGISTRY[model_type]
    millions = monthly_tokens / 1_000_000
    return round(millions * factors["cost_per_million_tokens"], 2), round(millions * factors["co2_per_million_tokens"], 3)

def get_model_options(): return list(MODEL_REGISTRY)

def get_sustainability_rating(co2_kg: float):
    if isinstance(co2_kg, bool) or not isinstance(co2_kg, Real) or not math.isfinite(co2_kg) or co2_kg < 0:
        raise ValueError("co2_kg must be finite and non-negative")
    return "Illustrative scenario only; sustainability alignment has not been assessed"
