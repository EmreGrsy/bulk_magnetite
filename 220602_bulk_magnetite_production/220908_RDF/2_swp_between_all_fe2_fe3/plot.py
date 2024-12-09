import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter, NullFormatter

font = {'size'   : 20}
plt.rc('font', **font)

df = pd.read_csv("acceptance_vs_temp.txt", delimiter=" ")
df.columns =["temp","accepted_swp","swp_attempts"]

# Change units from kcal/mol to eV
df["acceptance_ratio"] = df["accepted_swp"] / df["swp_attempts"] 

fig, axs = plt.subplots()

axs.semilogx(df["temp"], df["acceptance_ratio"], linewidth=3, label="3x3x3 magnetite")

#axs.plot(df[""], df["dE_linear"], linewidth=3, label=r"$E_{charge\_ordered}-E_{sa,linear}$")
#axs.plot(df["layer"], df["dE_exp"], linewidth=3, label=r"$E_{charge\_ordered}-E_{sa,exponential}$")

#axs.set_ylim((-1.5, 1.5))

axs.set_ylabel(r"$\frac{N_{swap, accepted}}{N_{swap, attempts}}$",labelpad=12)
axs.set_xlabel("MC Temperature (K)",labelpad=12)

axs.legend(frameon=False, fontsize=10)

fig.savefig('acceptance_vs_temp.pdf',format='pdf', bbox_inches = "tight")
fig.savefig('acceptance_vs_temp.png', dpi=300.0,format='png', bbox_inches = "tight")