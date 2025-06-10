import matplotlib.pyplot as plt

def save_plot(history, grid, step=-1, filename='results/output/velocity.png'):
    u = history[step]["u"]
    v = history[step]["v"]
    X = grid["X"]
    Y = grid["Y"]

    plt.figure(figsize=(6, 5))
    plt.quiver(X, Y, u, v, scale=2, pivot='mid')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Velocity field')
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()
