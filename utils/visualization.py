import matplotlib.pyplot as plt
import os
import numpy as np

def save_velocity_plot(history, grid, step=-1, filename='results/output/velocity.png'):
    u = history[step]["u"]
    v = history[step]["v"]
    X = grid["X"]
    Y = grid["Y"]

    plt.figure(figsize=(6, 5))

    # Downsample for quiver clarity (adjust step if needed)
    step_size = max(1, X.shape[0] // 30)
    Xs = X[::step_size, ::step_size]
    Ys = Y[::step_size, ::step_size]
    us = u[::step_size, ::step_size]
    vs = v[::step_size, ::step_size]

    plt.quiver(Xs, Ys, us, vs, scale=5, pivot='mid', color='blue')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Velocity field')
    plt.axis('equal')
    plt.tight_layout()
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