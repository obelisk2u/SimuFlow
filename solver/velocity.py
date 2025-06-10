import numpy as np

def update_velocity(u, v, p, un, vn, rho, nu, dt, dx, dy):
    # Update u-component of velocity
    u[1:-1, 1:-1] = (
        un[1:-1, 1:-1]
        - dt / rho * (p[1:-1, 2:] - p[1:-1, :-2]) / (2 * dx)
        + nu * dt * (
            (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, :-2]) / dx**2 +
            (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[:-2, 1:-1]) / dy**2
        )
    )

    # Update v-component of velocity
    v[1:-1, 1:-1] = (
        vn[1:-1, 1:-1]
        - dt / rho * (p[2:, 1:-1] - p[:-2, 1:-1]) / (2 * dy)
        + nu * dt * (
            (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, :-2]) / dx**2 +
            (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[:-2, 1:-1]) / dy**2
        )
    )

    return u, v
