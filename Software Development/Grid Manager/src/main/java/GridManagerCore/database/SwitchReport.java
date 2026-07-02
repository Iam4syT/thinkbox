package GridManagerCore.database;

import java.time.LocalDateTime;

/**
 * SwitchReport — Pure Data Model (Single Responsibility Principle).
 *
 * SRP: This class has exactly one responsibility — to represent a single
 *      switch event record as retrieved from the database. It contains no
 *      business logic, no cost calculations, and no formatting.
 *
 *      Cost and CO₂ calculations have been moved to CostCalculationService,
 *      which is the single class responsible for that concern.
 */
public class SwitchReport {

    private final int id;
    private final String location;
    private final String source;
    private final LocalDateTime timestamp;
    private final double demand;

    public SwitchReport(int id, String location, String source,
                        LocalDateTime timestamp, double demand) {
        this.id        = id;
        this.location  = location;
        this.source    = source;
        this.timestamp = timestamp;
        this.demand    = demand;
    }

    public int getId()                  { return id; }
    public String getLocation()         { return location; }
    public String getSource()           { return source; }
    public LocalDateTime getTimestamp() { return timestamp; }
    public double getDemand()           { return demand; }

    @Override
    public String toString() {
        return String.format("SwitchReport{id=%d, location='%s', source='%s', timestamp=%s, demand=%.1f}",
                id, location, source, timestamp, demand);
    }
}
