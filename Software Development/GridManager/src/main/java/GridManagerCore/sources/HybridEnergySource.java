package GridManagerCore.sources;

/**
 * HybridEnergySource — concrete implementation of EnergySource.
 * Represents a blended Solar + Wind configuration.
 * Cost and CO₂ are averaged across both sources.
 */
public class HybridEnergySource implements EnergySource {

    @Override
    public void switchTo() {
        System.out.println("Two or more sources are great choices. Switching to Hybrid (Solar + Wind)");
    }

    @Override
    public String getName() {
        return "Hybrid";
    }

    /** ~$0.045/kWh — blended average of Solar ($0.05) and Wind ($0.04). */
    @Override
    public double getCostPerKwh() {
        return 0.045;
    }

    /** ~0.015 kg CO₂/kWh — blended lifecycle emissions for Solar + Wind. */
    @Override
    public double getCo2PerKwh() {
        return 0.015;
    }
}
