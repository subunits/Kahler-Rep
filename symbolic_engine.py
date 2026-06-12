import sympy as sp

class KahlerAuditor:
    def __init__(self, coordinates, potential):
        self.coords = coordinates
        self.potential = potential
        self.metric = None
        
    def compute_metric_hessian(self):
        self.metric = sp.hessian(self.potential, self.coords)
        return self.metric

    def verify_monge_ampere(self):
        if self.metric is None:
            self.compute_metric_hessian()
        return sp.simplify(self.metric.det())
