package GridManagerCore.facade;

import GridManagerCore.calculator.CostCalculationService;
import GridManagerCore.config.GridManagerConfig;
import GridManagerCore.database.GridReportDAO;
import GridManagerCore.factory.EnergySourceFactory;
import GridManagerCore.log.UsageReport;
import GridManagerCore.system.GridSystemManager;

public class GridSystemFacade {

    private final GridSystemManager manager;

    public GridSystemFacade(GridManagerConfig config) {
        this.manager = new GridSystemManager(
            config,
            EnergySourceFactory.withDefaultStrategies(),
            GridReportDAO.getInstance(),
            new UsageReport(new CostCalculationService())
        );
    }

    public void initialize() {
        System.out.println("\n ==== Initializing Grid System ====");
        manager.sensorData();

        // Intelligent 30-minute ahead GHI and PV output prediction
        manager.evaluateSolarPrediction30MinAhead();

        manager.intelligentSwitch();
        manager.saveSwitchHistory();
        System.out.println("\n ==== Grid System Initialization Successful ====");

        System.out.println("\n ==== Preparing Daily Report ====");
        manager.dailySwitchReport();
        System.out.println("\n ==== Daily Report Generated ====");
    }
}
