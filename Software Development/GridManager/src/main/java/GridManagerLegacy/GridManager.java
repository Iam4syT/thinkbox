package GridManagerLegacy;

import java.util.ArrayList;
import java.util.List;

public class GridManager {
     public static void main(String[] args) throws Exception {
        GridManagerSystem gridManager1 = new GridManagerSystem("Amsterdam Campus", 60, 50, 70, 80, "Daytime");
        gridManager1.Sensors();
        gridManager1.IntelligentSwitch();
        gridManager1.saveSwitchHistory();
        gridManager1.dailySwitchReport();
     }
        
}

class GridManagerSystem {
    private String location;
    private int IndustrialDemand;
    private int windspeed;
    private int solarIrradiance;
    private int electricityCost;
    private String timeofDay;

    private List<String> switchHistory = new ArrayList<>();



    public GridManagerSystem(String location, int IndustrialDemand, int windspeed, int solarIrradiance, int electricityCost, String timeofDay) {
        this.location = location;
        this.IndustrialDemand = IndustrialDemand;
        this.windspeed = windspeed;
        this.solarIrradiance = solarIrradiance;
        this.electricityCost = electricityCost;
        this.timeofDay = timeofDay;
    }


    public void Sensors() {

        System.out.println(" ==== Reading Sensors at " + location + " . " + "Time of the day : " + timeofDay + "====");
        System.out.println(" Industrial Demand : " + IndustrialDemand);
        System.out.println(" Wind Speed : " + windspeed);
        System.out.println(" Solar Irradiance : " + solarIrradiance);
        System.out.println(" Electricity Price : " + electricityCost);
    }

    public void IntelligentSwitch() {
        // Based on Sensor data and AI analysis
        System.out.println("Analyzing data for choice of energy source at " + location);

        /* 

        All metrics such as solar irradiance,  and wind speed are converted to a percentage of their historical maximums.
        Same as Industrial demand is converted to a percentage of the maximum demand historically recorded for that region
        Hence if energy output of sources is 1000kw/h and Demand is 800kw/h, it will be converted to 80% demand and 100% energy output.
        Thiis makes it easier to compare and make decisions based on the relative strength of each source and demand.

        0 - 45 = Low
        46 - 69 = Medium
        70 - 100 = High

        i.e if historically the  average hottest a region has gotten is 800 W/m², it will be converted to a percent, hence 100%. 
        on a day that is 600 W/m², it will be converted to 75% and categorized as High.
        on a day that is 500 W/m², it will be converted to 62.5% and categorized as Medium.
        On a day that is 400 W/m², it will be converted to 50% and categorized as Low.
        
        when it is low, energy is switched to a different source
        when it is medium, it will  be used as hybrid
        when it is high, it will be used as primary source

        Cost of Electricity is also a factor, if it is high, the system will prioritize cheaper sources even if they are not at their maximum output.
        Real Cost of electricty is calclated by the amount of waste such as co2 emitted per kWh of energy produced from each source, OPEX, CAPEX and the current price of electricity from the grid.

        Current price is measured by comparing the current price to the historical average price for that time of day and season. 
        The system will prioritize sources based on  Real Costs, especially if the hybrid state meets demand. 
        This ensures that the system is not only optimizing for energy output but also for cost efficiency, providing a more balanced and economical energy management strategy.

        Cost of electricty is calculated by how much it costs to produce 1 kWh of energy from each source, and the current real cost of electricity from the grid.
        
        Historically, the cost of producing 1 kWh of energy from solar is $0.05, from wind is $0.04 and from the grid is $0.10.

                           ================================================================
                              SYSTEM VARIABLE DEFINITIONS: REAL COST CALCULATION [Cr(s)]
                           ================================================================

                            VARIABLE    | DEFINITION          | EXPLANATION
                            ------------|---------------------|---------------------------------------
                            Cr(s)       | Real Cost           | The final value used by the system to 
                                        |                     | prioritize sources ($/kWh).
                                        |                     |
                            COPE        | Operating Cost      | Maintenance and fuel costs per kWh.
                                        |                     |
                            CAPX        | Capital Cost        | The "payback" cost of the equipment 
                                        |                     | over its lifespan per kWh.
                                        |                     |
                            Eco2        | Emission Intensity  | Amount of CO2 emitted per kWh 
                                        |                     | (e.g., kg/kWh).
                                        |                     |
                            Ptax        | Carbon Price        | A "penalty" factor that converts 
                                        |                     | emissions into a dollar value.
                                        |                     |
                            dP_grid     | Grid Deviation      | P_current - P_avg. If current price is 
                                        |                     | higher than history, value is positive
                            ----------------------------------------------------------------
                                 Note: Cr(s) = (COPE + CAPX) + (Eco2 * Ptax) + dP_grid
                            ================================================================

        dP_grid = (P_current - P_avg)
        * P_current: The real-time price of electricity from the grid.
        * P_avg: The historical average price for the current Time-of-Use (ToU) and Season.

        LCOE is the levelized cost of energy, which is the average cost of producing 1 kWh of energy from a source over its lifetime, 
        including capital costs, operation and maintenance costs, fuel costs (if any) and decommissioning costs. LCOE = (COPE + CAPX)  

        Each source will be calculated and grouped into High, Medium, Low.

        and cost of each source will be calculated then compared to each other.

        this way, it can be empirically determined, if despite having Wind and Solar, the Grid is the most economical, sustainable and efficient choice."

        */

        int Solar = solarIrradiance;
        int Wind = windspeed;
        int Demand = IndustrialDemand;
        String bestSource = " ";
        //Using values from Data Analytics
        if (timeofDay.equals("Daytime") || electricityCost >=70 ) {    
            if (Solar > Wind && Solar > Demand) {
                bestSource = "Solar Energy";
                System.out.println( "Solar is best choice for demand. Switching to " + bestSource);
            } else if (Wind > Solar && Wind > Demand) {
                bestSource = "Wind Energy";
                System.out.println( "Wind is best choice for demand. Switching to" + bestSource);
            }else if (Solar >= Wind && Solar >= Demand && Wind >= Demand) {
                bestSource = "Hybrid";
                System.out.println( "Both Solar and Wind are great choices for demand. Switching to " + bestSource);

            } else {
                bestSource = "Grid Electricity";
                System.out.println( "WARNING: Switching to" + bestSource);
            }

            switchHistory.add("Switched to " + bestSource + " at " + java.time.LocalTime.now().format(java.time.format.DateTimeFormatter.ofPattern("HH:mm:ss")));
            System.out.println("Switch Entry: " + switchHistory.get(switchHistory.size() - 1));
        }
    
    }

    public void saveSwitchHistory() {
        System.out.println("\n ==== Saving Switch History at " + location + "====");
        System.out.println("Connecting to SQL Server ...");
        // Simulate SQL connection and saving data
        System.out.println ("Saved " + switchHistory.size() + " entry to database");
    }

    public void dailySwitchReport () {
        UsageReport report = new UsageReport();
        report.switchReport("Daily Switch Report for " + java.time.LocalDate.now().toString());
    }

    class UsageReport {
        public void switchReport(String title){
            System.out.println("\n ==== " + title + " at " + location + "====");
            System.out.println("Total Switches Made : " + switchHistory.size());
            System.out.println("Cost Savings : " );
            System.out.println("Estimated CO₂ Saved: ");
            System.out.println("Reccomendations: ");   
        }
    }

}
