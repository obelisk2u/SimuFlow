import numpy as np

def initialize_fields(config, grid):
    Nx = grid["Nx"]
    Ny = grid["Ny"]

    u = np.zeros((Ny, Nx))  # x-velocity
    v = np.zeros((Ny, Nx))  # y-velocity
    p = np.zeros((Ny, Nx))  # pressure

    return {"u": u, "v": v, "p": p}
