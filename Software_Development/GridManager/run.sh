#!/bin/bash
JAVA_FX_PATH="/Users/4syt/Library/CloudStorage/OneDrive-4syTIntegratedSolutions/Downloads/MSc Artificial Intelligence/SWE7302/javafx-sdk-25.0.2/lib"
java --module-path "$JAVA_FX_PATH" \
     --add-modules javafx.controls,javafx.fxml \
     src/main/java/GridManagerCore/ui/GridManagerDashboard.java