import hashlib
import uuid
from typing import List, Dict

class MaterialFormula:
    def __init__(self, name: str, category: str, base_chemistry: str, co2_sequestered_per_kg: float):
        self.name = name
        self.category = category                  # e.g., "Concrete", "Polymer", "Steel"
        self.base_chemistry = base_chemistry
        self.co2_sequestered_per_kg = co2_sequestered_per_kg  # Positive values mean it traps carbon
        
        # Public, immutable cryptographic identifier for an un-patentable compound
        self.formula_hash = hashlib.sha256(base_chemistry.encode()).hexdigest()[:12]

class AREMMolecularDatabase:
    """Public index of machine-learning discovered chemical formulas."""
    def __init__(self):
        self.public_registry: Dict[str, MaterialFormula] = {}

    def publish_formula(self, formula: MaterialFormula):
        self.public_registry[formula.formula_hash] = formula
        print(f"🔬 [AREM Registry] Published '{formula.name}' ({formula.category})")
        print(f"  └─ Formula Hash: sha256-{formula.formula_hash} | Net Sequestration: {formula.co2_sequestered_per_kg:+.2f} kg CO2/kg")

class SupplyChainAuditor:
    """AI-driven ledger to track industrial infrastructure projects."""
    def __init__(self, database: AREMMolecularDatabase):
        self.database = database
        self.active_infrastructure: List[Dict] = []

    def audit_building_project(self, project_name: str, formula_hash: str, total_mass_kg: float):
        print(f"\n🏗️ [Supply Chain Audit] Processing procurement for '{project_name}'...")
        
        if formula_hash not in self.database.public_registry:
            print(f"  🚨 WARNING: Material hash sha256-{formula_hash} not found in public database. Defaulting to historical emissions high-risk status.")
            return

        material = self.database.public_registry[formula_hash]
        total_co2_trapped = material.co2_sequestered_per_kg * total_mass_kg
        
        project_record = {
            "project_id": str(uuid.uuid4())[:8],
            "name": project_name,
            "material_used": material.name,
            "net_carbon_impact_kg": -total_co2_trapped # Negative signifies carbon trapped
        }
        
        self.active_infrastructure.append(project_record)
        print(f"  ✅ Audit Complete. Material approved as structural carbon sink.")
        print(f"  └─ Trapped CO2: {total_co2_trapped:,.2f} kg across foundation lifecycle.")

    def generate_global_impact_report(self):
        print("\n==============================================")
        
        total_sunk_carbon = 0.0
        for project in self.active_infrastructure:
            total_sunk_carbon += abs(project["net_carbon_impact_kg"])
            
        print(f"🌍 [AREM Global Balance Ledger]")
        print(f"  * Total Active Infrastructure Sinks Monitored: {len(self.active_infrastructure)}")
        print(f"  * Total Sequestered Carbon Removed from Air: {total_sunk_carbon:,.2f} kg CO2")
        print("==============================================")

# --- Run the Materials Simulation Engine ---
if __name__ == "__main__":
    print("--- Launching Algorithmic Re-Engineering of Materials v0.1 ---")
    
    # 1. Initialize the Open-Source Database
    arem_db = AREMMolecularDatabase()
    
    # 2. Add machine-learning discovered carbon-negative building blocks
    concrete_alt = MaterialFormula(
        name="Bio-Calcified Slag Cement V4",
        category="Concrete",
        base_chemistry="CaCO3 + Al2O3·2SiO2·2H2O + Micro-algal Binder Matrix",
        co2_sequestered_per_kg=0.35 # Traps 0.35 kg of CO2 per kg of concrete cured
    )
    
    steel_alt = MaterialFormula(
        name="Hydrogen-Reduced Bio-Carbon Structural Alloy",
        category="Steel",
        base_chemistry="Fe + Bio-char Charcoal Matrix + Zero-Emission Arc Refinement",
        co2_sequestered_per_kg=0.12
    )
    
    arem_db.publish_formula(concrete_alt)
    arem_db.publish_formula(steel_alt)
    
    # 3. Simulate AI Supply Chain Ledger processing construction demands
    ledger = SupplyChainAuditor(arem_db)
    
    # Audit a large industrial layout deployment
    ledger.audit_building_project(
        project_name="Oceania P2P Laser Transceiver Substation",
        formula_hash=concrete_alt.formula_hash,
        total_mass_kg=500000.0 # 500 Metric Tonnes
    )
    
    ledger.audit_building_project(
        project_name="Americas Microgrid Hub Structural Skeleton",
        formula_hash=steel_alt.formula_hash,
        total_mass_kg=120000.0 # 120 Metric Tonnes
    )
    
    # 4. Generate summary telemetry payload
    ledger.generate_global_impact_report()
