package GridManagerTest.java.com.store.core;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static org.junit.jupiter.api.Assertions.*;

import GridManagerCore.config.GridManagerConfig;
import GridManagerCore.factory.EnergySourceFactory;
import GridManagerCore.sources.EnergySource;

@DisplayName("Energy Source Strategy Tests")
public class StrategyTest {

    private final EnergySourceFactory factory = EnergySourceFactory.withDefaultStrategies();

    /** Convenience builder to reduce repetition in tests. */
    private GridManagerConfig build(double demand, double wind, double solar, double cost, String time) {
        return new GridManagerConfig.GridBuilder("Test Site")
                .industrialDemand(demand)
                .windSpeed(wind)
                .solarIrradiance(solar)
                .electricityCost(cost)
                .timeOfDay(time)
                .grid();
    }

    // ── Solar Strategy ─────────────────────────────────────────────────────────

    @Test
    @DisplayName("Solar selected when solar > wind AND solar > demand")
    void testSolarWins() {
        // solar(80) > wind(40) && solar(80) > demand(50) → Solar
        GridManagerConfig config = build(50, 40, 80, 70, "Daytime");
        EnergySource source = factory.createBestSource(config);
        assertEquals("Solar Energy", source.getName());
    }

    @Test
    @DisplayName("Solar selected at boundary: solar just above demand and wind")
    void testSolarAtBoundary() {
        // solar(60) > wind(40) && solar(60) > demand(55) → Solar
        GridManagerConfig config = build(55, 40, 60, 70, "Daytime");
        EnergySource source = factory.createBestSource(config);
        assertEquals("Solar Energy", source.getName());
    }

    // ── Wind Strategy ──────────────────────────────────────────────────────────

    @Test
    @DisplayName("Wind selected when wind > solar AND wind > demand")
    void testWindWins() {
        // wind(90) > solar(30) && wind(90) > demand(40) → Wind
        GridManagerConfig config = build(40, 90, 30, 60, "Daytime");
        EnergySource source = factory.createBestSource(config);
        assertEquals("Wind Energy", source.getName());
    }

    // ── Hybrid Strategy ────────────────────────────────────────────────────────

    @Test
    @DisplayName("Hybrid selected when solar >= wind >= demand")
    void testHybridWins() {
        // solar(80) >= wind(70) >= demand(50) → Hybrid
        GridManagerConfig config = build(50, 70, 80, 60, "Daytime");
        EnergySource source = factory.createBestSource(config);
        assertEquals("Hybrid", source.getName());
    }

    // ── Grid Fallback ──────────────────────────────────────────────────────────

    @Test
    @DisplayName("Grid Electricity selected when no renewable source qualifies")
    void testGridFallback() {
        // demand(95) > solar(20) && demand(95) > wind(30) → Grid fallback
        GridManagerConfig config = build(95, 30, 20, 50, "Daytime");
        EnergySource source = factory.createBestSource(config);
        assertEquals("Grid Electricity", source.getName());
    }

    // ── Config Validation ──────────────────────────────────────────────────────

    @Test
    @DisplayName("Config with boundary values 0 and 100 is valid")
    void testConfigBoundaryValuesValid() {
        assertDoesNotThrow(() -> build(0, 100, 50, 0, "Night"));
    }

    @Test
    @DisplayName("Config with value > 100 throws IllegalStateException")
    void testConfigValidationOver100() {
        assertThrows(IllegalStateException.class, () ->
                new GridManagerConfig.GridBuilder("Bad Campus")
                        .industrialDemand(101)
                        .windSpeed(50)
                        .solarIrradiance(50)
                        .electricityCost(50)
                        .timeOfDay("Daytime")
                        .grid()
        );
    }

    @Test
    @DisplayName("Config with negative value throws IllegalStateException")
    void testConfigValidationNegative() {
        assertThrows(IllegalStateException.class, () ->
                new GridManagerConfig.GridBuilder("Bad Campus")
                        .industrialDemand(50)
                        .windSpeed(-1)
                        .solarIrradiance(50)
                        .electricityCost(50)
                        .timeOfDay("Daytime")
                        .grid()
        );
    }
}
