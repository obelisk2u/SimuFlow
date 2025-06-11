# SimuFlow

**SimuFlow** is a 2D Navier-Stokes solver implemented in Python for simulating incompressible fluid flow around a circular obstacle. The project emphasizes efficient numerical linear algebra for solving the pressure Poisson equation, a computational bottleneck in CFD simulations.

## Matrix Computations

The simulation relies heavily on sparse matrix operations for performance-critical components:

- **Sparse Poisson Solver**: The pressure correction step is formulated as a large sparse linear system, solved using `scipy.sparse.linalg.spsolve` with a precomputed Laplacian matrix.
- **Laplacian Matrix**: The discrete 5-point Laplacian is constructed using Kronecker products of 1D second-derivative matrices in the x and y directions. This results in a large structured sparse matrix with shape `(Nx * Ny, Nx * Ny)`.
- **Matrix-Free Potential**: The implementation is ready to be upgraded to matrix-free CG solvers to further improve performance, reducing memory overhead and enabling better cache utilization.
- **Profiler-Aware Design**: Bottlenecks were identified using line profiling, showing that >95% of runtime was spent in the Poisson solve. This guided a refactor to build the Laplacian once and reuse it.

## Technologies

- Python
- NumPy
- SciPy (sparse matrices, linear solvers)
- Matplotlib (visualization)
- tqdm (progress tracking)

## Performance Considerations

To address the high cost of solving the pressure Poisson equation:

- The sparse Laplacian is constructed once and passed to the solver.
- The solver uses efficient sparse matrix factorization and direct methods.
- The code structure facilitates future extensions to use matrix-free CG, FFT-based solvers, or PETSc for multigrid methods.

## Future Work

- Matrix-free Laplacian-vector product for use in iterative solvers
- OpenMP-parallel C++ backend for pressure solve
- Multigrid preconditioning (via PETSc or Hypre)

## License

MIT License
