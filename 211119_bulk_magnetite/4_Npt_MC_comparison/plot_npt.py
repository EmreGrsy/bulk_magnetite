from cProfile import label
from turtle import color, width
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyrsistent import v

font = {"size": 20}
plt.rc("font", **font)
plt.rc("legend",fontsize=12)

# Radial distribution and g(r) integral of Fe2+,Fe3+,O2- ion pairs
fe2fe2_npt = pd.read_csv("\
fe2fe2_last3ns_delta_0001_step1.dat", sep="\s+", header=None)
fe3fe3_npt = pd.read_csv("\
fe3fe3_last3ns_delta_0001_step1.dat", sep="\s+", header=None)
fe2fe3_npt = pd.read_csv("\
fe2fe3_last3ns_delta_0001_step1.dat", sep="\s+", header=None)

# Fe(2+)-Fe(3+) 
fe2fe3_npt.columns = ["Distance", "RDF", "NumberDensity"]
fe3fe3_npt.columns = ["Distance", "RDF", "NumberDensity"]
fe2fe2_npt.columns = ["Distance", "RDF", "NumberDensity"]

# Define a figure object, is it important to explictly state this if there is more than one axes object
figure = plt.figure()

##########################
# Define axes
ax1 = figure.add_axes([0.0, 0.0, 1, 1])
ax2 = figure.add_axes([0.08, 0.60, 0.30, 0.35])

# Plot main npt part
ax1.plot(fe2fe2_npt["Distance"], fe2fe2_npt["RDF"], "b", linewidth=1.5, label="$\mathrm{g_{Fe^{2+}}}$")
ax1.plot(fe3fe3_npt["Distance"], fe3fe3_npt["RDF"], "r", linewidth=1.5, label="$\mathrm{g_{Fe^{3+}}}$")
ax1.plot(fe2fe3_npt["Distance"], fe2fe3_npt["RDF"], "green", linewidth=1, label="$\mathrm{g_{Fe^{3+}Fe^{2+}}}$")

# Manually add ideal lattice coordination shells
ax1.axvline(x=2.998135, color="black", ymax=1, ls="--", linewidth=1.5, label="crystal\nstructure")
ax1.axvline(x=3.515625, color="black", ymax=1, ls="--", linewidth=1.5)
ax1.axvline(x=3.671945, color="black", ymax=1, ls="--", linewidth=1.5)
ax1.axvline(x=5.192915, color="black", ymax=1, ls="--", linewidth=1.5)
ax1.axvline(x=5.507925, color="black", ymax=1, ls="--", linewidth=1.5)
ax1.axvline(x=5.996265, color="black", ymax=1, ls="--", linewidth=1.5)
ax1.axvline(x=6.704025, color="black", ymax=1, ls="--", linewidth=1.5)
ax1.axvline(x=6.950885, color="black", ymax=1, ls="--", linewidth=1.5)
ax1.axvline(x=7.031245, color="black", ymax=1, ls="--", linewidth=1.5)

###############################
## Plot zoomed npt part
# Shift Fe3 curve to match Fe2Fe3 curve
fe3fe3_npt["RDF"] = fe3fe3_npt["RDF"] + 4.6

ax2.plot(fe2fe2_npt["Distance"], fe2fe2_npt["RDF"], "b", linewidth=1.5, label="$\mathrm{g_{Fe^{2+}}}$")
ax2.plot(fe3fe3_npt["Distance"], fe3fe3_npt["RDF"], "r", linewidth=1.5, label="$\mathrm{g_{Fe^{3+}}}$")
ax2.plot(fe2fe3_npt["Distance"], fe2fe3_npt["RDF"], "green", linewidth=1.5, label="$\mathrm{g_{Fe^{3+}Fe^{2+}}}$")

ax2.axvline(x=2.998135, color="black", ymax=1, ls="--", linewidth=1.5, label="crystal\nstructure")
ax2.axvline(x=3.515625, color="black", ymax=1, ls="--", linewidth=1.5)
ax2.axvline(x=3.671945, color="black", ymax=1, ls="--", linewidth=1.5)
ax2.axvline(x=5.192915, color="black", ymax=1, ls="--", linewidth=1.5)
ax2.axvline(x=5.507925, color="black", ymax=1, ls="--", linewidth=1.5)
ax2.axvline(x=5.996265, color="black", ymax=1, ls="--", linewidth=1.5)
ax2.axvline(x=6.704025, color="black", ymax=1, ls="--", linewidth=1.5)
ax2.axvline(x=6.950885, color="black", ymax=1, ls="--", linewidth=1.5)
ax2.axvline(x=7.031245, color="black", ymax=1, ls="--", linewidth=1.5)

ax2.set_ylim([5.4,8])
ax2.set_xlim([2.9,3.11])

#ax2.yaxis.tick_right()
ax2.tick_params(axis='both', which='major', labelsize=10)
ax2.set_xlabel("r / $\mathrm{\AA}$", fontsize=10)
ax2.set_ylabel("$\mathrm{g}$(r)", fontsize=10)

# Restrict axes for clarity
ax1.set_ylim([0,10])
ax1.set_xlim([0,7.3])

# Define labels
ax1.set_xlabel("r / $\mathrm{\AA}$",labelpad=12)
ax1.set_ylabel("$\mathrm{g}$(r)", labelpad=15)

ax1.legend(loc="lower left", framealpha=0.0)

figure.savefig('RDF_NPT.pdf',format='pdf', bbox_inches = "tight")
figure.savefig('RDF_NPT.png',dpi=300.0,format='png', bbox_inches = "tight")