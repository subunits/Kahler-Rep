import sympy as sp
from core.symbolic_engine import KahlerAuditor
from core.manifolds import get_eguchi_hanson, get_taub_nut

def run_geometric_audit():
    print("💿 OBZEN ENGINE ONLINE // STARTING GEOMETRIC AUDIT...\n")
    
    # Define coordinates and parameters
    r, a, m = sp.symbols('r a m', real=True, positive=True)
    coords = [r]

    # 1. Audit Eguchi-Hanson
    print("=== MONITORING: EGUCHI-HANSON INSTANTON ===")
    eh_pot = get_eguchi_hanson(r, a)
    eh_auditor = KahlerAuditor(coords, eh_pot)
    print("Metric Hessian Component:")
    sp.pprint(eh_auditor.compute_metric_hessian())
    print(f"Monge-Ampere Determinant: {eh_auditor.verify_monge_ampere()}\n")

    # 2. Audit Taub-NUT
    print("=== MONITORING: TAUB-NUT TWISTED GEOMETRY ===")
    tn_pot = get_taub_nut(r, m)
    tn_auditor = KahlerAuditor(coords, tn_pot)
    print("Metric Hessian Component:")
    sp.pprint(tn_auditor.compute_metric_hessian())
    print(f"Monge-Ampere Determinant: {tn_auditor.verify_monge_ampere()}\n")

if __name__ == "__main__":
    run_geometric_audit()
