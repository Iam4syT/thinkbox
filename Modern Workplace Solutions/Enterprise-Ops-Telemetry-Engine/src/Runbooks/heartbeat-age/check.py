import math

def heartbeat(age_minutes):
    if type(age_minutes) not in (int, float) or not math.isfinite(age_minutes) or age_minutes < 0:
        return "review input"
    if age_minutes > 5:
        return "investigate"
    return "fresh"
