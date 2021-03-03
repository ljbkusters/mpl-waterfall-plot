import matplotlib.pyplot as plt
import numpy as np

# generate data: sine wave (x-y) with 1/sqrt(z) frequency dependency
# this is simply some "interesting looking" dummy data
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
print(lowest)
bottom = lowest*np.ones(Nx)
for i in np.flip(range(Nz)):
    yi = y[:,i] + i*t
    zindex = Nz-i
    ax.fill_between(x, lowest, yi, facecolor="white", alpha=0.5, zorder=zindex)
    ax.plot(x, yi, c="black", zorder=zindex, lw=0.5)
    delta_x = max(x)-min(x)
    if (i)%10==0:
        ax.text(min(x)-5e-2*delta_x, t*i, "$\\theta=%i^\\circ$"%i, horizontalAlignment="right")

plt.yticks([])
ax.yaxis.set_ticks_position('none')
fig.savefig("waterfall_plot")
