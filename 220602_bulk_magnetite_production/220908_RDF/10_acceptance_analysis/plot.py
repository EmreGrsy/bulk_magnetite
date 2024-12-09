import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter, NullFormatter

font = {"size": 22}
plt.rc("font", **font)
plt.rc("legend",fontsize=16)

df = pd.read_csv("/home/emre/220602_bulk_magnetite_SA/220908_RDF/2_swp_between_all_fe2_fe3/acceptance_vs_temp.txt", delimiter=" ")
df.columns =["temp","accepted_swp_all","accepted_swp_oct", "swp_attempts"]

# Change units from kcal/mol to eV
df["acceptance_ratio_all"] = df["accepted_swp_all"] / df["swp_attempts"] 
df["acceptance_ratio_oct"] = df["accepted_swp_oct"] / df["swp_attempts"] 

fig, axs = plt.subplots()

axs.semilogx(df["temp"], df["acceptance_ratio_all"], linewidth=4, label="all Fe ions", color="blue")
axs.semilogx(df["temp"], df["acceptance_ratio_oct"], linewidth=4, label=r"$\mathrm{Fe_{oct}}$ ions", color="red")

#axs.plot(df[""], df["dE_linear"], linewidth=3, label=r"$E_{charge\_ordered}-E_{sa,linear}$")
#axs.plot(df["layer"], df["dE_exp"], linewidth=3, label=r"$E_{charge\_ordered}-E_{sa,exponential}$")

axs.set_yticks((0.0, 0.5, 0.83, 1.0))

axs.set_ylabel(r"$\frac{N_{\mathrm{accepted}}}{N_{\mathrm{attempts}}}$",labelpad=14,fontsize=24)
axs.set_xlabel(r"$T^{\mathrm{MC}}$ (K)",labelpad=12,fontsize=24)
axs.axvline(x=1e5, color="black", ymax=0.83, ls="--", linewidth=2)
axs.axhline(y=0.83, color="black", xmax=0.4, ls="--", linewidth=2)
axs.set_xticks((1e3, 1e4, 1e5, 1e6, 1e8))

axs.legend(frameon=False, fontsize=20)

fig.savefig('acceptance_vs_temp.pdf',format='pdf', bbox_inches = "tight")
fig.savefig('acceptance_vs_temp.png', dpi=300.0,format='png', bbox_inches = "tight")