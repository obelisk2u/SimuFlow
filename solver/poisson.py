import numpy as np

def pressure_poisson(p, dx, dy, b, nit=50):
    pn = p.copy()
    for _ in range(nit):
        pn[1:-1, 1:-1] = (
            ((pn[1:-1, 2:] + pn[1:-1, :-2]) * dy**2 +
             (pn[2:, 1:-1] + pn[:-2, 1:-1]) * dx**2 -
             b[1:-1, 1:-1] * dx**2 * dy**2)
            / (2 * (dx**2 + dy**2))
        )

        # Enforce boundary conditions (Neumann)
        pn[:, 0] = pn[:, 1]
        pn[:, -1] = pn[:, -2]
        pn[0, :] = pn[1, :]
        pn[-1, :] = pn[-2, :]

    return pn
