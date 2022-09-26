# WindRose

## Overview

Python module to make windrose plots.

## Installation
```bash
cd <path to repository>
pip install .
```
You can test the installation with
```bash
cd <path to repository>
pytest
```
## Example

```python
N = 8
n_repeats = 10

theta = np.repeat(np.linspace(0.0, 2 * np.pi, N, endpoint=False), n_repeats)
width = 2 * np.pi / N
radii = np.random.rand(N * n_repeats)

fig = plt.figure(figsize=(12,12))
Windrose(radii, theta, n_bins_r=3, n_bins_theta=N, fig=fig)
plt.legend()
```
