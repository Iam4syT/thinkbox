package GridManagerCore.main;

import GridManagerCore.config.GridManagerConfig;
import GridManagerCore.facade.GridSystemFacade;

public class GridSystem{
    
    public static void main(String[] args) {

        GridManagerConfig config = new GridManagerConfig.GridBuilder("Amsterdam Campus")
                                                        .industrialDemand(60)
                                                        .windSpeed(50)
                                                        .solarIrradiance(70)
                                                        .electricityCost(80)
                                                        .timeOfDay("Daytime")
                                                        .grid();

        GridSystemFacade gridsystem = new GridSystemFacade(config);
        gridsystem.initialize();

        GridManagerConfig config2 = new GridManagerConfig.GridBuilder("Seattle Campus")
                                                        .industrialDemand(60)
                                                        .windSpeed(80)
                                                        .solarIrradiance(50)
                                                        .electricityCost(90)
                                                        .timeOfDay("Daytime")
                                                        .grid();

        GridSystemFacade gridsystem2 = new GridSystemFacade(config2);
        gridsystem2.initialize();

        
    }
}
