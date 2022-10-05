import numpy as np
import matplotlib.pyplot as plt


def create_plot(nsteps, n_output, fig, u, T_cold, T_hot, dt):
	fig_counter = 0

	# Time loop
	for n in range(nsteps):

		# Create figure
		if n in n_output:
			fig_counter += 1
			ax = fig.add_subplot(220 + fig_counter)
			im = ax.imshow(u.copy(), cmap=plt.get_cmap('hot'), vmin=T_cold, vmax=T_hot)  # image for color bar axes
			ax.set_axis_off()
			ax.set_title('{:.1f} ms'.format(n * dt * 1000))

	output_plots(fig, im)


def output_plots(fig, im):
	# Plot output figures
	fig.subplots_adjust(right=0.85)
	cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
	cbar_ax.set_xlabel('$T$ / K', labelpad=20)
	fig.colorbar(im, cax=cbar_ax)
	plt.show()