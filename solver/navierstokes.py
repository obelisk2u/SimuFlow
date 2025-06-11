import numpy as np
from tqdm import trange
from solver.poisson import pressure_poisson
from solver.velocity import update_velocity
from solver.boundary import apply_boundary_conditions
from solver.poisson_sparse import build_laplacian, pressure_poisson_sparse


def run_simulation(config, grid, fields):
    u = fields["u"]
    v = fields["v"]
    p = fields["p"]
    s = fields["s"]

    dx = grid["dx"]
    dy = grid["dy"]
    Nx = grid["Nx"]
    Ny = grid["Ny"]

    A = build_laplacian(Nx, Ny, dx, dy)


    rho = config["physics"]["density"]
    nu = config["physics"]["viscosity"]
    dt = config["solver"]["dt"]
    n_steps = config["solver"]["n_steps"]
    D = config.get("scalar", {}).get("diffusivity", 0.0001)

    b = np.zeros((Ny, Nx))
    history = []

    for step in trange(n_steps, desc="Simulating", unit="step"):
        un = u.copy()
        vn = v.copy()
        sn = s.copy()

        # Compute source term for pressure Poisson equation
        b[1:-1, 1:-1] = rho * (1 / dt) * (
            (un[1:-1, 2:] - un[1:-1, :-2]) / (2 * dx) +
            (vn[2:, 1:-1] - vn[:-2, 1:-1]) / (2 * dy)
        )

        # Solve pressure Poisson equation
        p = pressure_poisson_sparse(b, A)

        # Update velocity
        u, v = update_velocity(u, v, p, un, vn, rho, nu, dt, dx, dy)

        # Apply boundary conditions
        fields["u"] = u
        fields["v"] = v
        fields["p"] = p
        apply_boundary_conditions(fields, config)

        # Update scalar field (advection-diffusion)
        dsdx = (sn[:, 2:] - sn[:, :-2]) / (2 * dx)
        dsdy = (sn[2:, :] - sn[:-2, :]) / (2 * dy)
        dsdx = np.pad(dsdx, ((0, 0), (1, 1)), mode='edge')
        dsdy = np.pad(dsdy, ((1, 1), (0, 0)), mode='edge')

        advect = -u * dsdx - v * dsdy

        # x-direction Laplacian: (Ny, Nx - 2)
        lap_x = (sn[:, 2:] - 2 * sn[:, 1:-1] + sn[:, :-2]) / dx**2
        lap_x = np.pad(lap_x, ((0, 0), (1, 1)), mode='edge')

        # y-direction Laplacian: (Ny - 2, Nx)
        lap_y = (sn[2:, :] - 2 * sn[1:-1, :] + sn[:-2, :]) / dy**2
        lap_y = np.pad(lap_y, ((1, 1), (0, 0)), mode='edge')

        laplace_s = lap_x + lap_y

        # Advection-diffusion step
        s += dt * (advect + D * laplace_s)
        y = np.linspace(0, 1, Ny)
        gaussian = np.exp(-((y - 0.5)**2) / 0.001)  # narrower = sharper stream
        s[:, 0] = gaussian


        # Clipping for sanity
        s = np.clip(s, 0, 3.0)

        # Enforce solid obstacle (no dye inside)
        s[config["obstacle"]["mask"]] = 0.0

        fields["s"] = s
        fields["scalar"] = s

        # Diagnostics
        velocity_mag = np.sqrt(u**2 + v**2)
        omega = np.gradient(v, dx, axis=1) - np.gradient(u, dy, axis=0)
        fields["velocity_mag"] = velocity_mag
        fields["omega"] = omega

        # Store snapshot
        history.append({k: v.copy() for k, v in fields.items()})

    return history
