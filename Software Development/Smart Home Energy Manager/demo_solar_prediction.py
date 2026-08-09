#!/usr/bin/env python3
"""
Automated Demonstration Script for Smart Home Energy Manager:
30-Minute Ahead Solar Irradiance Drop & PV Output Prediction Engine
"""

import sys
import os

# Add src to python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from solar_prediction import SolarIntelligenceEngine, PhysicalGhiPredictionStrategy


def run_demo():
    print("================================================================================")
    print(" ☀️ SMART HOME ENERGY MANAGER — 30-MINUTE AHEAD SOLAR PREDICTION DEMO")
    print("================================================================================\n")

    engine = SolarIntelligenceEngine(PhysicalGhiPredictionStrategy(drop_threshold_ratio=0.20))

    scenarios = [
        {
            "name": "Scenario A: Clear Sun / Stable Solar Conditions",
            "ghi": 850.0,
            "area": 40.0,
            "efficiency": 0.21,
            "trend": "stable",
            "location": "Suburban Rooftop Array"
        },
        {
            "name": "Scenario B: Approaching Cloud Front (30-Min Drop Warning)",
            "ghi": 780.0,
            "area": 40.0,
            "efficiency": 0.21,
            "trend": "increasing",
            "location": "Suburban Rooftop Array"
        },
        {
            "name": "Scenario C: Sudden Severe Storm Front (High-Impact Drop Warning)",
            "ghi": 900.0,
            "area": 40.0,
            "efficiency": 0.21,
            "trend": "severe",
            "location": "Suburban Rooftop Array"
        }
    ]

    for idx, sc in enumerate(scenarios, 1):
        print(f"--------------------------------------------------------------------------------")
        print(f" 🔹 {sc['name']}")
        print(f"--------------------------------------------------------------------------------")
        forecast = engine.evaluate_forecast(
            current_ghi_w_m2=sc["ghi"],
            panel_area_sqm=sc["area"],
            panel_efficiency=sc["efficiency"],
            cloud_cover_trend=sc["trend"],
            location_name=sc["location"]
        )

        if forecast.is_drop_warning:
            print("\n 💡 [RECOMMENDED AUTOMATED PROACTIVE ACTION]")
            print("   1. Pre-charge home battery storage (BESS) at current peak solar rates.")
            print("   2. Defer heavy HVAC and EV charging loads beyond the 30-minute window.")
            print("   3. Arm seamless transition to grid / hybrid fallback.\n")
        else:
            print("\n   [ACTION] No load shedding required. Excess solar available for battery storage.\n")


if __name__ == "__main__":
    run_demo()
