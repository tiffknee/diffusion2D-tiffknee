"""
Solving the two-dimensional diffusion equation

Example acquired from https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/
"""

import numpy as np
import matplotlib.pyplot as plt
import output_plots

def solve():

    # plate size, mm
    w = h = 10.
    # intervals in x-, y- directions, mm
    dx = dy = 0.3
    # Thermal diffusivity of steel, mm^2/s
    D = 12.

    # Initial cold temperature of square domain
    T_cold = 300

    # Initial hot temperature of circular disc at the center
    T_hot = 700

    # Number of discrete mesh points in X and Y directions
    nx, ny = int(w / dx), int(h / dy)

    # Computing a stable time step
    dx2, dy2 = dx * dx, dy * dy
    dt = dx2 * dy2 / (2 * D * (dx2 + dy2))

    print("dt = {}".format(dt))

    u0 = T_cold * np.ones((nx, ny))
    u = u0.copy()

    # Initial conditions - circle of radius r centred at (cx,cy) (mm)
    r, cx, cy = 2, 5, 5
    r2 = r ** 2
    for i in range(nx):
        for j in range(ny):
            p2 = (i * dx - cx) ** 2 + (j * dy - cy) ** 2
            if p2 < r2:
                u0[i, j] = T_hot


    def do_timestep(u_nm1, u, D, dt, dx2, dy2):
        # Propagate with forward-difference in time, central-difference in space
        u[1:-1, 1:-1] = u_nm1[1:-1, 1:-1] + D * dt * (
                (u_nm1[2:, 1:-1] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[:-2, 1:-1]) / dx2
                + (u_nm1[1:-1, 2:] - 2 * u_nm1[1:-1, 1:-1] + u_nm1[1:-1, :-2]) / dy2)

        u_nm1 = u.copy()
        return u_nm1, u


    # Number of timesteps
    nsteps = 101
    # Output 4 figures at these timesteps
    n_output = [0, 10, 50, 100]

    fig = plt.figure()

    # Time loop
    for n in range(nsteps):
        u0, u = do_timestep(u0, u, D, dt, dx2, dy2)

    output_plots.create_plot(nsteps, n_output, fig, u, T_cold, T_hot, dt)

