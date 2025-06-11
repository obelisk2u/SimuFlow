from scipy.sparse import diags, kron, eye, csr_matrix
from scipy.sparse.linalg import spsolve

def build_laplacian(Nx, Ny, dx, dy):
    # 1D second derivative matrices
    Dxx = diags([1, -2, 1], [-1, 0, 1], shape=(Nx, Nx)) / dx**2
    Dyy = diags([1, -2, 1], [-1, 0, 1], shape=(Ny, Ny)) / dy**2

    # Apply zero Neumann BCs by modifying first and last rows
    Dxx = Dxx.tolil()
    Dyy = Dyy.tolil()
    Dxx[0, 0:2] = [-2, 2]
    Dxx[-1, -2:] = [2, -2]
    Dyy[0, 0:2] = [-2, 2]
    Dyy[-1, -2:] = [2, -2]

    Dxx = Dxx.tocsr()
    Dyy = Dyy.tocsr()

    # 2D Laplacian: kron sums
    L = kron(eye(Ny), Dxx) + kron(Dyy, eye(Nx))

    return csr_matrix(L)


def pressure_poisson_sparse(b, A):
    b_flat = b.ravel()
    p_flat = spsolve(A, b_flat)
    return p_flat.reshape(b.shape)
