package GridManagerCore.config;

public class GridManagerConfig 
{
    private final String location;
    private final double industrialDemand;
    private final double windSpeed;
    private final double solarIrradiance;
    private final double electricityCost;
    private final String timeOfDay;

    private GridManagerConfig(GridBuilder buildGrid) {
        this.location = buildGrid.location;
        this.industrialDemand = buildGrid.industrialDemand;
        this.windSpeed = buildGrid.windSpeed;
        this.solarIrradiance = buildGrid.solarIrradiance;
        this.electricityCost = buildGrid.electricityCost;
        this.timeOfDay = buildGrid.timeOfDay; 
    }   

    public String getLocation()          { return location; }
    public double getIndustrialDemand()     { return industrialDemand; }
    public double getWindSpeed()            { return windSpeed; }
    public double getSolarIrradiance()      { return solarIrradiance; }
    public double getElectricityCost()      { return electricityCost; }
    public String getTimeOfDay()         { return timeOfDay; }

    public static class GridBuilder {
    
        private final String location;
        private double industrialDemand;
        private double windSpeed;
        private double solarIrradiance;
        private double electricityCost;
        private String timeOfDay;

        public GridBuilder(String location) {
            this.location = location;
        }
        
        public GridBuilder industrialDemand(double val)    { this.industrialDemand = val; return this; }
        public GridBuilder windSpeed(double val)           { this.windSpeed = val; return this; }
        public GridBuilder solarIrradiance(double val)     { this.solarIrradiance = val; return this; }
        public GridBuilder electricityCost(double val)     { this.electricityCost = val; return this; }
        public GridBuilder timeOfDay(String val)           { this.timeOfDay = val; return this; }
        

        public GridManagerConfig grid() {
            // Validate all percentage values are within the 0-100 range
            if (industrialDemand < 0 || industrialDemand > 100 || windSpeed < 0 || windSpeed > 100 || solarIrradiance < 0 || solarIrradiance > 100 || electricityCost < 0 || electricityCost > 100) {
                throw new IllegalStateException("Review Values. Convert all values to Percentage (0-100)");
            } else 
                 return new GridManagerConfig(this);
        }
    }
}
