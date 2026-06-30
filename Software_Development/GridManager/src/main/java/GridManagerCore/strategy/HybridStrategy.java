package GridManagerCore.strategy;

import GridManagerCore.config.GridManagerConfig;
import GridManagerCore.sources.EnergySource;
import GridManagerCore.sources.HybridEnergySource;


public class HybridStrategy implements SourceStrategy {

    @Override
    public boolean isBest(GridManagerConfig config) {
        return config.getSolarIrradiance() >= config.getWindSpeed() 
               && config.getSolarIrradiance() >= config.getIndustrialDemand()
               && config.getWindSpeed() >= config.getIndustrialDemand();
    }

    @Override
    public EnergySource getSource() {
        return new HybridEnergySource();
    }

}
