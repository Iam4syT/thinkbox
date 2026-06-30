package GridManagerCore.strategy;

import GridManagerCore.config.GridManagerConfig;
import GridManagerCore.sources.EnergySource;

public interface SourceStrategy {

    boolean isBest(GridManagerConfig config);
    EnergySource getSource();
}