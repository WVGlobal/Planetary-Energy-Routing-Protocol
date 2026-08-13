import numpy as np

def run_palo_optimization():
    print(f"--- PALO Land Optimization Engine Launching ---")
    
    # Zone data: [Available Land (km2), Protein Output (tonnes), Emissions Index, Biodiversity Index]
    zones = {
        "Zone_A_North_America": {"land": 5000, "protein": 2000, "emissions": 45, "biodiversity": 0.8},
        "Zone_B_South_America": {"land": 8000, "protein": 4000, "emissions": 65, "biodiversity": 0.95},
        "Zone_C_Europe":        {"land": 3000, "protein": 1500, "emissions": 30, "biodiversity": 0.6}
    }
    
    global_demand = 4000  # Total tonnes of protein required globally
    alpha = 50           # Carbon sequestration constant per km2 of forest
    beta = 0.75          # Maximum land transition allowed (75% limit)
    
    print(f"Global Nutritional Baseline Target: {global_demand} Tonnes")
    print("Evaluating Regional Sequestration Potentials...")
    
    # Calculate Optimization Scores (Emissions avoidance + Reforestation potential)
    rankings = []
    for name, data in zones.items():
        score = (data["land"] * data["biodiversity"] * alpha) + (data["protein"] * data["emissions"])
        rankings.append((name, score, data))
    
    # Sort zones by highest mitigation impact first
    rankings.sort(key=lambda x: x[1], reverse=True)
    
    allocated_protein = sum(z["protein"] for z in zones.values())
    total_freed_land = 0
    
    print("\nExecuting Targeted Transitions:")
    for name, score, data in rankings:
        if allocated_protein > global_demand:
            # Calculate how much traditional capacity we can safely transition
            surplus = allocated_protein - global_demand
            max_transition_by_protein = surplus / data["protein"]
            
            # Bound transition by safety buffer beta
            transition_pct = min(max_transition_by_protein, beta)
            
            freed_km2 = data["land"] * transition_pct
            allocated_protein -= (data["protein"] * transition_pct)
            total_freed_land += freed_km2
            
            print(f"  🌱 Transitioned {transition_pct*100:.1f}% of {name} | Freed: {freed_km2:.2f} km2 for Drone Reforestation")
        else:
            print(f"  🛑 Safe nutritional limit reached. Halting transition on {name}.")
            
    print(f"\nFinal Optimization State:")
    print(f"  Total Freed Planetary Surface Area: {total_freed_land:.2f} km2")
    print(f"  Remaining Traditional Supply Safety Net: {allocated_protein:.2f} Tonnes")

if __name__ == "__main__":
    run_palo_optimization()
