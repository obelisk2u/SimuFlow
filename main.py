from mesh.grid import create_grid
from physics.initial_conditions import initialize_fields
from solver.navierstokes import run_simulation
from utils.visualization import save_velocity_plot, save_pressure_plot
import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

grid = create_grid(config)
fields = initialize_fields(config, grid)

history = run_simulation(config, grid, fields)

save_velocity_plot(history, grid)
save_pressure_plot(history, grid)
