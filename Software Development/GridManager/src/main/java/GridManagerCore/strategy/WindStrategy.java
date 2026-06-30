package GridManagerCore.strategy;

import GridManagerCore.config.GridManagerConfig;
import GridManagerCore.sources.EnergySource;
import GridManagerCore.sources.WindEnergySource;

public class WindStrategy implements SourceStrategy {

    @Override
    public boolean isBest(GridManagerConfig config) {
        return config.getSolarIrradiance() < config.getWindSpeed() 
               && config.getWindSpeed() > config.getIndustrialDemand();
    }

    @Override
    public EnergySource getSource() {
        return new WindEnergySource();
    }

}
