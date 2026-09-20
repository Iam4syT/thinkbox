"""Local customer-review regression benchmark. No ZenML stack or saved model required."""
import json
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
ROOT = Path(__file__).resolve().parent
FEATURES = ["price", "freight_value", "payment_value", "payment_installments", "product_weight_g"]

def run(data_path=None):
    data = pd.read_csv(data_path or ROOT / "data/olist_customers_dataset.csv")
    data = data.dropna(subset=["order_id", "review_score"])
    if len(data) < 10: raise ValueError("At least 10 labelled rows required")
    train, test = next(GroupShuffleSplit(n_splits=1, test_size=.2, random_state=42).split(data, groups=data.order_id))
    x_train, x_test = data.iloc[train][FEATURES], data.iloc[test][FEATURES]
    y_train, y_test = data.iloc[train].review_score, data.iloc[test].review_score
    assert set(data.iloc[train].order_id).isdisjoint(data.iloc[test].order_id)
    results = {}
    for name, estimator in [("mean_baseline", DummyRegressor(strategy="mean")), ("ridge", Ridge(alpha=1.0))]:
        pipeline = make_pipeline(SimpleImputer(strategy="median"), estimator)
        pipeline.fit(x_train, y_train)
        predictions = pipeline.predict(x_test)
        results[name] = {"mae": float(mean_absolute_error(y_test, predictions)), "rmse": float(np.sqrt(mean_squared_error(y_test, predictions)))}
    report = {"dataset": "Existing attributed Olist-derived repository fixture; see data/README.md", "seed":42,
        "train_rows":len(train),"test_rows":len(test), "split":"grouped by order_id; median imputation fitted only on training rows",
        "results":results,"limitations":"One random group holdout; not temporal validation, causal impact or production serving evidence."}
    out=ROOT / "evidence";out.mkdir(exist_ok=True)
    (out/'evaluation.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    return report

if __name__=='__main__':run()
