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

# Fe(2+)-Fe(3+) of global min
fe2fe3_nvt.columns = ["Distance", "RDF", "NumberDensity"]
fe3fe3_nvt.columns = ["Distance", "RDF", "NumberDensity"]
fe2fe2_nvt.columns = ["Distance", "RDF", "NumberDensity"]

# Radial distribution and g(r) integral of Fe2+,Fe3+,O2- ion pairs
fe2fe2_nvt_1e5 = pd.read_csv("../7_1e5_temp_nvt_mc/fe2_fe2_0.001.data", sep="\s+", header=None)
fe3fe3_nvt_1e5 = pd.read_csv("../7_1e5_temp_nvt_mc/fe3_fe3_0.001.data", sep="\s+", header=None)
fe2fe3_nvt_1e5 = pd.read_csv("../7_1e5_temp_nvt_mc/fe3_fe2_0.001.data", sep="\s+", header=None)

# Fe(2+)-Fe(3+) of elevated temp.
fe2fe3_nvt_1e5.columns = ["Distance", "RDF", "NumberDensity"]
fe3fe3_nvt_1e5.columns = ["Distance", "RDF", "NumberDensity"]
fe2fe2_nvt_1e5.columns = ["Distance", "RDF", "NumberDensity"]

# Define a figure object, is it important to explictly state this if there is more than one axes object
fig, axs = plt.subplots(2, sharex=True)

#fe3fe3_nvt["RDF"] = fe3fe3_nvt["RDF"] + 3
#fe3fe3_nvt_1e5["RDF"] = fe3fe3_nvt_1e5["RDF"] + 3.5

ax1 = axs[0]
ax2 = axs[1]

# Plot main NVT part of global min.
ax1.plot(fe2fe2_nvt["Distance"], fe2fe2_nvt["RDF"], "b", linewidth=4, label="$\mathrm{{Fe^{2+}}}$")
ax1.plot(fe3fe3_nvt["Distance"], fe3fe3_nvt["RDF"], "r", linewidth=4, label="$\mathrm{{Fe^{3+}}}$")
ax1.plot(fe2fe3_nvt["Distance"], fe2fe3_nvt["RDF"], "green", linewidth=4, label="$\mathrm{{Fe^{3+}Fe^{2+}}}$")

# Plot main NVT part of elevated temp.
ax2.plot(fe2fe2_nvt_1e5["Distance"], fe2fe2_nvt_1e5["RDF"], "b", linewidth=4, label="$\mathrm{{Fe^{2+}}}$")
ax2.plot(fe3fe3_nvt_1e5["Distance"], fe3fe3_nvt_1e5["RDF"], "r", linewidth=4, label="$\mathrm{{Fe^{3+}}}$")
ax2.plot(fe2fe3_nvt_1e5["Distance"], fe2fe3_nvt_1e5["RDF"], "green", linewidth=4, label="$\mathrm{{Fe^{3+}Fe^{2+}}}$")


# Manually add ideal lattice coordination shells
ax1.axvline(x=2.998135, color="black", ymax=1, ls="--", linewidth=2, label="Ideal lattice")
ax2.axvline(x=2.998135, color="black", ymax=1, ls="--", linewidth=2, label="Ideal lattice")

# Restrict axes for clarity
#ax1.set_ylim([0,8])
#ax1.set_ylim([3.3, 9])
ax1.set_xlim([2.7, 3.3])

#ax2.set_ylim([4, 18])
#ax2.set_yticks([15, 8])
#ax2.set_xlim([2.9,3.11])

# Define label
ax2.set_xlabel(r"$r\,(\mathrm{\AA})$",labelpad=12, fontsize=24)

ax1.text(0.11, 0.95, '(a)',verticalalignment='top', horizontalalignment='right',transform=ax1.transAxes)
ax1.text(0.99, 0.93, r'$T^\mathrm{MC} < T^\mathrm{MC}_\mathrm{c}$',verticalalignment='top', horizontalalignment='right',transform=ax1.transAxes)

ax2.text(0.11, 0.95, '(b)',verticalalignment='top', horizontalalignment='right',transform=ax2.transAxes)
ax2.text(0.99, 0.93, r'$T^\mathrm{MC} > T^\mathrm{MC}_\mathrm{c}$',verticalalignment='top', horizontalalignment='right',transform=ax2.transAxes)

ax1.legend(bbox_to_anchor=(0.5, 1.36), framealpha=0.0, ncol=2, loc='center')

fig.text(-0.05, 0.5, r"$g\,(r)$", va='center', rotation='vertical')

fig.savefig('RDF_NVT_zoomed1.pdf',format='pdf', bbox_inches = "tight")
fig.savefig('RDF_NVT_zoomed1.png',dpi=300.0,format='png', bbox_inches = "tight")