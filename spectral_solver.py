import numpy as np
import matplotlib.pyplot as plt

def run_spectral_solver(N=256, L=10.0, s=0.75):
    x = np.linspace(0, L, N, endpoint=False)
    dx = L / N
    X, Y = np.meshgrid(x, x, indexing='ij')

    kx = 2 * np.pi * np.fft.fftfreq(N, d=dx)
    KX, KY = np.meshgrid(kx, kx, indexing='ij')
    K2 = KX**2 + KY**2
    frac_multiplier = K2**s

    phi = np.exp(-((X - L / 2)**2 + (Y - L / 2)**2))
    phi_hat = np.fft.fft2(phi)
    frac_hat = -frac_multiplier * phi_hat
    phi_frac = np.real(np.fft.ifft2(frac_hat))

    plt.imshow(phi_frac, origin='lower', extent=[0, L, 0, L])
    plt.title(f'Fractional Laplacian of Gaussian (s = {s:.2f})')
    plt.colorbar()
    plt.show()
