import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

# generate data: sine wave (x-y) with 1/z frequency dependency

Nx = 200
Nz = 91
x = np.linspace(-10, 10, Nx)
z = 0.1*np.linspace(-10, 10, Nz)**2 + 4

w = 2*np.pi

y = np.zeros((Nx, Nz))
for i in range(Nz):
    y[:, i] = np.cos(w*x/z[i]**0.5)/z[i]**0.2

# create waterfall plot
fig = plt.figure()
ax = fig.add_subplot(111)
for side in ['right', 'top', 'left']:
    ax.spines[side].set_visible(False)

highest = np.max(y)
lowest = np.min(y)
delta = highest-lowest
t = np.sqrt(abs(delta))/10
bottom = lowest*np.ones(Nx)

cmap= plt.get_cmap('viridis')
for i in np.flip(range(Nz)):
    yi_ = y[:,i]
    yi = yi_ + i*t
    zindex = Nz-i

    ax.fill_between(x, lowest, yi, facecolor="white", alpha=0.5, zorder=zindex)

    points = np.array([x, yi]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    # Create a continuous norm to map from data points to colors
    norm = plt.Normalize(lowest, highest)
    lc = LineCollection(segments, cmap='plasma', norm=norm)
    # Set the values used for colormapping
    lc.set_array(yi_)
    lc.set_zorder(zindex)
    lc.set_linewidth(1)
    line = ax.add_collection(lc)
    delta_x = max(x)-min(x)
    if (i)%10==0:
        ax.text(min(x)-5e-2*delta_x, t*i, "$\\theta=%i^\\circ$"%i, horizontalAlignment="right")

ax.set_ylim(lowest, highest + Nz*t)
ax.set_xlim(-10, 10)
fig.colorbar(line, ax=ax)
print("saving image...")
plt.yticks([])
ax.yaxis.set_ticks_position('none')
fig.savefig("waterfall_plot_cmap")
