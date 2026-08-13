# 🕹️ PERP Architecture Simulations

This directory contains the baseline Python prototypes for the Planetary Energy Routing Protocol (PERP). These scripts demonstrate how our decentralized protocols balance physical energy, digital data workloads, and global land use.

## 🚀 How to Run the Simulations

You do not need to install any external libraries. These scripts run using standard Python 3. 

Open your terminal and run the scripts from the root directory of the repository:

### 1. Federated AI Mesh Balancer (Pillar 1)
Models peer-to-peer node communication, physical space solar (SBSP) routing, and virtual data center workload migration.
```bash
python simulations/perp_mesh_simulation.py
```

### 2. PALO Land Allocator (Pillar 4)
Calculates localized optimization models to transition livestock land into native forests while maintaining global nutritional safety nets.
```bash
python simulations/palo_land_allocator.py
```

## 🛠️ Contributor Roadmap for v0.3
We are actively looking for developers to help expand these prototypes:
* **Pillar 1:** Introduce random network lag and node dropouts to test mesh resiliency.
* **Pillar 4:** Integrate real GIS coordinate data structures using the models in the `/schemas` folder.
