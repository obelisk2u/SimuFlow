import matplotlib.pyplot as plt
import os
import numpy as np

import numpy as np
import matplotlib.pyplot as plt
import os

def save_velocity_plot(history, grid, step=-1, filename='results/output/velocity.png'):
    u = history[step]["u"]
    v = history[step]["v"]
    X = grid["X"]
    Y = grid["Y"]

    # Compute velocity magnitude
    velocity_mag = np.sqrt(u**2 + v**2)

    plt.figure(figsize=(6, 5))
    contour = plt.contourf(X, Y, velocity_mag, levels=100, cmap='viridis')
    plt.colorbar(contour, label='Velocity magnitude')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Velocity Magnitude Heatmap')
    plt.axis('equal')
    plt.tight_layout()

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename)
    plt.close()


def save_pressure_plot(history, grid, step=-1, filename='results/output/pressure.png'):
    p = history[step]["p"]
    p_normalized = (p - np.min(p)) / (np.max(p) - np.min(p))

    X = grid["X"]
    Y = grid["Y"]

    plt.figure(figsize=(6, 5))
    contour = plt.contourf(X, Y, p_normalized, 50, cmap='coolwarm')
    plt.colorbar(contour, label='Pressure')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Pressure Field')
    plt.axis('equal')
    plt.tight_layout()

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename)
    plt.close()

def save_vorticity_plot(history, grid, step=-1, filename='results/output/vorticity.png'):
    u = history[step]["u"]
    v = history[step]["v"]
    X = grid["X"]
    Y = grid["Y"]
    dx = grid["dx"]
    dy = grid["dy"]

    omega = (np.gradient(v, dx, axis=1) - np.gradient(u, dy, axis=0))

    plt.figure(figsize=(6, 5))
    contour = plt.contourf(X, Y, omega, levels=100, cmap='RdBu_r')
    plt.colorbar(contour, label='Vorticity')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Vorticity Field')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
