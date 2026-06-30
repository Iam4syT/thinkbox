package GridManagerCore.factory;

import GridManagerCore.config.GridManagerConfig;
import GridManagerCore.sources.EnergySource;
import GridManagerCore.sources.GridEnergySource;
import GridManagerCore.strategy.HybridStrategy;
import GridManagerCore.strategy.SolarStrategy;
import GridManagerCore.strategy.SourceStrategy;
import GridManagerCore.strategy.WindStrategy;

import java.util.List;

/**
 * EnergySourceFactory — Open/Closed Principle (OCP) + Dependency Inversion (DIP).
 *
 * OCP:  The factory is open for extension and closed for modification.
 *       Adding a new energy source strategy requires no changes to this class —
 *       simply pass a different list of strategies via the constructor.
 *
 * DIP:  The factory depends on the SourceStrategy abstraction, not on any
 *       concrete strategy implementation.
 *
 * The static {@link #withDefaultStrategies()} factory method provides the standard
 * production configuration without forcing callers to know the strategy list.
 */
public class EnergySourceFactory {

    private final List<SourceStrategy> strategies;

    /**
     * Constructor injection — strategies are supplied by the caller (DIP, OCP).
     * The list is copied defensively to guarantee immutability after construction.
     *
     * @param strategies An ordered list of strategies to evaluate, highest priority first.
     */
    public EnergySourceFactory(List<SourceStrategy> strategies) {
        this.strategies = List.copyOf(strategies);
    }

    /**
     * Convenience factory method that builds the standard production strategy set:
     * Hybrid → Solar → Wind → Grid (fallback).
     * Hybrid is evaluated first because it is the most efficient combined state.
     *
     * @return a configured EnergySourceFactory with default strategies
     */
    public static EnergySourceFactory withDefaultStrategies() {
        return new EnergySourceFactory(List.of(
                new HybridStrategy(),
                new SolarStrategy(),
                new WindStrategy()
        ));
    }

    /**
     * Evaluates each strategy in priority order and returns the first source
     * whose conditions are met. Falls back to Grid Electricity if none qualify.
     *
     * @param config the current sensor readings and site configuration
     * @return the best available EnergySource for the given conditions
     */
    public EnergySource createBestSource(GridManagerConfig config) {
        return strategies.stream()
                .filter(strategy -> strategy.isBest(config))
                .findFirst()
                .map(SourceStrategy::getSource)
                .orElse(new GridEnergySource());
    }
}
