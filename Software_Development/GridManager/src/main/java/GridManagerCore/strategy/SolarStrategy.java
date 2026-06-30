package GridManagerCore.strategy;

import GridManagerCore.config.GridManagerConfig;
import GridManagerCore.sources.EnergySource;
import GridManagerCore.sources.SolarEnergySource;

public class SolarStrategy implements SourceStrategy{


    @Override
    public boolean isBest(GridManagerConfig config) {
        return config.getSolarIrradiance() > config.getWindSpeed() 
               && config.getSolarIrradiance() > config.getIndustrialDemand();
    }

    @Override
    public EnergySource getSource() {
        return new SolarEnergySource();
    }

}

