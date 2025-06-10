def apply_boundary_conditions(fields, config):
    u = fields["u"]
    v = fields["v"]
    p = fields["p"]

    Ny, Nx = u.shape
    U_in = config["boundary"].get("inflow_velocity", 1.0)

    # Inflow (left)
    u[:, 0] = U_in
    v[:, 0] = 0

    # Outflow (right)
    u[:, -1] = u[:, -2]
    v[:, -1] = v[:, -2]

    # No-slip walls (top/bottom)
    u[0, :] = 0
    u[-1, :] = 0
    v[0, :] = 0
    v[-1, :] = 0

    # Pressure Neumann
    p[:, 0] = p[:, 1]
    p[:, -1] = p[:, -2]
    p[0, :] = p[1, :]
    p[-1, :] = p[-2, :]

    # Obstacle
    mask = config.get("obstacle", {}).get("mask", None)
    if mask is not None:
        u[mask] = 0
        v[mask] = 0
