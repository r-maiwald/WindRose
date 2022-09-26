import matplotlib.pyplot as plt
from matplotlib.scale import FuncScale
import numpy as np


def forward(x):
    return np.sqrt(x)


def backward(x):
    return x * x


class Windrose:
    def __init__(self, r, theta, n_bins_r, n_bins_theta, fig):
        # Init polar ax
        ax = fig.add_subplot(projection="polar")
        func_scale = FuncScale(ax, (forward, backward))
        ax.set_yscale(func_scale)
        ax.set_theta_offset(np.pi/2)
        # ax.set_rlabel_position(180 - 22.5)

        theta_width = 2 * np.pi / n_bins_theta
        theta_mid_points = (np.arange(n_bins_theta) + 0.5) / n_bins_theta * 2 * np.pi

        values = np.zeros((n_bins_theta, n_bins_r))

        for i, theta_mid_point in enumerate(theta_mid_points):
            theta_min = theta_mid_point - theta_width / 2
            theta_max = theta_mid_point + theta_width / 2
            index = (theta >= theta_min) & (theta < theta_max)
            r_hist, r_bin_edges = np.histogram(
                r[index], bins=n_bins_r, range=(r.min(), r.max())
            )
            values[i] = r_hist

        # Scale values to percent
        values = values / len(r) * 100

        bottom = np.zeros(n_bins_theta)
        scaling_factor = 0.9
        for i in range(n_bins_r):
            ax.bar(
                theta_mid_points,
                values[:, i],
                width=theta_width * scaling_factor,
                bottom=bottom,
                label="{:.1f} m/s to {:.1f} m/s".format(r_bin_edges[i], r_bin_edges[i+1]),
            )
            bottom += values[:, i]

        # Fixed formatter (not preferred)
        # ticks = ax.get_yticks()
        # ax.set_yticklabels(["{}%".format(int(i)) for i in ticks])

        # Flexible formatter
        ax.yaxis.set_major_formatter('{x}%')