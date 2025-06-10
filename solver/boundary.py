def apply_boundary_conditions(fields, config, lid_velocity=1.0):
    u = fields["u"]
    v = fields["v"]
    p = fields["p"]

    Ny, Nx = u.shape

    u[:, 0] = 0      # Left
    u[:, -1] = 0     # Right
    u[0, :] = 0      # Bottom
    u[-1, :] = lid_velocity  # Top

    v[:, 0] = 0
    v[:, -1] = 0
    v[0, :] = 0
    v[-1, :] = 0

    p[:, 0] = p[:, 1]
    p[:, -1] = p[:, -2]
    p[0, :] = p[1, :]
    p[-1, :] = p[-2, :]