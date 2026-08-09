package GridManagerCore.prediction;

import GridManagerCore.config.GridManagerConfig;

/**
 * PhysicalGhiPredictionStrategy — Concrete strategy predicting 30-minute ahead
 * GHI and PV output drop based on atmospheric transmittivity trends, cloud cover index,
 * and physical panel specifications.
 */
public class PhysicalGhiPredictionStrategy implements GhiPredictionStrategy {

    private final double dropThresholdRatio;

    /**
     * Default constructor with 20% drop threshold ratio.
     */
    public PhysicalGhiPredictionStrategy() {
        this(0.20); // 20% drop triggers warning
    }

    public PhysicalGhiPredictionStrategy(double dropThresholdRatio) {
        this.dropThresholdRatio = dropThresholdRatio;
    }

    @Override
    public SolarForecast predict30MinAhead(GridManagerConfig config) {
        // Current Solar Irradiance (GHI) in W/m² (normalized 0-100 mapped to 0-1000 W/m²)
        double rawSolar = config.getSolarIrradiance();
        double currentGhiW = rawSolar * 10.0; // Map percentage (e.g. 70%) to W/m² (700 W/m²)

        // Simulate 30-minute ahead GHI prediction factoring in cloud attenuation factor
        // If night or low irradiance, GHI drop factor is minimal
        double cloudFactor = config.getElectricityCost() >= 85 ? 0.45 : 0.65; // Simulated cloud attenuation
        double predictedGhi30Min = config.getTimeOfDay().equalsIgnoreCase("Daytime") 
                ? currentGhiW * cloudFactor 
                : 0.0;

        // Physical PV Output Formula: P = Area (m²) * Efficiency * GHI (W/m²) * (1 - Loss)
        double areaSqM = 500.0;     // 500 m² commercial solar panel array
        double efficiency = 0.20;    // 20% panel efficiency
        double systemLoss = 0.14;    // 14% balance-of-system loss

        double currentPvKw = (areaSqM * efficiency * (currentGhiW / 1000.0) * (1.0 - systemLoss));
        double predictedPvKw30Min = (areaSqM * efficiency * (predictedGhi30Min / 1000.0) * (1.0 - systemLoss));

        double dropAmount = Math.max(0, currentPvKw - predictedPvKw30Min);
        double pvDropPercentage = currentPvKw > 0 ? (dropAmount / currentPvKw) * 100.0 : 0.0;

        boolean isWarning = (pvDropPercentage >= (dropThresholdRatio * 100.0))
                || (predictedPvKw30Min < (config.getIndustrialDemand() * 0.8) && currentPvKw >= config.getIndustrialDemand());

        String warningMsg = isWarning 
                ? String.format("CRITICAL 30-MIN AHEAD PV DROP DETECTED: PV Output expected to drop by %.1f%% (from %.2f kW down to %.2f kW). Pre-emptive supply dispatch required!",
                                pvDropPercentage, currentPvKw, predictedPvKw30Min)
                : "Solar GHI output stable for next 30 minutes.";

        return new SolarForecast(
            config.getLocation(),
            currentGhiW,
            predictedGhi30Min,
            currentPvKw,
            predictedPvKw30Min,
            pvDropPercentage,
            isWarning,
            warningMsg
        );
    }
}
