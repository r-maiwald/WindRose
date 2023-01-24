import numpy as np


from context import Windrose

def test_windrose():
    # Create example data
    rng = np.random.default_rng(1)
    r = rng.normal(loc=np.repeat(2, 100))**2
    theta = rng.normal(loc=np.repeat(1, 100), scale=0.5)

    n_bins_r = 5
    n_bins_theta = 16
    Windrose(r, theta, n_bins_r, n_bins_theta)
