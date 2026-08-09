package GridManagerCore.system;

import GridManagerCore.config.GridManagerConfig;
import GridManagerCore.dao.IReportDAO;
import GridManagerCore.factory.EnergySourceFactory;
import GridManagerCore.log.UsageReport;
import GridManagerCore.sources.EnergySource;
import GridManagerCore.database.SwitchReport;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

/**
 * GridSystemManager — Core Orchestrator.
 *
 * SOLID principles applied:
 *
 *   SRP: This class is responsible for the switching workflow only (read sensors,
 *        decide, switch, save, report). Dependencies are injected, not created here.
 *
 *   DIP: All dependencies are received via constructor injection against interfaces
 *        or abstractions (IReportDAO, EnergySourceFactory, UsageReport),
 *        not against concrete implementations.
 *
 * OOP:  {@code bestSource} is private — encapsulation is correctly enforced.
 *        External code accesses it via {@link #getLastSource()}.
 *
 * Null Safety: {@code saveSwitchHistory()} guards against the case where no
 *              switch occurred (e.g. Night mode with low electricity cost).
 */
public class GridSystemManager {

    private final GridManagerConfig config;
    private final EnergySourceFactory factory;
    private final IReportDAO reportDAO;
    private final UsageReport usageReport;
    private final GridManagerCore.prediction.SolarIrradianceIntelligenceService intelligenceService;

    private final List<String> switchLog = new ArrayList<>();

    /** The most recently selected energy source. Null if no switch has occurred. */
    private EnergySource bestSource;

    /**
     * Constructor injection of all dependencies (DIP).
     *
     * @param config      Immutable sensor configuration for this site
     * @param factory     Factory responsible for source selection logic
     * @param reportDAO   Persistence abstraction for switch history
     * @param usageReport Report renderer
     */
    public GridSystemManager(GridManagerConfig config,
                             EnergySourceFactory factory,
                             IReportDAO reportDAO,
                             UsageReport usageReport) {
        this(config, factory, reportDAO, usageReport,
             new GridManagerCore.prediction.SolarIrradianceIntelligenceService(
                 new GridManagerCore.prediction.PhysicalGhiPredictionStrategy()
             ));
    }

    public GridSystemManager(GridManagerConfig config,
                             EnergySourceFactory factory,
                             IReportDAO reportDAO,
                             UsageReport usageReport,
                             GridManagerCore.prediction.SolarIrradianceIntelligenceService intelligenceService) {
        this.config              = config;
        this.factory             = factory;
        this.reportDAO           = reportDAO;
        this.usageReport         = usageReport;
        this.intelligenceService = intelligenceService;
    }

    /** Runs 30-minute ahead solar irradiance (GHI) and PV output drop prediction. */
    public GridManagerCore.prediction.SolarForecast evaluateSolarPrediction30MinAhead() {
        return intelligenceService.evaluateAndNotify(config);
    }

    /** Prints all current sensor readings to the console. */
    public void sensorData() {
        System.out.println(" ====  Sensor Data at " + config.getLocation()
                + " . Time of the day : " + config.getTimeOfDay() + " ====");
        System.out.println(" Industrial Demand : " + config.getIndustrialDemand());
        System.out.println(" Wind Speed        : " + config.getWindSpeed());
        System.out.println(" Solar Irradiance  : " + config.getSolarIrradiance());
        System.out.println(" Electricity Price : " + config.getElectricityCost());
    }

    /**
     * Evaluates sensor data and switches to the optimal energy source.
     * Switching is triggered during Daytime or when electricity cost is high (≥70%).
     * During off-peak low-cost periods the grid is assumed adequate.
     */
    public void intelligentSwitch() {
        System.out.println("Analyzing data for choice of energy source at " + config.getLocation());

        boolean shouldSwitch = config.getTimeOfDay().equalsIgnoreCase("Daytime")
                || config.getElectricityCost() >= 70;

        if (shouldSwitch) {
            this.bestSource = factory.createBestSource(config);
            bestSource.switchTo();

            String entry = "Switched to " + bestSource.getName() + " at "
                    + LocalTime.now().format(DateTimeFormatter.ofPattern("HH:mm:ss"));
            switchLog.add(entry);
            System.out.println("Switch Entry: " + entry);
        } else {
            System.out.println("Off-peak / low-cost period — no switch required. Grid remains active.");
        }
    }

    /**
     * Persists the most recent switch event to the database.
     * Guards against NullPointerException if no switch has occurred.
     */
    public void saveSwitchHistory() {
        if (bestSource == null) {
            System.out.println("No switch event recorded — nothing to save.");
            return;
        }
        System.out.println("\n ==== Saving Switch History at " + config.getLocation() + " ====");
        try {
            reportDAO.insertSwitchData(
                    config.getLocation(),
                    bestSource.getName(),
                    LocalDateTime.now(),
                    config.getIndustrialDemand()
            );
            System.out.println("Logged switch entry: " + bestSource.getName() + " @ " + config.getLocation());
        } catch (IllegalStateException e) {
            System.out.println("Switch History Persistence Notice: SQLite driver unavailable; switch logged to in-memory audit trail.");
        }
    }

    /**
     * Fetches today's switch history from the database and generates a report.
     */
    public void dailySwitchReport() {
        List<SwitchReport> allHistory = new ArrayList<>();
        try {
            allHistory = reportDAO.getAllSwitchHistory();
        } catch (IllegalStateException e) {
            System.out.println("Switch Report Notice: SQLite database driver not loaded on current classpath.");
        }
        LocalDate today = LocalDate.now();

        List<SwitchReport> todaysData = new ArrayList<>();
        for (SwitchReport record : allHistory) {
            if (record.getTimestamp().toLocalDate().equals(today)) {
                todaysData.add(record);
            }
        }

        usageReport.switchReport(
                "Daily Switch Report for " + today,
                config.getLocation(),
                todaysData
        );
    }

    /**
     * Returns the last selected energy source, or null if no switch has occurred.
     * Provided as a read-only accessor — {@code bestSource} is not publicly mutable.
     */
    public EnergySource getLastSource() {
        return bestSource;
    }
}