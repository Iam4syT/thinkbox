package GridManagerTest.java.com.store.core;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


import GridManagerCore.config.GridManagerConfig;

public class BuilderTest {
   @Test
   void testBuilderConfig(){
    GridManagerConfig config = new GridManagerConfig.GridBuilder("Test Campus")
                                                        .industrialDemand(50)
                                                        .windSpeed(40)
                                                        .solarIrradiance(60)
                                                        .electricityCost(70)
                                                        .timeOfDay("daytime")
                                                        .grid();
    
    assertEquals("Test Campus", config.getLocation());
    assertEquals(50, config.getIndustrialDemand());
    assertEquals(40, config.getWindSpeed());
    assertEquals(60, config.getSolarIrradiance());
    assertEquals(70, config.getElectricityCost());
    assertEquals("daytime", config.getTimeOfDay()); 

   }

}

