import time
import random

class PowerSatellite:
    def __init__(self, name, orbit_period_mins, max_output_mw):
        self.name = name
        self.orbit_period = orbit_period_mins
        self.max_output = max_output_mw
        self.current_position_deg = 0

    def update_position(self, time_step_mins):
        # Update orbital angle (0-360 degrees)
        self.current_position_deg = (self.current_position_deg + (360 / self.orbit_period) * time_step_mins) % 360
        return self.current_position_deg

    def calculate_laser_output(self, atmospheric_density):
        # Simulate baseline generation with dynamic atmospheric attenuation (loss)
        base_generation = self.max_output
        efficiency = 1.0 - (atmospheric_density * 0.15) # Up to 15% atmospheric loss
        return max(0.0, base_generation * efficiency)

class TerrestrialMicrogrid:
    def __init__(self, node_id, local_demand_mw):
        self.node_id = node_id
        self.base_demand = local_demand_mw
        self.battery_storage_mwh = 50.0 # 50 MWh baseline storage capacity
        self.max_battery_capacity = 200.0

    def get_current_demand(self):
        # Add dynamic load fluctuation to human grid usage
        return max(5.0, self.base_demand + random.uniform(-10.0, 10.0))

    def accept_beamed_power(self, power_received_mw):
        current_demand = self.get_current_demand()
        net_power = power_received_mw - current_demand
       
        print(f"[{self.node_id}] Grid Demand: {current_demand:.2f} MW | Beamed Inbound: {power_received_mw:.2f} MW")
       
        if net_power > 0:
            # Route excess power to localized storage banks
            stored = min(net_power, self.max_battery_capacity - self.battery_storage_mwh)
            self.battery_storage_mwh += stored
            print(f"[{self.node_id}] Grid surplus! Routed {stored:.2f} MW to local battery banks. Storage: {self.battery_storage_mwh:.2f} MWh")
        else:
            # Draw from storage if beamed power doesn't cover local demand
            deficit = abs(net_power)
            drawn = min(deficit, self.battery_storage_mwh)
            self.battery_storage_mwh -= drawn
            print(f"[{self.node_id}] Deficit met. Drawn {drawn:.2f} MW from local storage. Remaining Storage: {self.battery_storage_mwh:.2f} MWh")

# Initialize PERP Pillar 1 Simulation Network
satellite_node = PowerSatellite("PERP-Sat-Alpha", orbit_period_mins=90, max_output_mw=100.0)
local_grid = TerrestrialMicrogrid("NZ-Whanganui-Microgrid-01", local_demand_mw=45.0)

print(f"--- Launching PERP Pillar 1 Simulation: {satellite_node.name} Handoff System ---")

# Run 5 iterations of simulated orbital handoffs
for minute in range(0, 25, 5):
    print(f"\n[Timestamp: T+{minute} mins]")
   
    # Update satellite telemetry
    sat_pos = satellite_node.update_position(5)
    print(f"[{satellite_node.name}] Current Orbital Telemetry: {sat_pos:.1f}°")
   
    # Check line-of-sight window (simulate beacon lock between 0° and 180° horizon visibility)
    if 0 <= sat_pos <= 180:
        # Simulate varying weather conditions affecting atmospheric clarity
        weather_factor = random.uniform(0.1, 0.8)
        beamed_power = satellite_node.calculate_laser_output(weather_factor)
       
        # Route beamed energy directly to the terrestrial grid controller
        local_grid.accept_beamed_power(beamed_power)
    else:
        print(f"[{satellite_node.name}] Orbital telemetry out of horizon bounds. Maintaining passive solar accumulation.")
        local_grid.accept_beamed_power(0.0)
       
    time.sleep(1)

print("\n--- Simulation step complete. Network operating within safe boundaries. ---")
