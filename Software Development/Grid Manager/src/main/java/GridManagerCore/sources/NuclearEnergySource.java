package GridManagerCore.sources;

public class NuclearEnergySource implements EnergySource {
    @Override
    public void switchTo() {
        System.out.println("Switching to Nuclear Energy");
    }
    @Override
    public String getName() { return "Nuclear Energy"; }

    @Override
    public double getCostPerKwh() { return 0.06; }

    @Override
    public double getCo2PerKwh() { return 0.005; }
}
