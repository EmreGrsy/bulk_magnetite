from cProfile import label
from turtle import color, width
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from pyrsistent import v
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

font = {"size": 22}
plt.rc("font", **font)
plt.rc("legend",fontsize=16)

# Radial distribution and g(r) integral of Fe2+,Fe3+,O2- ion pairs
fe2fe2_nvt = pd.read_csv("fe2_fe2_0.001.data", sep="\s+", header=None)
fe3fe3_nvt = pd.read_csv("fe3_fe3_0.001.data", sep="\s+", header=None)
fe2fe3_nvt = pd.read_csv("fe3_fe2_0.001.data", sep="\s+", header=None)

# Fe(2+)-Fe(3+) 
fe2fe3_nvt.columns = ["Distance", "RDF", "NumberDensity"]
fe3fe3_nvt.columns = ["Distance", "RDF", "NumberDensity"]
fe2fe2_nvt.columns = ["Distance", "RDF", "NumberDensity"]

# Define subplots
#fig, ax1 = plt.subplots()

# Define a figure object, is it important to explictly state this if there is more than one axes object
figure = plt.figure()

##########################
# Define axes
ax1 = figure.add_axes([0.0, 0.0, 1, 1])
ax2 = figure.add_axes([0.06, 0.60, 0.30, 0.35])

# Plot main NVT part
ax1.plot(fe2fe2_nvt["Distance"], fe2fe2_nvt["RDF"], "b", linewidth=3, label="$\mathrm{{Fe^{2+}}}$")
ax1.plot(fe3fe3_nvt["Distance"], fe3fe3_nvt["RDF"], "r", linewidth=3, label="$\mathrm{{Fe^{3+}}}$")
ax1.plot(fe2fe3_nvt["Distance"], fe2fe3_nvt["RDF"], "green", linewidth=3, label="$\mathrm{{Fe^{3+}Fe^{2+}}}$")

# Manually add ideal lattice coordination shells
ax1.axvline(x=2.998135, color="black", ymax=1, ls="--", linewidth=2, label="ideal\nlattice")
ax1.axvline(x=3.515625, color="black", ymax=1, ls="--", linewidth=2)
ax1.axvline(x=3.671945, color="black", ymax=1, ls="--", linewidth=2)
ax1.axvline(x=5.192915, color="black", ymax=1, ls="--", linewidth=2)
ax1.axvline(x=5.507925, color="black", ymax=1, ls="--", linewidth=2)
ax1.axvline(x=5.996265, color="black", ymax=1, ls="--", linewidth=2)
ax1.axvline(x=6.704025, color="black", ymax=1, ls="--", linewidth=2)
ax1.axvline(x=6.950885, color="black", ymax=1, ls="--", linewidth=2)
ax1.axvline(x=7.031245, color="black", ymax=1, ls="--", linewidth=2)

###############################
## Plot zoomed NVT part
# Shift Fe3 curve to match Fe2Fe3 curve
#fe3fe3_nvt["RDF"] = fe3fe3_nvt["RDF"] + 3.5

ax2.plot(fe2fe2_nvt["Distance"], fe2fe2_nvt["RDF"], "b", linewidth=3, label="$\mathrm{{Fe^{2+}}}$")
ax2.plot(fe3fe3_nvt["Distance"], fe3fe3_nvt["RDF"], "r", linewidth=3, label="$\mathrm{{Fe^{3+}}}$")
ax2.plot(fe2fe3_nvt["Distance"], fe2fe3_nvt["RDF"], "green", linewidth=3, label="$\mathrm{{Fe^{3+}Fe^{2+}}}$")

ax2.axvline(x=2.998135, color="black", ymax=1, ls="--", linewidth=2, label="ideal\nlattice")
ax2.axvline(x=3.515625, color="black", ymax=1, ls="--", linewidth=1.5)
ax2.axvline(x=3.671945, color="black", ymax=1, ls="--", linewidth=1.5)
ax2.axvline(x=5.192915, color="black", ymax=1, ls="--", linewidth=1.5)
ax2.axvline(x=5.507925, color="black", ymax=1, ls="--", linewidth=1.5)
ax2.axvline(x=5.996265, color="black", ymax=1, ls="--", linewidth=1.5)
ax2.axvline(x=6.704025, color="black", ymax=1, ls="--", linewidth=1.5)
ax2.axvline(x=6.950885, color="black", ymax=1, ls="--", linewidth=1.5)
ax2.axvline(x=7.031245, color="black", ymax=1, ls="--", linewidth=1.5)

#ax2.set_ylim([4,18])
ax2.set_xlim([2.8,3.2])
#ax2.yaxis.tick_right()
#ax2.tick_params(axis='both', which='major', labelsize=14)
ax2.set_yticks([])

#ax2.yaxis.tick_right()
#ax2.tick_params(axis='both', which='major', labelsize=20)
#ax2.set_xlabel("r / $\mathrm{\AA}$", fontsize=16)
#ax2.set_ylabel("$\mathrm{g}$(r)", fontsize=16)

# Restrict axes for clarity
ax1.set_ylim([0,18])
ax1.set_xlim([0,7.3])

# Define labeles
ax1.set_xlabel(r"$r\,(\mathrm{\AA})$",labelpad=12, fontsize=24)
ax1.set_ylabel(r"$g\,(r)$", labelpad=15, fontsize=24)

ax1.legend(loc="lower left", framealpha=0.0)

figure.savefig('RDF_NVT_1e5.pdf',format='pdf', bbox_inches = "tight")
figure.savefig('RDF_NVT_1e5.png',dpi=300.0,format='png', bbox_inches = "tight")