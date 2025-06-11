from mesh.grid import create_grid
from physics.initial_conditions import initialize_fields
from solver.navierstokes import run_simulation
from utils.visualization import save_velocity_plot, save_pressure_plot,save_vorticity_plot, save_scalar_plot
from solver.poisson_sparse import build_laplacian
import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

grid = create_grid(config)

X = grid["X"]
Y = grid["Y"]
Lx = config["domain"]["Lx"]
Ly = config["domain"]["Ly"]

cx = Lx / 2
cy = Ly / 2
r = 0.1

mask = (X - cx)**2 + (Y - cy)**2 < r**2

config["obstacle"] = {
    "cx": cx,
    "cy": cy,
    "radius": r,
    "mask": mask
}

fields = initialize_fields(config, grid)


A = build_laplacian(grid["Nx"], grid["Ny"], grid["dx"], grid["dy"])
history = run_simulation(config, grid, fields, A)
save_velocity_plot(history, grid)
save_pressure_plot(history, grid)
save_vorticity_plot(history, grid)
save_scalar_plot(history, grid)