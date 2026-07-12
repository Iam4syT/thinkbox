"""
scoring_engine.py
=================
Core priority scoring logic for the Enterprise AI Prioritization Engine.

Implements the classic consulting 2×2 prioritization matrix — mapping
commercial impact against engineering feasibility to produce a scored,
quadrant-classified recommendation for each AI use case.
"""


def calculate_priority_score(impact: float, feasibility: float) -> float:
    """
    Calculates a weighted priority score out of 100.

    Weighting rationale:
      - Commercial Impact (60%) — reflects that strategic value drives
        executive buy-in and budget allocation.
      - Engineering Feasibility (40%) — accounts for delivery risk,
        data availability, and team capability constraints.

    Args:
        impact:      Commercial impact score (0–100).
        feasibility: Engineering feasibility score (0–100).

    Returns:
        Weighted priority score rounded to 1 decimal place.
    """
    return round((impact * 0.6) + (feasibility * 0.4), 1)


def determine_quadrant(impact: float, feasibility: float) -> str:
    """
    Categorises a use case into one of four consulting 2×2 matrix quadrants
    using a threshold of 65 to distinguish high from low on each axis.

    Quadrant Map:
        ┌──────────────────────┬───────────────────────────┐
        │  Strategic Initiative│       Quick Win           │
        │  High Value /        │  High Value /             │
        │  High Complexity     │  Easy to Deliver          │
        ├──────────────────────┼───────────────────────────┤
        │  Divest / Reconsider │  Low Hanging Fruit        │
        │  Low Value /         │  Low Value /              │
        │  High Complexity     │  Easy to Deliver          │
        └──────────────────────┴───────────────────────────┘
              Low Feasibility         High Feasibility

    Args:
        impact:      Commercial impact score (0–100).
        feasibility: Engineering feasibility score (0–100).

    Returns:
        String label for the appropriate strategic quadrant.
    """
    if impact >= 65 and feasibility >= 65:
        return "⚡ Quick Win — High Value, Easy to Deliver"
    elif impact >= 65 and feasibility < 65:
        return "🎯 Strategic Initiative — High Value, High Complexity"
    elif impact < 65 and feasibility >= 65:
        return "🍎 Low Hanging Fruit — Low Value, Easy to Deliver"
    else:
        return "⚠️ Divest / Reconsider — Low Value, High Complexity"
