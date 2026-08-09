package GridManagerCore.prediction;

import GridManagerCore.config.GridManagerConfig;

/**
 * GhiPredictionStrategy — Strategy Pattern interface for GHI & PV Drop Predictions.
 *
 * SOLID Principles applied:
 *   OCP: Allows adding machine learning models, physics-based transmittivity models,
 *        or weather API integrations without modifying core grid management code.
 *   DIP: High-level intelligence services depend on this abstraction.
 */
public interface GhiPredictionStrategy {

    /**
     * Predicts GHI and PV output 30 minutes ahead using site configuration and sensor data.
     *
     * @param config GridManagerConfig holding current sensor parameters
     * @return SolarForecast containing 30-min ahead prediction and alert evaluation
     */
    SolarForecast predict30MinAhead(GridManagerConfig config);
}
