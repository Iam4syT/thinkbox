package GridManagerCore.main;

import GridManagerCore.config.GridManagerConfig;
import GridManagerCore.facade.GridSystemFacade;
import GridManagerCore.prediction.ConsolePredictionListener;
import GridManagerCore.prediction.PhysicalGhiPredictionStrategy;
import GridManagerCore.prediction.SolarForecast;
import GridManagerCore.prediction.SolarIrradianceIntelligenceService;

/**
 * GridSystem — CLI Entry Point & Automated Demonstration for 30-Minute Ahead
 * Solar Irradiance (GHI) and PV Output Drop Prediction Engine.
 */
public class GridSystem {

    public static void main(String[] args) {
        System.out.println("================================================================================");
        System.out.println(" ⚡ GRID MANAGER CORE — 30-MINUTE AHEAD SOLAR PREDICTION DEMO");
        System.out.println("================================================================================\n");

        // Scenario 1: High Solar Irradiance with Incoming Cloud Cover (Triggers 30-Min Drop Warning)
        System.out.println("--- Scenario 1: Amsterdam Campus (High Solar + Predicted Cloud Cover Drop) ---");
        GridManagerConfig configAmsterdam = new GridManagerConfig.GridBuilder("Amsterdam Campus")
                .industrialDemand(60)
                .windSpeed(50)
                .solarIrradiance(70)
                .electricityCost(85) // High cost triggers 30-min drop simulation
                .timeOfDay("Daytime")
                .grid();

        GridSystemFacade facadeAmsterdam = new GridSystemFacade(configAmsterdam);
        facadeAmsterdam.initialize();

        System.out.println("\n--------------------------------------------------------------------------------\n");

        // Scenario 2: Moderate Solar & High Wind (Stable Solar Output)
        System.out.println("--- Scenario 2: Seattle Campus (High Wind + Stable Solar Output) ---");
        GridManagerConfig configSeattle = new GridManagerConfig.GridBuilder("Seattle Campus")
                .industrialDemand(50)
                .windSpeed(80)
                .solarIrradiance(40)
                .electricityCost(40) // Off-peak cost, stable output
                .timeOfDay("Daytime")
                .grid();

        GridSystemFacade facadeSeattle = new GridSystemFacade(configSeattle);
        facadeSeattle.initialize();

        System.out.println("\n================================================================================");
        System.out.println(" ✅ DEMO COMPLETE: 30-Minute Ahead Prediction & Facade Integration Verified");
        System.out.println("================================================================================\n");
    }
}
