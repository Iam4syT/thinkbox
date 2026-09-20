"""Compare the heuristic with persistence on explicit synthetic scenarios."""
from pathlib import Path
import json, sys
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from solar_prediction import PhysicalGhiPredictionStrategy

def evaluate():
    cases = [(850, "stable", 830), (780, "increasing", 600), (900, "severe", 420), (500, "stable", 510), (700, "increasing", 680)]
    strategy = PhysicalGhiPredictionStrategy()
    rows=[]
    for current, trend, synthetic_future in cases:
        prediction = strategy.predict_30min_ahead(current, cloud_cover_trend=trend).predicted_ghi_30min_w_m2
        rows.append({"current_ghi":current,"trend":trend,"synthetic_future_ghi":synthetic_future,"scenario_prediction":prediction,"persistence_prediction":current})
    report={"dataset":"Five hand-authored hypothetical scenarios, not measured weather", "sample_size":len(rows),
        "heuristic_mae_w_m2":sum(abs(r['scenario_prediction']-r['synthetic_future_ghi']) for r in rows)/len(rows),
        "persistence_mae_w_m2":sum(abs(r['persistence_prediction']-r['synthetic_future_ghi']) for r in rows)/len(rows),
        "limitations":"Illustrates evaluation arithmetic only. Attenuation is not a validated 30-minute forecast; no energy savings or equipment changes measured.","cases":rows}
    out=Path(__file__).resolve().parent/'evidence';out.mkdir(exist_ok=True)
    (out/'solar-evaluation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
    return report
if __name__=='__main__':evaluate()
