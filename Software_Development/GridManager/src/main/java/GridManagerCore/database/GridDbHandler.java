package GridManagerCore.database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * GridDbHandler — Thread-safe Singleton for SQLite connection management.
 *
 * Singleton: Ensures only one Connection is created for the lifetime of
 *            the application, preventing resource exhaustion and connection conflicts.
 *
 * Thread Safety: Uses double-checked locking with a volatile field to prevent
 *                race conditions in concurrent environments.
 *
 * SRP: Responsible only for managing the database connection and initialising
 *      the schema. Query execution is delegated to GridReportDAO.
 */
public class GridDbHandler {

    private static volatile GridDbHandler instance;
    private Connection connection;

    private static final String DB_URL = "jdbc:sqlite:energy.db";

    private GridDbHandler() {
        try {
            this.connection = DriverManager.getConnection(DB_URL);
            System.out.println("Connected to SQLite database: " + DB_URL);
            initializeSchema();
        } catch (SQLException e) {
            System.err.println("Database connection error: " + e.getMessage());
        }
    }

    /**
     * Thread-safe lazy singleton accessor using double-checked locking.
     */
    public static GridDbHandler getInstance() {
        if (instance == null) {
            synchronized (GridDbHandler.class) {
                if (instance == null) {
                    instance = new GridDbHandler();
                }
            }
        }
        return instance;
    }

    /**
     * Creates the SwitchHistory table if it does not already exist.
     * Called once at construction time.
     */
    private void initializeSchema() {
        String sql = "CREATE TABLE IF NOT EXISTS SwitchHistory ("
                + "id        INTEGER PRIMARY KEY AUTOINCREMENT,"
                + "location  TEXT    NOT NULL,"
                + "source    TEXT    NOT NULL,"
                + "timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,"
                + "demand    DOUBLE  NOT NULL"
                + ");";
        try (Statement stmt = connection.createStatement()) {
            stmt.execute(sql);
            System.out.println("SwitchHistory schema initialised successfully.");
        } catch (SQLException e) {
            System.err.println("Schema initialisation error: " + e.getMessage());
        }
    }

    /**
     * Returns the active database connection.
     *
     * @throws IllegalStateException if the connection was never established
     */
    public Connection getConnection() {
        if (connection == null) {
            throw new IllegalStateException(
                    "No database connection available. Check DB_URL and SQLite driver.");
        }
        return connection;
    }
}
