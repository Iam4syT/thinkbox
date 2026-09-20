import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
from solar_prediction import PhysicalGhiPredictionStrategy
from energy_manager import cost_of_power_consumption

class SolarTests(unittest.TestCase):
    def test_power_conversion_and_zero(self):
        strategy=PhysicalGhiPredictionStrategy()
        forecast=strategy.predict_30min_ahead(1000, panel_area_sqm=10, panel_efficiency=.2, cloud_cover_trend='stable')
        self.assertAlmostEqual(forecast.current_pv_output_kw, 1.72)
        self.assertEqual(strategy.predict_30min_ahead(0).pv_drop_percentage, 0)
        self.assertAlmostEqual(cost_of_power_consumption(1000, .36)*3600, .36, places=6)
    def test_bad_inputs_fail(self):
        strategy=PhysicalGhiPredictionStrategy()
        for kwargs in [{'current_ghi_w_m2':-1},{'current_ghi_w_m2':float('nan')},{'current_ghi_w_m2':1,'panel_efficiency':2},{'current_ghi_w_m2':1,'cloud_cover_trend':'mystery'}]:
            with self.assertRaises(ValueError):strategy.predict_30min_ahead(**kwargs)
