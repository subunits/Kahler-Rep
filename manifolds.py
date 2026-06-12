import sympy as sp

def get_eguchi_hanson(r, a):
    """Returns the classic Eguchi-Hanson potential function."""
    return sp.sqrt(r**4 + a**4) + a**2 * sp.log(r**2) - a**2 * sp.log(a**2 + sp.sqrt(r**4 + a**4))

def get_taub_nut(r, m):
    """
    Returns the Taub-NUT potential profile.
    m represents the NUT variable scale.
    """
    return (r**2 / (4 * m)) + m * sp.log(r**2)
