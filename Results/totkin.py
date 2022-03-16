import numpy as np
import matplotlib
from matplotlib import pyplot as plt
matplotlib.rcParams['text.usetex'] = True

path = "/home/ignacio/DonElias/NPT.Lambda/05ALA/helix/eq/totkin.dat"
data = np.loadtxt(path)

fig,  ax = plt.subplots(figsize=(10, 5))
ax.plot(data[:, 0], data[:, 1], color="k", lw=1)
ax.set_xlabel('time [ps]', fontsize=16)
ax.set_ylabel('Kinetic energy [kJ/mol]', fontsize=16)
#ax.set_title('Kinetic Energy evolution during Thermalization')


fig.savefig("/home/ignacio/CINV/Memoria/Figures/CH4/totkin.png")
plt.show()

print()
