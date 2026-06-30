package GridManagerCore.sources;

/**
 * GridEnergySource — the fallback energy source when no renewable qualifies.
 * This is the most expensive and highest-emission option, used only as a
 * last resort to guarantee operational continuity.
 */
public class GridEnergySource implements EnergySource {

    @Override
    public void switchTo() {
        System.out.println("WARNING: No renewable source qualifies. Switching to Grid Electricity.");
    }

    @Override
    public String getName() {
        return "Grid Electricity";
    }

    /** $0.10/kWh — IEA global average grid electricity price estimate. */
    @Override
    public double getCostPerKwh() {
        return 0.10;
    }

    /** 0.450 kg CO₂/kWh — IEA global average grid electricity emission intensity. */
    @Override
    public double getCo2PerKwh() {
        return 0.450;
    }
}
