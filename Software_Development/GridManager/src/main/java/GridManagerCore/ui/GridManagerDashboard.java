package GridManagerCore.ui;

import GridManagerCore.config.GridManagerConfig;
import GridManagerCore.facade.GridSystemFacade;
import javafx.application.Application;
import javafx.application.Platform;
import javafx.concurrent.Task;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.*;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Stage;

import java.io.OutputStream;
import java.io.PrintStream;

public class GridManagerDashboard extends Application {

    // ── UI Controls ────────────────────────────────────────────────────────────
    private TextArea logArea;
    private ProgressBar progressBar;
    private Button btnStartGrid;
    private Button btnClear;

    private TextField tfLocation;
    private Slider   slDemand;
    private Slider   slWind;
    private Slider   slSolar;
    private Slider   slCost;
    private ComboBox<String> cbTimeOfDay;

    private Label lblDemandVal;
    private Label lblWindVal;
    private Label lblSolarVal;
    private Label lblCostVal;

    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("⚡ GridManager — Energy Source Dashboard");

        // ── Header ──────────────────────────────────────────────────────────────
        Label header = new Label("⚡ Grid Manager");
        header.setFont(Font.font("System", FontWeight.BOLD, 26));
        header.setStyle("-fx-text-fill: #1a73e8;");

        Label subHeader = new Label("Intelligent Energy Source Optimisation");
        subHeader.setStyle("-fx-text-fill: #5f6368; -fx-font-size: 13px;");

        VBox headerBox = new VBox(4, header, subHeader);
        headerBox.setAlignment(Pos.CENTER);

        // ── Input form ──────────────────────────────────────────────────────────
        tfLocation = new TextField("Amsterdam Campus");
        tfLocation.setPromptText("e.g. Amsterdam Campus");

        cbTimeOfDay = new ComboBox<>();
        cbTimeOfDay.getItems().addAll("Daytime", "Night", "Peak", "Off-Peak");
        cbTimeOfDay.setValue("Daytime");
        cbTimeOfDay.setMaxWidth(Double.MAX_VALUE);

        slDemand = buildSlider(60); lblDemandVal = buildValLabel(60);
        slWind   = buildSlider(50); lblWindVal   = buildValLabel(50);
        slSolar  = buildSlider(70); lblSolarVal  = buildValLabel(70);
        slCost   = buildSlider(80); lblCostVal   = buildValLabel(80);

        bindSlider(slDemand, lblDemandVal);
        bindSlider(slWind,   lblWindVal);
        bindSlider(slSolar,  lblSolarVal);
        bindSlider(slCost,   lblCostVal);

        GridPane form = new GridPane();
        form.setHgap(12);
        form.setVgap(10);
        ColumnConstraints col1 = new ColumnConstraints(160);
        ColumnConstraints col2 = new ColumnConstraints();
        col2.setHgrow(Priority.ALWAYS);
        ColumnConstraints col3 = new ColumnConstraints(45);
        form.getColumnConstraints().addAll(col1, col2, col3);

        form.add(new Label("Location:"),            0, 0); form.add(tfLocation,   1, 0, 2, 1);
        form.add(new Label("Time of Day:"),          0, 1); form.add(cbTimeOfDay,  1, 1, 2, 1);
        form.add(new Label("Industrial Demand %:"),  0, 2); form.add(slDemand,     1, 2); form.add(lblDemandVal, 2, 2);
        form.add(new Label("Wind Speed %:"),         0, 3); form.add(slWind,       1, 3); form.add(lblWindVal,   2, 3);
        form.add(new Label("Solar Irradiance %:"),   0, 4); form.add(slSolar,      1, 4); form.add(lblSolarVal,  2, 4);
        form.add(new Label("Electricity Cost %:"),   0, 5); form.add(slCost,       1, 5); form.add(lblCostVal,   2, 5);

        TitledPane inputPane = new TitledPane("📋 Sensor Configuration", form);
        inputPane.setCollapsible(false);
        inputPane.setStyle("-fx-font-weight: bold;");

        // ── Log area ────────────────────────────────────────────────────────────
        logArea = new TextArea();
        logArea.setEditable(false);
        logArea.setWrapText(true);
        logArea.setPrefHeight(240);
        logArea.setStyle("-fx-font-family: monospace; -fx-font-size: 12px;");

        // Redirect System.out and System.err into the log area
        redirectConsoleToLog();

        TitledPane logPane = new TitledPane("📜 System Log", logArea);
        logPane.setCollapsible(false);
        logPane.setStyle("-fx-font-weight: bold;");

        // ── Progress bar ────────────────────────────────────────────────────────
        progressBar = new ProgressBar(0);
        progressBar.setVisible(false);
        progressBar.setPrefWidth(Double.MAX_VALUE);

        // ── Buttons ─────────────────────────────────────────────────────────────
        btnStartGrid = new Button("🚀  Initialise Grid");
        btnStartGrid.setStyle("-fx-font-size: 14px; -fx-padding: 10 24; "
                + "-fx-background-color: #1a73e8; -fx-text-fill: white; -fx-background-radius: 6;");
        btnStartGrid.setMaxWidth(Double.MAX_VALUE);
        btnStartGrid.setOnAction(e -> startGridInitialization());

        btnClear = new Button("🗑  Clear Log");
        btnClear.setStyle("-fx-font-size: 14px; -fx-padding: 10 24; -fx-background-radius: 6;");
        btnClear.setMaxWidth(Double.MAX_VALUE);
        btnClear.setOnAction(e -> {
            logArea.clear();
            btnStartGrid.setText("🚀  Initialise Grid");
            btnStartGrid.setStyle("-fx-font-size: 14px; -fx-padding: 10 24; "
                    + "-fx-background-color: #1a73e8; -fx-text-fill: white; -fx-background-radius: 6;");
        });

        HBox buttonBox = new HBox(12, btnStartGrid, btnClear);
        buttonBox.setAlignment(Pos.CENTER);
        HBox.setHgrow(btnStartGrid, Priority.ALWAYS);
        HBox.setHgrow(btnClear, Priority.ALWAYS);

        // ── Root layout ─────────────────────────────────────────────────────────
        VBox root = new VBox(16, headerBox, inputPane, logPane, progressBar, buttonBox);
        root.setPadding(new Insets(24));
        root.setStyle("-fx-background-color: #f8f9fa;");

        Scene scene = new Scene(root, 760, 680);
        primaryStage.setScene(scene);
        primaryStage.setResizable(true);
        primaryStage.show();
    }

    // ── Slider helpers ──────────────────────────────────────────────────────────
    private Slider buildSlider(double initial) {
        Slider s = new Slider(0, 100, initial);
        s.setShowTickMarks(true);
        s.setShowTickLabels(true);
        s.setMajorTickUnit(25);
        s.setBlockIncrement(5);
        return s;
    }

    private Label buildValLabel(double val) {
        Label l = new Label(String.valueOf((int) val));
        l.setStyle("-fx-font-weight: bold; -fx-min-width: 35;");
        l.setAlignment(Pos.CENTER_RIGHT);
        return l;
    }

    private void bindSlider(Slider slider, Label label) {
        slider.valueProperty().addListener((obs, o, n) ->
                label.setText(String.valueOf(n.intValue())));
    }

    // ── Redirect System.out / System.err → log TextArea ─────────────────────────
    private void redirectConsoleToLog() {
        PrintStream ps = new PrintStream(new OutputStream() {
            private final StringBuilder sb = new StringBuilder();

            @Override
            public void write(int b) {
                char c = (char) b;
                sb.append(c);
                if (c == '\n') {
                    String line = sb.toString();
                    sb.setLength(0);
                    Platform.runLater(() -> logArea.appendText(line));
                }
            }
        }, true);
        System.setOut(ps);
        System.setErr(ps);
    }

    // ── Grid initialisation task ────────────────────────────────────────────────
    private void startGridInitialization() {
        String location = tfLocation.getText().trim();
        if (location.isEmpty()) {
            showAlert("Validation Error", "Location cannot be empty.");
            return;
        }

        btnStartGrid.setDisable(true);
        btnClear.setDisable(true);
        progressBar.setVisible(true);
        progressBar.setProgress(ProgressBar.INDETERMINATE_PROGRESS);
        System.out.println("🚀 Starting Grid initialisation for: " + location);

        Task<Void> task = new Task<>() {
            @Override
            protected Void call() {
                try {
                    GridManagerConfig config = new GridManagerConfig.GridBuilder(location)
                            .industrialDemand(slDemand.getValue())
                            .windSpeed(slWind.getValue())
                            .solarIrradiance(slSolar.getValue())
                            .electricityCost(slCost.getValue())
                            .timeOfDay(cbTimeOfDay.getValue())
                            .grid();

                    GridSystemFacade facade = new GridSystemFacade(config);
                    facade.initialize();
                } catch (Exception e) {
                    System.out.println("❌ Error: " + e.getMessage());
                }
                return null;
            }

            @Override protected void succeeded() { finish("✅ Done.", true); }
            @Override protected void failed()    { finish("❌ Failed.", false); }
        };

        new Thread(task).start();
    }

    private void finish(String msg, boolean success) {
        Platform.runLater(() -> {
            System.out.println(msg);
            progressBar.setVisible(false);
            btnStartGrid.setDisable(false);
            btnClear.setDisable(false);
            if (success) {
                btnStartGrid.setText("🔄  Run Again");
                btnStartGrid.setStyle("-fx-font-size: 14px; -fx-padding: 10 24; "
                        + "-fx-background-color: #34a853; -fx-text-fill: white; -fx-background-radius: 6;");
            }
        });
    }

    private void showAlert(String title, String message) {
        Alert alert = new Alert(Alert.AlertType.WARNING);
        alert.setTitle(title);
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }

    public static void main(String[] args) {
        launch(args);
    }
}