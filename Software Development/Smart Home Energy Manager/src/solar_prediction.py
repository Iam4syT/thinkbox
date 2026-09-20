import math
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class SolarForecast:
    """
    Data class representing a 30-minute ahead solar irradiance (GHI)
    and PV power output prediction.
    """
    location_name: str
    current_ghi_w_m2: float
    predicted_ghi_30min_w_m2: float
    current_pv_output_kw: float
    predicted_pv_output_30min_kw: float
    pv_drop_percentage: float
    is_drop_warning: bool
    warning_message: str


class GhiPredictionStrategy(ABC):
    """
    Strategy Interface (SOLID - OCP/DIP) for predicting 30-minute ahead
    Global Horizontal Irradiance (GHI) and PV output.
    """
    @abstractmethod
    def predict_30min_ahead(
        self,
        current_ghi_w_m2: float,
        panel_area_sqm: float = 30.0,
        panel_efficiency: float = 0.20,
        cloud_cover_trend: str = "increasing",
        location_name: str = "Home Solar Array"
    ) -> SolarForecast:
        pass


class PhysicalGhiPredictionStrategy(GhiPredictionStrategy):
    """
    Concrete Strategy implementing illustrative GHI attenuation scenario
    and PV output conversion.
    Formula: P_PV = Area (m²) * Efficiency * (GHI / 1000) * (1 - Loss)
    """
    def __init__(self, drop_threshold_ratio: float = 0.20):
        if not math.isfinite(drop_threshold_ratio) or not 0 <= drop_threshold_ratio <= 1:
            raise ValueError("drop_threshold_ratio must be between 0 and 1")
        self.drop_threshold_ratio = drop_threshold_ratio

    def predict_30min_ahead(
        self,
        current_ghi_w_m2: float,
        panel_area_sqm: float = 30.0,
        panel_efficiency: float = 0.20,
        cloud_cover_trend: str = "increasing",
        location_name: str = "Home Solar Array"
    ) -> SolarForecast:
        if not all(isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v) for v in [current_ghi_w_m2, panel_area_sqm, panel_efficiency]):
            raise ValueError("Inputs must be finite numbers")
        if current_ghi_w_m2 < 0 or panel_area_sqm <= 0 or not 0 < panel_efficiency <= 1:
            raise ValueError("GHI must be non-negative; area positive; efficiency in (0, 1]")
        if not isinstance(cloud_cover_trend, str) or cloud_cover_trend.lower() not in {"rapid_clouds", "severe", "increasing", "moderate", "stable", "clear"}:
            raise ValueError("Unknown scenario trend")
        # Illustrative attenuation assumptions, not fitted weather forecasts.
        if cloud_cover_trend.lower() == "rapid_clouds" or cloud_cover_trend.lower() == "severe":
            attenuation_factor = 0.40  # 60% drop in GHI
        elif cloud_cover_trend.lower() == "increasing" or cloud_cover_trend.lower() == "moderate":
            attenuation_factor = 0.65  # 35% drop in GHI
        else:
            attenuation_factor = 0.95  # Stable / clear

        predicted_ghi = current_ghi_w_m2 * attenuation_factor
        system_loss = 0.14  # 14% balance-of-system loss

        # Calculate current & 30-min ahead PV Output in kW
        current_pv_kw = panel_area_sqm * panel_efficiency * (current_ghi_w_m2 / 1000.0) * (1.0 - system_loss)
        predicted_pv_kw = panel_area_sqm * panel_efficiency * (predicted_ghi / 1000.0) * (1.0 - system_loss)

        drop_amount = max(0.0, current_pv_kw - predicted_pv_kw)
        pv_drop_percentage = (drop_amount / current_pv_kw * 100.0) if current_pv_kw > 0 else 0.0

        is_warning = pv_drop_percentage >= (self.drop_threshold_ratio * 100.0)

        warning_msg = (
            f"SCENARIO: PV output would drop by {pv_drop_percentage:.1f}% in 30 minutes "
            f"(from {current_pv_kw:.2f} kW down to {predicted_pv_kw:.2f} kW). Review assumptions before planning any physical action."
            if is_warning
            else "Scenario remains below the selected warning threshold; future weather is unknown."
        )

        return SolarForecast(
            location_name=location_name,
            current_ghi_w_m2=current_ghi_w_m2,
            predicted_ghi_30min_w_m2=predicted_ghi,
            current_pv_output_kw=current_pv_kw,
            predicted_pv_output_30min_kw=predicted_pv_kw,
            pv_drop_percentage=pv_drop_percentage,
            is_drop_warning=is_warning,
            warning_message=warning_msg
        )


class PredictionObserver(ABC):
    """
    Observer Interface (SOLID - ISP/DIP) for receiving 30-minute ahead solar alerts.
    """
    @abstractmethod
    def on_prediction_evaluated(self, forecast: SolarForecast) -> None:
        pass


class ConsolePredictionObserver(PredictionObserver):
    """
    Concrete Observer that formats and displays 30-minute ahead solar predictions
    and drop notifications in the console.
    """
    def on_prediction_evaluated(self, forecast: SolarForecast) -> None:
        print("\n 🔮 [30-MINUTE AHEAD SOLAR PREDICTION ENGINE]")
        print(f" Target Array / Location   : {forecast.location_name}")
        print(f" Current GHI               : {forecast.current_ghi_w_m2:.1f} W/m² (PV Output: {forecast.current_pv_output_kw:.2f} kW)")
        print(f" 30-Min Forecasted GHI     : {forecast.predicted_ghi_30min_w_m2:.1f} W/m² (PV Output: {forecast.predicted_pv_output_30min_kw:.2f} kW)")
        print(f" Projected PV Output Drop : {forecast.pv_drop_percentage:.1f}%")

        if forecast.is_drop_warning:
            print(" ⚠️  ALERT: 30-MINUTE AHEAD PV OUTPUT DROP WARNING!")
            print(f" Details : {forecast.warning_message}")
        else:
            print(" STATUS: scenario below warning threshold; no actual weather forecast.")


class SolarIntelligenceEngine:
    """
    Orchestrator class managing prediction strategies and observer notifications (SRP).
    """
    def __init__(self, strategy: Optional[GhiPredictionStrategy] = None):
        self.strategy = strategy or PhysicalGhiPredictionStrategy()
        self.observers: List[PredictionObserver] = [ConsolePredictionObserver()]

    def add_observer(self, observer: PredictionObserver) -> None:
        if observer not in self.observers:
            self.observers.append(observer)

    def evaluate_forecast(
        self,
        current_ghi_w_m2: float,
        panel_area_sqm: float = 30.0,
        panel_efficiency: float = 0.20,
        cloud_cover_trend: str = "increasing",
        location_name: str = "Home Solar Array"
    ) -> SolarForecast:
        forecast = self.strategy.predict_30min_ahead(
            current_ghi_w_m2=current_ghi_w_m2,
            panel_area_sqm=panel_area_sqm,
            panel_efficiency=panel_efficiency,
            cloud_cover_trend=cloud_cover_trend,
            location_name=location_name
        )
        for observer in self.observers:
            observer.on_prediction_evaluated(forecast)
        return forecast
