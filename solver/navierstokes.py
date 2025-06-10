import numpy as np
from solver.poisson import pressure_poisson
from solver.boundary import apply_boundary_conditions
from solver.velocity import update_velocity
from tqdm import trange

def run_simulation(config, grid, fields):
    u = fields["u"]
    v = fields["v"]
    p = fields["p"]

    dx = grid["dx"]
    dy = grid["dy"]
    Nx = grid["Nx"]
    Ny = grid["Ny"]

    rho = config["physics"]["density"]
    nu = config["physics"]["viscosity"]
    dt = config["solver"]["dt"]
    n_steps = config["solver"]["n_steps"]

    b = np.zeros((Ny, Nx))
    history = []

    for step in trange(n_steps, desc="Simulating", unit="step"):
        un = u.copy()
        vn = v.copy()

        # Compute divergence-based source term b
        b[1:-1, 1:-1] = rho * (1 / dt) * (
            (un[1:-1, 2:] - un[1:-1, :-2]) / (2 * dx) +
            (vn[2:, 1:-1] - vn[:-2, 1:-1]) / (2 * dy)
        )

        p = pressure_poisson(p, dx, dy, b)

        # Update velocity field using pressure gradient
        u, v = update_velocity(u, v, p, un, vn, rho, nu, dt, dx, dy)

        # Apply boundary conditions
        fields["u"] = u
        fields["v"] = v
        fields["p"] = p
        apply_boundary_conditions(fields, config)

        # Store a copy of the current field state
        history.append({k: v.copy() for k, v in fields.items()})

    return history
