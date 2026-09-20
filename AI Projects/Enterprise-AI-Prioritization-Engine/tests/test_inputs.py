import unittest
from core_engine.scoring_engine import calculate_priority_score, determine_quadrant
from core_engine.green_ai_estimator import estimate_green_ai_impact, get_model_options, get_sustainability_rating

class InputTests(unittest.TestCase):
    def test_valid_boundaries(self):
        self.assertEqual(calculate_priority_score(0, 0), 0)
        self.assertEqual(calculate_priority_score(100, 100), 100)
        self.assertEqual(calculate_priority_score(80, 50), 68)
        self.assertIn("Quick Win", determine_quadrant(65, 65))
        self.assertIn("Reconsider", determine_quadrant(64, 64))
    def test_invalid_scores(self):
        for bad in [-1, 101, float("nan"), float("inf"), "50", True, None]:
            for fn in [calculate_priority_score, determine_quadrant]:
                for args in [(bad, 50), (50, bad)]:
                    with self.subTest(args=args, fn=fn.__name__), self.assertRaises(ValueError): fn(*args)
    def test_usage_validation(self):
        scenario = get_model_options()[0]
        self.assertEqual(estimate_green_ai_impact(0, scenario), (0, 0))
        self.assertEqual(estimate_green_ai_impact(1000000, scenario), (1.5, .05))
        for bad in [-1, 1.5, True, float("nan"), None]:
            with self.assertRaises(ValueError): estimate_green_ai_impact(bad, scenario)
        with self.assertRaises(ValueError): estimate_green_ai_impact(1, "unknown")
    def test_no_net_zero_claim(self):
        self.assertIn("not been assessed", get_sustainability_rating(0))
        with self.assertRaises(ValueError): get_sustainability_rating(-1)
