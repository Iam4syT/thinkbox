package GridManagerCore.sources;

/**
 * SolarEnergySource — concrete implementation of EnergySource.
 * Each source is fully self-describing: it knows its own name, cost, and CO₂ footprint.
 * This satisfies OCP — the system is open to new sources without modifying existing ones.
 */
public class SolarEnergySource implements EnergySource {

    @Override
    public void switchTo() {
        System.out.println("Solar is best choice for demand. Switching to Solar Energy");
    }

    @Override
    public String getName() {
        return "Solar Energy";
    }

    /** ~$0.05/kWh — IRENA utility-scale solar PV LCOE estimate. */
    @Override
    public double getCostPerKwh() {
        return 0.05;
    }

    /** ~0.020 kg CO₂/kWh — lifecycle emissions for utility-scale solar PV. */
    @Override
    public double getCo2PerKwh() {
        return 0.020;
    }
}
