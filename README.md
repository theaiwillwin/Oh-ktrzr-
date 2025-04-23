# Scalar Field Simulations

This repository contains four simulation frameworks for scalar field evolution in 2D using:

1. Finite-Difference (SciPy)
2. Spectral Method (NumPy FFT)
3. Finite-Element (FEniCSx)
4. COMSOL (Python API via mph)

## Usage

Each Python script defines a run_*_solver() function that you can run or modify for experiments.

## Dependencies

- Python 3.10+
- NumPy, SciPy, matplotlib
- FEniCSx (for FEM)
- COMSOL + mph (for COMSOL automation)
