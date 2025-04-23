from mpi4py import MPI
from dolfinx import mesh, fem
from dolfinx.fem import FunctionSpace, Constant
from dolfinx.fem.petsc import LinearProblem
import ufl

def run_fenicsx_solver():
    domain = mesh.create_unit_square(MPI.COMM_WORLD, 32, 32)
    V = FunctionSpace(domain, ("CG", 1))
    phi = fem.Function(V)
    v = ufl.TestFunction(V)
    alpha = Constant(domain, 0.1)
    m = Constant(domain, 1.0)
    a = ufl.inner(ufl.grad(phi), ufl.grad(v)) * ufl.dx + m**2 * phi * v * ufl.dx
    L = Constant(domain, 0.0) * v * ufl.dx
    problem = LinearProblem(a, L, bcs=[])
    phi_sol = problem.solve()
    return phi_sol
