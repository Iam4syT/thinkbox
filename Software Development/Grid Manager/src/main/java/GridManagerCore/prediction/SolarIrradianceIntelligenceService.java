package GridManagerCore.prediction;

import GridManagerCore.config.GridManagerConfig;

import java.util.ArrayList;
import java.util.List;

/**
 * SolarIrradianceIntelligenceService — Orchestrates 30-minute ahead solar irradiance
 * prediction and publishes drop notifications to registered observers.
 *
 * SOLID Principles applied:
 *   SRP: Manages prediction orchestration and observer notifications.
 *   DIP: Strategy and listeners are injected as interfaces.
 */
public class SolarIrradianceIntelligenceService {

    private final GhiPredictionStrategy predictionStrategy;
    private final List<PredictionListener> listeners = new ArrayList<>();

    public SolarIrradianceIntelligenceService(GhiPredictionStrategy predictionStrategy) {
        this.predictionStrategy = predictionStrategy;
        // Default observer
        this.listeners.add(new ConsolePredictionListener());
    }

    public void addListener(PredictionListener listener) {
        if (listener != null) {
            listeners.add(listener);
        }
    }

    public SolarForecast evaluateAndNotify(GridManagerConfig config) {
        SolarForecast forecast = predictionStrategy.predict30MinAhead(config);
        for (PredictionListener listener : listeners) {
            listener.onPredictionEvaluated(forecast, config);
        }
        return forecast;
    }
}
