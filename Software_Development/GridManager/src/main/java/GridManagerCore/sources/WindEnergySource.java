package GridManagerCore.sources;

/**
 * WindEnergySource — concrete implementation of EnergySource.
 * Wind is the cheapest and lowest-emission dispatchable renewable available.
 */
public class WindEnergySource implements EnergySource {

    @Override
    public void switchTo() {
        System.out.println("Wind is best choice for demand. Switching to Wind Energy");
    }

    @Override
    public String getName() {
        return "Wind Energy";
    }

    /** ~$0.04/kWh — IRENA onshore wind LCOE estimate. */
    @Override
    public double getCostPerKwh() {
        return 0.04;
    }

    /** ~0.010 kg CO₂/kWh — lifecycle emissions for onshore wind. */
    @Override
    public double getCo2PerKwh() {
        return 0.010;
    }
}
