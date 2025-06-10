def apply_boundary_conditions(fields, config):
    u = fields["u"]
    v = fields["v"]
    p = fields["p"]

    # Inflow on the left (Dirichlet)
    U_in = config["boundary"].get("inflow_velocity", 1.0)
    u[:, 0] = U_in
    v[:, 0] = 0

    # Outflow on the right (Neumann)
    u[:, -1] = u[:, -2]
    v[:, -1] = v[:, -2]

    # No-slip top and bottom walls
    u[0, :] = 0
    u[-1, :] = 0
    v[0, :] = 0
    v[-1, :] = 0

    # Pressure Neumann everywhere
    p[:, 0] = p[:, 1]       # left
    p[:, -1] = p[:, -2]     # right
    p[0, :] = p[1, :]       # bottom
    p[-1, :] = p[-2, :]     # top

    mask = config.get("obstacle", {}).get("mask", None)
    if mask is not None:
        u[mask] = 0
        v[mask] = 0
