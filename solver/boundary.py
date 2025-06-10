import numpy as np

def apply_boundary_conditions(fields, config, lid_velocity=1.0):
    u = fields["u"]
    v = fields["v"]
    p = fields["p"]

    Ny, Nx = u.shape

    # Velocity boundary conditions (u, v)

    # Left wall (x = 0): u = 0, v = 0
    u[:, 0] = 0
    v[:, 0] = 0

    # Right wall (x = Lx): u = 0, v = 0
    u[:, -1] = 0
    v[:, -1] = 0

    # Bottom wall (y = 0): u = 0, v = 0
    u[0, :] = 0
    v[0, :] = 0

    # Top wall (y = Ly): u = lid_velocity, v = 0
    u[-1, :] = lid_velocity
    v[-1, :] = 0

    # Pressure boundary condition (Neumann: dp/dn = 0)
    p[:, 0] = p[:, 1]         # Left
    p[:, -1] = p[:, -2]       # Right
    p[0, :] = p[1, :]         # Bottom
    p[-1, :] = p[-2, :]       # Top

    fields["u"] = u
    fields["v"] = v
    fields["p"] = p
