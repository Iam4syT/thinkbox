package GridManagerCore.sources;

public class HydrogenEnergySource implements EnergySource {
    @Override
    public void switchTo() {
        System.out.println("Switching to Hydrogen Source");
    }
    @Override
    public String getName() { return "Hydrogen"; }
}

