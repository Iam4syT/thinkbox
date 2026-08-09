package GridManagerCore.prediction;

import GridManagerCore.config.GridManagerConfig;

/**
 * PredictionListener — Observer Pattern interface for 30-minute ahead PV Output Drop Alerts.
 *
 * SOLID Principles applied:
 *   ISP: Focused strictly on prediction events.
 *   OCP: Allows attaching multiple notification channels (Console, SMS, Database, Dashboard UI)
 *        without changing the prediction service.
 */
public interface PredictionListener {

    /**
     * Triggered when a 30-minute ahead solar irradiance / PV output drop prediction is generated.
     *
     * @param forecast Prediction forecast object
     * @param config   Current site configuration
     */
    void onPredictionEvaluated(SolarForecast forecast, GridManagerConfig config);
}
