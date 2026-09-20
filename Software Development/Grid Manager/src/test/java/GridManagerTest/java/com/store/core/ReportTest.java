package GridManagerTest.java.com.store.core;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static org.junit.jupiter.api.Assertions.*;

import GridManagerCore.database.SwitchReport;
import GridManagerCore.calculator.CostCalculationService;

import java.time.LocalDateTime;

@DisplayName("SwitchReport Cost & CO₂ Calculation Tests")
public class ReportTest {
    private final CostCalculationService costService = new CostCalculationService();

    /** Convenience factory for test reports. */
    private SwitchReport makeReport(String source, double demand) {
        return new SwitchReport(1, "Test Site", source, LocalDateTime.now(), demand);
    }

    // ── Cost savings ───────────────────────────────────────────────────────────

    @Test
    @DisplayName("Solar: cost saving is positive vs Grid baseline")
    void testSolarCostSaving() {
        SwitchReport r = makeReport("Solar Energy", 60);
        // Solar ($0.05) is cheaper than Grid ($0.10) → saving > 0
        assertTrue(costService.estimatedCostSaving(r) > 0, "Solar should save cost vs Grid");
    }

    @Test
    @DisplayName("Wind: highest cost saving vs Grid (cheapest at $0.04/kWh)")
    void testWindHighestSaving() {
        SwitchReport solar = makeReport("Solar Energy", 60);
        SwitchReport wind  = makeReport("Wind Energy",  60);
        assertTrue(costService.estimatedCostSaving(wind) > costService.estimatedCostSaving(solar),
                "Wind ($0.04) should save more than Solar ($0.05)");
    }

    @Test
    @DisplayName("Hybrid: cost saving between Wind and Solar")
    void testHybridSavingBetweenWindAndSolar() {
        SwitchReport wind   = makeReport("Wind Energy",  60);
        SwitchReport hybrid = makeReport("Hybrid",       60);
        SwitchReport solar  = makeReport("Solar Energy", 60);
        assertTrue(costService.estimatedCostSaving(hybrid) < costService.estimatedCostSaving(wind));
        assertTrue(costService.estimatedCostSaving(hybrid) > costService.estimatedCostSaving(solar));
    }

    @Test
    @DisplayName("Grid Electricity: zero cost saving (it IS the baseline)")
    void testGridZeroSaving() {
        SwitchReport r = makeReport("Grid Electricity", 60);
        assertEquals(0.0, costService.estimatedCostSaving(r), 0.001);
    }

    // ── CO₂ savings ────────────────────────────────────────────────────────────

    @Test
    @DisplayName("Solar: CO₂ saving is positive vs Grid")
    void testSolarCo2Saving() {
        SwitchReport r = makeReport("Solar Energy", 60);
        assertTrue(costService.estimatedCo2Saving(r) > 0);
    }

    @Test
    @DisplayName("Wind: highest CO₂ saving (lowest emission at 0.01 kg/kWh)")
    void testWindCo2GreaterThanSolar() {
        SwitchReport solar = makeReport("Solar Energy", 60);
        SwitchReport wind  = makeReport("Wind Energy",  60);
        assertTrue(costService.estimatedCo2Saving(wind) > costService.estimatedCo2Saving(solar));
    }

    @Test
    @DisplayName("Grid: zero CO₂ saving (baseline source)")
    void testGridZeroCo2Saving() {
        SwitchReport r = makeReport("Grid Electricity", 60);
        assertEquals(0.0, costService.estimatedCo2Saving(r), 0.001);
    }

    // ── Demand scaling ─────────────────────────────────────────────────────────

    @Test
    @DisplayName("Higher demand produces proportionally higher savings")
    void testHigherDemandHigherSaving() {
        SwitchReport low  = makeReport("Solar Energy", 30);
        SwitchReport high = makeReport("Solar Energy", 90);
        assertTrue(costService.estimatedCostSaving(high) > costService.estimatedCostSaving(low));
        assertTrue(costService.estimatedCo2Saving(high)  > costService.estimatedCo2Saving(low));
    }

    @Test
    @DisplayName("Zero demand produces zero savings")
    void testZeroDemandZeroSaving() {
        SwitchReport r = makeReport("Solar Energy", 0);
        assertEquals(0.0, costService.estimatedCostSaving(r), 0.001);
        assertEquals(0.0, costService.estimatedCo2Saving(r),  0.001);
    }
}
