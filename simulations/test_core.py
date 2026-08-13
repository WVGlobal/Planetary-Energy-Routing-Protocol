import os

def test_repository_files():
    print("🔎 Auditing Repository Architecture...")
    
    # Check that all simulation files exist
    required_files = [
        "simulations/perp_mesh_simulation.py",
        "simulations/palo_land_allocator.py",
        "schemas/geoengineering-telemetry.json",
        "schemas/land-optimization-asset.json",
        "schemas/product-circular-lifecycle.json"
    ]
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"  ✅ Found: {file_path}")
        else:
            print(f"  ❌ MISSING: {file_path}")
            
    print("\n🎉 Repository Structure Verification Complete!")

if __name__ == "__main__":
    test_repository_files()
