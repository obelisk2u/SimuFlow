import numpy as np

def create_grid(config):
    Nx = config["domain"]["Nx"]
    Ny = config["domain"]["Ny"]
    Lx = config["domain"]["Lx"]
    Ly = config["domain"]["Ly"]

    dx = Lx / (Nx - 1)
    dy = Ly / (Ny - 1)

    x = np.linspace(0, Lx, Nx)
    y = np.linspace(0, Ly, Ny)
    X, Y = np.meshgrid(x, y)

    return {"X": X, "Y": Y, "dx": dx, "dy": dy, "Nx": Nx, "Ny": Ny}
