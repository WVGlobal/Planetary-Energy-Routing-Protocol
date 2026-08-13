import subprocess
import sys
import os

def run_simulation_test(script_name: str) -> bool:
    path = os.path.join("simulations", script_name)
    print(f"🧪 Testing: {path}...")
    try:
        # Runs the script and captures output
        result = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print(f"  ✅ {script_name} passed successfully.")
            return True
        else:
            print(f"  ❌ {script_name} failed with exit code {result.returncode}.")
            print(f"  Error details:\n{result.stderr}")
            return False
    except Exception as e:
        print(f"  ❌ Failed to execute {script_name}: {str(e)}")
        return False

if __name__ == "__main__":
    print("==============================================")
    print("🌍 PERP Simulation Stack: Automated Integrity Audit")
    print("==============================================\n")
    
    scripts_to_test = [
        "perp_mesh_simulation.py",
        "palo_land_allocator.py",
        "ace_circular_marketplace.py"
    ]
    
    all_passed = True
    for script in scripts_to_test:
        if not run_simulation_test(script):
            all_passed = False
        print("-" * 46)
        
    if all_passed:
        print("\n🎉 SUCCESS: All planetary simulation cores are functional!")
        sys.exit(0)
    else:
        print("\n🚨 FAILURE: One or more simulation engines returned errors.")
        sys.exit(1)
