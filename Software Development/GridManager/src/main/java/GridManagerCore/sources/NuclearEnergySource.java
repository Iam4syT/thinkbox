package GridManagerCore.sources;

public class NuclearEnergySource implements EnergySource {
    @Override
    public void switchTo() {
        System.out.println("Switching to Nuclear Energy");
    }
    @Override
    public String getName() { return "Nuclear Energy"; }

}
