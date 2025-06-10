import numpy as np

def initialize_fields(config, grid):
    Nx = grid["Nx"]
    Ny = grid["Ny"]
    U_in = config["boundary"].get("inflow_velocity", 1.0)

    u = np.ones((Ny, Nx)) * U_in
    v = np.zeros((Ny, Nx))
    p = np.zeros((Ny, Nx))
    s = np.zeros((Ny, Nx))  # dye starts at zero

    return {"u": u, "v": v, "p": p, "s": s}

