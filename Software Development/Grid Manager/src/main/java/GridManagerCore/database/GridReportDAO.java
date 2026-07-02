package GridManagerCore.database;

import GridManagerCore.dao.IReportDAO;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.Timestamp;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * GridReportDAO — implements IReportDAO (Dependency Inversion Principle).
 *
 * DIP:  High-level modules depend on IReportDAO, not this concrete class.
 *       This class can be swapped for any other IReportDAO implementation
 *       (e.g. an in-memory mock for testing) without changing business logic.
 *
 * Singleton: Uses a thread-safe double-checked locking pattern to guarantee
 *            exactly one database connection is used across the application.
 */
public class GridReportDAO implements IReportDAO {

    private static volatile GridReportDAO instance;
    private final GridDbHandler db;

    private GridReportDAO() {
        this.db = GridDbHandler.getInstance();
    }

    /**
     * Thread-safe lazy singleton accessor using double-checked locking.
     */
    public static GridReportDAO getInstance() {
        if (instance == null) {
            synchronized (GridReportDAO.class) {
                if (instance == null) {
                    instance = new GridReportDAO();
                }
            }
        }
        return instance;
    }

    /** {@inheritDoc} */
    @Override
    public void insertSwitchData(String location, String source,
                                 LocalDateTime timestamp, double demand) {
        String sql = "INSERT INTO SwitchHistory (location, source, timestamp, demand) VALUES (?, ?, ?, ?)";
        try (PreparedStatement pstmt = db.getConnection().prepareStatement(sql)) {
            pstmt.setString(1, location);
            pstmt.setString(2, source);
            pstmt.setTimestamp(3, Timestamp.valueOf(timestamp));
            pstmt.setDouble(4, demand);
            pstmt.executeUpdate();
            System.out.println("Switch data inserted successfully for " + location);
        } catch (SQLException e) {
            System.err.println("Failed to insert switch data: " + e.getMessage());
        }
    }

    /** {@inheritDoc} */
    @Override
    public List<SwitchReport> getAllSwitchHistory() {
        List<SwitchReport> reports = new ArrayList<>();
        String sql = "SELECT * FROM SwitchHistory";
        try (Statement stmt = db.getConnection().createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            while (rs.next()) {
                reports.add(new SwitchReport(
                        rs.getInt("id"),
                        rs.getString("location"),
                        rs.getString("source"),
                        rs.getTimestamp("timestamp").toLocalDateTime(),
                        rs.getDouble("demand")
                ));
            }
        } catch (SQLException e) {
            System.err.println("Failed to retrieve switch history: " + e.getMessage());
        }
        return Collections.unmodifiableList(reports);
    }
}
