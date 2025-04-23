import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

def run_fd_solver(nx=200, ny=200, Nt=500, dt=0.01, alpha=0.1, m=1.0, s=0.5):
    dx = dy = 1.0
    phi = np.zeros((nx, ny))
    phi_prev = np.zeros_like(phi)
    source = np.zeros_like(phi)

    kx = np.fft.fftfreq(nx, dx) * 2 * np.pi
    ky = np.fft.fftfreq(ny, dy) * 2 * np.pi
    k2 = kx[:, None]**2 + ky[None, :]**2
    frac_op = k2**s

    for _ in range(Nt):
        phi_k = np.fft.fft2(phi)
        frac_term = np.real(np.fft.ifft2(frac_op * phi_k))
        diff_term = ndimage.laplace(phi, mode='wrap')
        phi_next = 2 * phi - phi_prev + dt**2 * (alpha * frac_term - diff_term + source - m**2 * phi)
        phi_prev, phi = phi, phi_next

    plt.imshow(phi, origin='lower')
    plt.colorbar()
    plt.title('Scalar field at final time')
    plt.show()
