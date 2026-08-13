import uuid
from typing import List, Dict

class ManufacturedProduct:
    def __init__(self, name: str, metal_kg: float, polymer_kg: float, target_factory_id: str):
        self.product_uid = str(uuid.uuid4())[:8]
        self.name = name
        self.metal_kg = metal_kg
        self.polymer_kg = polymer_kg
        self.target_factory_id = target_factory_id # Where this material needs to go next

class AutomatedReclamationCenter:
    def __init__(self, name: str, latitude: float, longitude: float):
        self.center_id = str(uuid.uuid4())[:8]
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.landfill_inventory = {
            "reclaimed_metals_kg": 0.0,
            "reclaimed_polymers_kg": 0.0
        }

    def mine_landfill(self, expired_batch: List[ManufacturedProduct]):
        """Simulates autonomous robotic sorting networks processing expired items."""
        print(f"\n🤖 [{self.name}] Autonomous Landfill Mining sorting sequence active...")
        for product in expired_batch:
            self.landfill_inventory["reclaimed_metals_kg"] += product.metal_kg
            self.landfill_inventory["reclaimed_polymers_kg"] += product.polymer_kg
            print(f"  📦 Disassembled product {product.product_uid} ({product.name}) -> Extracted {product.metal_kg}kg Metal, {product.polymer_kg}kg Polymers.")

class ZeroCarbonProductionFacility:
    def __init__(self, name: str, latitude: float, longitude: float, metal_demand_kg: float):
        self.facility_id = str(uuid.uuid4())[:8]
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.metal_demand_kg = metal_demand_kg

class AlgorithmicCircularMarketplace:
    """The algorithm balancing manufacturing demands with recycled material availability."""
    
    @staticmethod
    def calculate_distance(lat1, lon1, lat2, lon2) -> float:
        """Simple coordinate distance calculation to prioritize localized shipping."""
        return ((lat1 - lat2)**2 + (lat1 - lat2)**2)**0.5

    def allocate_materials(self, centers: List[AutomatedReclamationCenter], factories: List[ZeroCarbonProductionFacility]):
        print("\n🔄 [ACE Marketplace] Commencing Dynamic Material Reallocation Loops...")
        
        for factory in factories:
            if factory.metal_demand_kg <= 0:
                continue
                
            print(f"\n🏭 Factory [{factory.name}] requires {factory.metal_demand_kg:.2f}kg of Reclaimed Metal.")
            
            # Find the closest reclamation center with inventory
            best_center = None
            shortest_distance = float('inf')
            
            for center in centers:
                if center.landfill_inventory["reclaimed_metals_kg"] > 0:
                    dist = self.calculate_distance(factory.latitude, factory.longitude, center.latitude, center.longitude)
                    if dist < shortest_distance:
                        shortest_distance = dist
                        best_center = center
            
            if best_center:
                available_metal = best_center.landfill_inventory["reclaimed_metals_kg"]
                allocated_metal = min(available_metal, factory.metal_demand_kg)
                
                # Execute algorithmic routing
                best_center.landfill_inventory["reclaimed_metals_kg"] -= allocated_metal
                factory.metal_demand_kg -= allocated_metal
                
                print(f"  🚛 Localized Routing: Shipped {allocated_metal:.2f}kg of metal from [{best_center.name}] to [{factory.name}] (Distance units: {shortest_distance:.2f})")
            else:
                print(f"  ⚠️ No regional recycled metal available to meet factory demand.")

# --- Run the Circular Economy Simulation ---
if __name__ == "__main__":
    print("--- Launching Automated Circular Economy Framework v0.1 ---")
    
    # 1. Create historical product waste profiles matching our data schemas
    waste_stream = [
        ManufacturedProduct("Expired Solar Frame", metal_kg=45.0, polymer_kg=12.0, target_factory_id="factory-1"),
        ManufacturedProduct("Decommissioned Smart Device Batches", metal_kg=80.0, polymer_kg=40.0, target_factory_id="factory-1"),
    ]
    
    # 2. Setup regional infrastructure components
    reclaim_center_north = AutomatedReclamationCenter("North Regional Reclaim Hub", latitude=45.0, longitude=-90.0)
    factory_chicago = ZeroCarbonProductionFacility("Chicago Green Infrastructure Plant", latitude=41.8, longitude=-87.6, metal_demand_kg=100.0)
    
    # 3. Step One: Run Robotic Mining
    reclaim_center_north.mine_landfill(waste_stream)
    
    # 4. Step Two: Trigger Algorithmic Resource Reallocation
    marketplace = AlgorithmicCircularMarketplace()
    marketplace.allocate_materials(centers=[reclaim_center_north], factories=[factory_chicago])
    
    print("\n--- Post-Loop Logistics Status ---")
    print(f"  * {reclaim_center_north.name} Remaining Metals: {reclaim_center_north.landfill_inventory['reclaimed_metals_kg']:.2f}kg")
    print(f"  * {factory_chicago.name} Unmet Metal Demand: {factory_chicago.metal_demand_kg:.2f}kg")
