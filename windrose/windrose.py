import matplotlib.pyplot as plt
from matplotlib.scale import FuncScale
import numpy as np


def forward(x):
    return np.sqrt(x)


def backward(x):
    return x * x


class Windrose:
    def __init__(self, r, theta, n_bins_r, n_bins_theta, fig=None, subplot_id=None):
        """
        Creates a windrose plot.

        Parameters
        ----------
        r : array-like
            The velocity or scalar value.
        theta : array-like
            The angle for the scalar value in radians.
        n_bins_r : int
            The number of bins for the scalar value.
        n_bins_theta : int
            The number of bins for the angle.
        fig : figure
            The matplotlib figure in which the rose should be plotted.
        subplot_id : int, optional
            The id of the subplot in which the ax should be plotted, by default None
        """
        # Init polar ax
        if fig is None:
            fig = plt.figure()
        if subplot_id is None:
            ax = fig.add_subplot(projection="polar")
        else:
            ax = fig.add_subplot(subplot_id, projection="polar")
        func_scale = FuncScale(None, (forward, backward))
        ax.set_yscale(func_scale)
        ax.set_theta_offset(np.pi / 2)
        # ax.set_rlabel_position(180 - 22.5)

        theta_width = 2 * np.pi / n_bins_theta
        theta_bins = np.arange(n_bins_theta + 1) * theta_width
        # Map directions to range(0, 2 pi)
        theta = theta % (2 * np.pi)

        values = np.zeros((n_bins_theta, n_bins_r))

        for i, (theta_lower, theta_upper) in enumerate(
            zip(theta_bins[:-1], theta_bins[1:])
        ):
            index = (theta >= theta_lower) & (theta < theta_upper)
            r_hist, r_bin_edges = np.histogram(
                r[index], bins=n_bins_r, range=(r.min(), r.max())
            )
            values[i] = r_hist

        # Scale values to percent
        values = values / len(r) * 100

        bottom = np.zeros(n_bins_theta)
        scaling_factor = 0.9
        theta_mid_points = (np.arange(n_bins_theta) + 0.5) * theta_width
        for i in range(n_bins_r):
            color = plt.cm.viridis(np.repeat(i / n_bins_r, n_bins_theta))
            ax.bar(
                theta_mid_points,
                values[:, i],
                width=theta_width * scaling_factor,
                bottom=bottom,
                color=color,
                label="{:.1f} to {:.1f}".format(r_bin_edges[i], r_bin_edges[i + 1]),
            )
            bottom += values[:, i]

        plt.legend(loc=(0.5, 0.2), title="Wind velocity in m/s")
        # Fixed formatter (not preferred)
        # ticks = ax.get_yticks()
        # ax.set_yticklabels(["{}%".format(int(i)) for i in ticks])

        # Flexible formatter
        ax.yaxis.set_major_formatter("{x}%")
