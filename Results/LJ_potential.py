import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['text.usetex'] = True

def ljp(r, epsilon, sigma):

    return 48 * epsilon * np.power(sigma, 12) / np.power(r, 13) \
        - 24 * epsilon * np.power(sigma, 6) / np.power(r, 7)


def ljp1(r, epsilon, sigma):

    return 48 * epsilon * np.power(sigma, 12) / np.power(r, 12) \
        - 24 * epsilon * np.power(sigma, 6) / np.power(r, 6)


def atractive(r, epsilon, sigma):
    return 48 * epsilon * np.power(sigma, 6) / np.power(r, 7)


def repulsive(r, epsilon, sigma):
    return -48 * epsilon * np.power(sigma, 12) / np.power(r, 13)


fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

r = np.linspace(3.5, 6, 100)

ax1.plot(r, atractive(r, 0.0103, 3.3), color='red',
         label='Attractive Force ' r'$(r^{-6})$', lw=1)
ax1.plot(r, repulsive(r, 0.0103, 3.3), color='blue',
         label='Repuslive Force ' r'$(r^{-12})$', lw=1)
ax1.plot(r, ljp1(r, 0.0103, 3.3), color='k',
         label='Total LJ potential', lw=1)
ax1.set_xlabel('Distance (r) in ' + u"\u00C5", fontsize=16)
ax1.set_ylabel('Potential Energy [eV]', fontsize=16)
ax1.set_title('Lennard Jones Force Terms', fontsize=16)

ax1.grid()
ax1.legend()
ax1.set_xlim(3.4, 6)

ax2.plot(r, ljp(r, 0.0103, 3.3), color='k', lw=1)
ax2.set_xlabel('Distance (r) in ' + u"\u00C5", fontsize=16)
ax2.set_ylabel('Potential Energy [eV]', fontsize=16)
ax2.set_title('Lennard-Jones FF Parameters', fontsize=16)

ax2.hlines(y=0, xmin=3.4, xmax=6, color='grey', lw=1, ls=(0, (5, 5)))
ax2.annotate('', xy=(4.1, 0), xytext=(4.1, -0.0075),
             arrowprops=dict(arrowstyle='<|-|>', color='r', lw=1, ls='-'))
ax2.annotate('', xy=(3.4, -0.0007), xytext=(3.7, -0.0007), arrowprops=dict(
    arrowstyle='<|-|>', color='r', lw=1, ls='-'))
ax2.text(3.52, -0.002, r'$\sigma$', fontsize=18)
ax2.text(4.147, -0.00396, r'$\epsilon$', fontsize=18)
ax2.text(4.1, 0.0006, r'$r_{min}$', fontsize=18)

# ax2.grid()

fig1.savefig('/home/ignacio/CINV/Memoria/Figures/CH2/LJ_1.png')
fig2.savefig('/home/ignacio/CINV/Memoria/Figures/CH2/LJ_2.png')
plt.show()
