package GridManagerCore.prediction;

/**
 * SolarForecast — Value object holding 30-minute ahead solar irradiance (GHI)
 * and PV power output predictions.
 *
 * SOLID Principles applied:
 *   SRP: Holds immutable prediction state and warning calculation attributes only.
 */
public class SolarForecast {

    private final String location;
    private final double currentGhi;
    private final double predictedGhi30Min;
    private final double currentPvOutputKw;
    private final double predictedPvOutputKw30Min;
    private final double pvDropPercentage;
    private final boolean isDropWarning;
    private final String warningMessage;

    public SolarForecast(String location,
                         double currentGhi,
                         double predictedGhi30Min,
                         double currentPvOutputKw,
                         double predictedPvOutputKw30Min,
                         double pvDropPercentage,
                         boolean isDropWarning,
                         String warningMessage) {
        this.location = location;
        this.currentGhi = currentGhi;
        this.predictedGhi30Min = predictedGhi30Min;
        this.currentPvOutputKw = currentPvOutputKw;
        this.predictedPvOutputKw30Min = predictedPvOutputKw30Min;
        this.pvDropPercentage = pvDropPercentage;
        this.isDropWarning = isDropWarning;
        this.warningMessage = warningMessage;
    }

    public String getLocation() { return location; }
    public double getCurrentGhi() { return currentGhi; }
    public double getPredictedGhi30Min() { return predictedGhi30Min; }
    public double getCurrentPvOutputKw() { return currentPvOutputKw; }
    public double getPredictedPvOutputKw30Min() { return predictedPvOutputKw30Min; }
    public double getPvDropPercentage() { return pvDropPercentage; }
    public boolean isDropWarning() { return isDropWarning; }
    public String getWarningMessage() { return warningMessage; }

    @Override
    public String toString() {
        return String.format(
            "SolarForecast[%s | Current GHI: %.1f W/m² -> 30-Min Predicted: %.1f W/m² | Current PV: %.2f kW -> Predicted PV: %.2f kW | Drop: %.1f%% | Warning: %s]",
            location, currentGhi, predictedGhi30Min, currentPvOutputKw, predictedPvOutputKw30Min, pvDropPercentage, isDropWarning ? "YES" : "NO"
        );
    }
}
