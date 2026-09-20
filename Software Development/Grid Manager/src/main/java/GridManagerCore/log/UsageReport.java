package GridManagerCore.log;

import GridManagerCore.calculator.CostCalculationService;
import GridManagerCore.database.SwitchReport;

import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * UsageReport — Single Responsibility Principle (SRP) + Dependency Inversion (DIP).
 *
 * SRP:  This class is responsible for one thing only: formatting and printing
 *       switch reports. Cost calculations are delegated to CostCalculationService.
 *
 * DIP:  CostCalculationService is injected, not created internally.
 *       This decouples report rendering from cost calculation logic.
 */
public class UsageReport {

    private final CostCalculationService costService;

    /**
     * Constructor injection of CostCalculationService (DIP).
     *
     * @param costService the service responsible for cost and CO₂ calculations
     */
    public UsageReport(CostCalculationService costService) {
        this.costService = costService;
    }

    /**
     * Prints a formatted daily switch report with illustrative cost and CO₂ arithmetic.
     *
     * @param title         Report title (e.g. "Daily Switch Report for 2026-06-28")
     * @param location      Campus or site name
     * @param todaysSwitches List of today's SwitchReport records from the database
     */
    public void switchReport(String title, String location, List<SwitchReport> todaysSwitches) {
        System.out.println("\n ==== " + title + " at " + location + " ====");
        System.out.println("Total Switches Made : " + todaysSwitches.size());

        if (todaysSwitches.isEmpty()) {
            System.out.println("No switch data recorded today.");
            return;
        }

        // Aggregate cost and CO₂ savings across all switches today
        double totalCostSaving = todaysSwitches.stream()
                .mapToDouble(costService::estimatedCostSaving)
                .sum();

        double totalCo2Saving = todaysSwitches.stream()
                .mapToDouble(costService::estimatedCo2Saving)
                .sum();

        // Count how many times each source was used today
        Map<String, Long> sourceCounts = todaysSwitches.stream()
                .collect(Collectors.groupingBy(SwitchReport::getSource, Collectors.counting()));

        // Recommend the most-used source today
        String recommendation = sourceCounts.entrySet().stream()
                .max(Map.Entry.comparingByValue())
                .map(Map.Entry::getKey)
                .orElse("Unknown");

        System.out.printf("Scenario cost difference:  $%.2f (vs. all-Grid baseline)%n", totalCostSaving);
        System.out.printf("Scenario CO\u2082 difference: %.2f kg CO\u2082%n", totalCo2Saving);
        System.out.println("Source Breakdown    : " + sourceCounts);
        System.out.println("Most selected source: '" + recommendation
                + "' \u2014 selection frequency does not establish efficiency.");
    }

    /** Prints the switch history section header. */
    public void history() {
        System.out.println("\n ==== Viewing Grid Switch History ====");
    }
}