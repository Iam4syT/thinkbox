package GridManagerCore.sources;

/**
 * EnergySource — Interface Segregation Principle (ISP) + Liskov Substitution Principle (LSP).
 *
 * ISP: The interface is intentionally small — only the behaviours all energy
 *      sources share. Cost and CO₂ data are included here so each concrete source
 *      carries its own environmental and financial footprint, removing the need for
 *      external string-based lookups on the source name.
 *
 * LSP: Any concrete implementation can replace another anywhere an EnergySource
 *      is expected, without changing system behaviour.
 */
public interface EnergySource {

    /** Executes the switch to this energy source and logs the action. */
    void switchTo();

    /** Returns the canonical display name of this energy source. */
    String getName();

    /**
     * Returns the approximate production cost per kWh ($/kWh).
     * Used for live cost analysis at switch time.
     */
    double getCostPerKwh();

    /**
     * Returns the approximate CO₂ emission intensity (kg CO₂/kWh).
     * Used for live carbon footprint analysis at switch time.
     */
    double getCo2PerKwh();
}