package GridManagerCore.prediction;

import GridManagerCore.config.GridManagerConfig;

/**
 * ConsolePredictionListener — Concrete Observer printing 30-minute ahead
 * solar irradiance drop notifications and supply management recommendations to terminal.
 */
public class ConsolePredictionListener implements PredictionListener {

    @Override
    public void onPredictionEvaluated(SolarForecast forecast, GridManagerConfig config) {
        System.out.println("\n 🔮 [30-MINUTE AHEAD SOLAR PREDICTION ENGINE]");
        System.out.printf(" Location                     : %s%n", forecast.getLocation());
        System.out.printf(" Current GHI / Solar Output   : %.1f W/m² (PV: %.2f kW)%n", forecast.getCurrentGhi(), forecast.getCurrentPvOutputKw());
        System.out.printf(" 30-Min Forecasted GHI        : %.1f W/m² (PV: %.2f kW)%n", forecast.getPredictedGhi30Min(), forecast.getPredictedPvOutputKw30Min());
        System.out.printf(" Projected PV Output Drop    : %.1f%%%n", forecast.getPvDropPercentage());

        if (forecast.isDropWarning()) {
            System.out.println(" ⚠️  ALERT: 30-MINUTE AHEAD PV OUTPUT DROP WARNING!");
            System.out.println(" Details : " + forecast.getWarningMessage());
            System.out.println(" PROACTIVE ACTION REQUIRED : Pre-activating Wind / Hybrid reserves or Grid fallback to ensure zero downtime.");
        } else {
            System.out.println(" ✅  STATUS: Solar output stable for the next 30 minutes.");
        }
    }
}
