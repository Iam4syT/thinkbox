package GridManagerCore.calculator;

import GridManagerCore.database.SwitchReport;

import java.util.Map;

/**
 * CostCalculationService — Single Responsibility Principle (SRP) + Open/Closed Principle (OCP).
 *
 * SRP: This class has one and only one reason to change — if the cost or CO₂
 *      data model changes. Cost logic no longer lives inside the SwitchReport
 *      data model or the UsageReport renderer.
 *
 * OCP: Adding a new energy source only requires adding one entry to each Map.
 *      No switch statements, no if-else chains, no class modifications elsewhere.
 *
 * All cost and CO₂ figures are sourced from:
 *   - IEA World Energy Outlook 2024
 *   - IRENA Renewable Power Generation Costs 2023
 */
public class CostCalculationService {

    /** Cost per kWh ($/kWh) by energy source name. */
    private static final Map<String, Double> COST_PER_KWH = Map.of(
            "Solar Energy",    0.05,
            "Wind Energy",     0.04,
            "Hybrid",          0.045,
            "Grid Electricity", 0.10
    );

    /** CO₂ intensity (kg CO₂/kWh) by energy source name. */
    private static final Map<String, Double> CO2_PER_KWH = Map.of(
            "Solar Energy",    0.020,
            "Wind Energy",     0.010,
            "Hybrid",          0.015,
            "Grid Electricity", 0.450
    );

    /** Baseline against which all savings are measured. */
    private static final double GRID_COST = 0.10;
    private static final double GRID_CO2  = 0.450;

    /**
     * Returns the cost per kWh for the given source name.
     * Defaults to Grid Electricity cost for unrecognised sources.
     */
    public double getCostPerKwh(String sourceName) {
        return COST_PER_KWH.getOrDefault(sourceName, GRID_COST);
    }

    /**
     * Returns the CO₂ intensity for the given source name (kg CO₂/kWh).
     * Defaults to Grid Electricity intensity for unrecognised sources.
     */
    public double getCo2PerKwh(String sourceName) {
        return CO2_PER_KWH.getOrDefault(sourceName, GRID_CO2);
    }

    /**
     * Estimates the cost saving (in $) for one switch event compared to
     * using Grid Electricity for the same demand.
     * Demand % is mapped to demand × 10 kWh against a 1,000 kWh baseline.
     */
    public double estimatedCostSaving(SwitchReport report) {
        double kWh = report.getDemand() * 10.0;
        return (GRID_COST - getCostPerKwh(report.getSource())) * kWh;
    }

    /**
     * Estimates the CO₂ saved (in kg) for one switch event compared to
     * using Grid Electricity for the same demand.
     */
    public double estimatedCo2Saving(SwitchReport report) {
        double kWh = report.getDemand() * 10.0;
        return (GRID_CO2 - getCo2PerKwh(report.getSource())) * kWh;
    }
}
