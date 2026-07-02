package GridManagerCore.facade;

import GridManagerCore.config.GridManagerConfig;
import GridManagerCore.system.GridSystemManager;

public class GridSystemFacade {

  private final GridSystemManager manager;

 public GridSystemFacade(GridManagerConfig config){
    this.manager =  new GridSystemManager(config);

 }
 public void initialize(){
    System.out.println("\n ==== Initializing Grid System ====");
    manager.sensorData();
    manager.intelligentSwitch();
    manager.saveSwitchHistory();
    System.out.println("\n ====  Grid System Initialization Successful ====");

    System.out.println("\n ==== Preparing Daily Report  ====");
    manager.dailySwitchReport();
    System.out.println("\n ====  Daily Report Generated  ====");
 }  

}
