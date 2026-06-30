package GridManagerCore.dao;

import GridManagerCore.database.SwitchReport;

import java.time.LocalDateTime;
import java.util.List;

/**
 * IReportDAO — Dependency Inversion Principle (DIP).
 *
 * High-level modules (GridSystemManager) depend on this abstraction,
 * not on the concrete GridReportDAO implementation. This decouples
 * business logic from the persistence layer and makes the system
 * testable without a real database.
 */
public interface IReportDAO {

    /**
     * Persists a single energy-source switch event to storage.
     *
     * @param location  The campus or site name
     * @param source    The name of the energy source switched to
     * @param timestamp The exact date-time of the switch
     * @param demand    The industrial demand percentage at time of switch
     */
    void insertSwitchData(String location, String source, LocalDateTime timestamp, double demand);

    /**
     * Retrieves the full switch history from storage.
     *
     * @return An unmodifiable list of all historical SwitchReport records
     */
    List<SwitchReport> getAllSwitchHistory();
}
