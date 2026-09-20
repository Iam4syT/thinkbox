"""Illustrative 60/40 priority model, not a prediction of business results."""
import math
from numbers import Real

def _score(value, name):
    if isinstance(value, bool) or not isinstance(value, Real) or not math.isfinite(value) or not 0 <= value <= 100:
        raise ValueError(f"{name} must be a finite number between 0 and 100")
    return float(value)

def calculate_priority_score(impact: float, feasibility: float) -> float:
    return round(_score(impact, "impact") * .6 + _score(feasibility, "feasibility") * .4, 1)

def determine_quadrant(impact: float, feasibility: float) -> str:
    impact, feasibility = _score(impact, "impact"), _score(feasibility, "feasibility")
    if impact >= 65 and feasibility >= 65: return "Quick Win — High Value, Easier Delivery"
    if impact >= 65: return "Strategic Initiative — High Value, Harder Delivery"
    if feasibility >= 65: return "Low Priority — Lower Value, Easier Delivery"
    return "Reconsider — Lower Value, Harder Delivery"
