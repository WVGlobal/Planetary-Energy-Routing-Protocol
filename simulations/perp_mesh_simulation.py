import uuid
from typing import List, Dict

class PERPFederatedNode:
    def __init__(self, name: str, terrestrial_gen: float, sbsp_gen: float, base_load: float, compute_load_mw: float):
        self.node_id = str(uuid.uuid4())[:8]
        self.name = name
        
        # --- Energy Assets ---
        self.terrestrial_gen = terrestrial_gen  # MW
        self.sbsp_gen = sbsp_gen                # MW (Space-Based Solar Power)
        self.base_load = base_load              # MW (Local Critical Infrastructure)
        self.compute_load_mw = compute_load_mw  # MW (Flexible Data Center Workloads)
        
        # --- Federated Network Connectivity ---
        self.peers: List['PERPFederatedNode'] = []
        
    @property
    def total_generation(self) -> float:
        return self.terrestrial_gen + self.sbsp_gen

    @property
    def total_demand(self) -> float:
        return self.base_load + self.compute_load_mw

    @property
    def net_balance(self) -> float:
        return self.total_generation - self.total_demand

    def connect_peer(self, peer_node: 'PERPFederatedNode'):
        if peer_node not in self.peers:
            self.peers.append(peer_node)
            peer_node.peers.append(self)  # P2P High-frequency space laser link

    def verify_tri_key_lock(self) -> bool:
        """Consensus security mechanism check before global routing."""
        key_1_human_coalition = True
        key_2_ai_mesh_vote = True
        key_3_immutable_directive = True # Always guarantee baseline survival power
        return key_1_human_coalition and key_2_ai_mesh_vote and key_3_immutable_directive

    def request_mesh_assistance(self, required_mw: float):
        """Asks connected peers for help using the two core protocol strategies."""
        print(f"\n🛰️ [{self.name}] Deficit detected! Requesting {abs(required_mw):.2f} MW from mesh...")
        
        # Strategy A: Look for Physical Space Solar (SBSP) to route over
        for peer in self.peers:
            if self.net_balance >= -0.1: 
                break # Grid balanced
                
            if peer.net_balance > 0 and peer.sbsp_gen > 0:
                # Find out how much space solar the peer can spare safely
                sharable_sbsp = min(peer.sbsp_gen, peer.net_balance, abs(self.net_balance))
                
                # Execute physical energy rerouting
                peer.sbsp_gen -= sharable_sbsp
                self.sbsp_gen += sharable_sbsp
                print(f"  ⚡ [Strategy A] Routed {sharable_sbsp:.2f} MW of SBSP from [{peer.name}] to [{self.name}]")

        # Strategy B: If still short, try to offload heavy digital compute work to surplus peers
        for peer in self.peers:
            if self.net_balance >= -0.1:
                break # Grid balanced
                
            if peer.net_balance > 0 and self.compute_load_mw > 0:
                # Find out how much computing work can migrate over the internet
                shiftable_compute = min(self.compute_load_mw, peer.net_balance, abs(self.net_balance))
                
                # Execute virtual balancing
                self.compute_load_mw -= shiftable_compute
                peer.compute_load_mw += shiftable_compute
                print(f"  🌐 [Strategy B] Migrated {shiftable_compute:.2f} MW of data center load from [{self.name}] to [{peer.name}]")

    def run_agent_loop(self):
        """The main autonomous cycle executed by each node's local AI engine."""
        balance = self.net_balance
        if balance >= 0:
            print(f"✅ [{self.name}] Grid is stable ({balance:+.2f} MW). Supporting mesh.")
            return

        # Security check before touching the planetary energy pool
        if not self.verify_tri_key_lock():
            print(f"🚨 [{self.name}] SECURITY ALERT: Tri-Key Lock failed! Local air-gapped breakers dropped.")
            return

        # Negotiate balance
        self.request_mesh_assistance(balance)

# --- Run the Combined Network Simulation ---
if __name__ == "__main__":
    print("--- Launching Integrated PERP AGMS Framework v0.2 ---")
    
    # Setup 3 regional nodes in different situations
    oceania = PERPFederatedNode(name="Oceania Hub", terrestrial_gen=300, sbsp_gen=400, base_load=200, compute_load_mw=100)
    americas = PERPFederatedNode(name="Americas Hub", terrestrial_gen=100, sbsp_gen=50, base_load=500, compute_load_mw=200)
    europe = PERPFederatedNode(name="Europe Hub", terrestrial_gen=250, sbsp_gen=50, base_load=200, compute_load_mw=50)

    # Connect nodes into the global P2P laser mesh
    oceania.connect_peer(americas)
    oceania.connect_peer(europe)
    americas.connect_peer(europe)

    print("\n--- Initial Grid Conditions ---")
    for node in [oceania, americas, europe]:
        print(f"  * {node.name} Net: {node.net_balance:+.2f} MW")

    print("\n--- Decentralized AI Orchestration Commencing ---")
    for node in [oceania, americas, europe]:
        node.run_agent_loop()

    print("\n--- Post-Routing Grid Status ---")
    for node in [oceania, americas, europe]:
        status = "STABLE ✅" if abs(node.net_balance) <= 0.1 else "UNBALANCED ⚠️"
        print(f"  * {node.name} Net: {node.net_balance:+.2f} MW | Status: {status}")
