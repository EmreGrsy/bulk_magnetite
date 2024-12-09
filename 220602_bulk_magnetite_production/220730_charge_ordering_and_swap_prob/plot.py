import pandas as pd
import matplotlib.pyplot as plt

font = {"size": 22}
plt.rc("font", **font)
plt.rc("legend",fontsize=16)

df = pd.read_csv("acceptance.data", delimiter=" ")
df1 = pd.read_csv("4x4x4_acc.data", delimiter=r"\s+")

df.columns =["temp", "PE", "swp_attempts", "swp_accepted", "n_fet3", "n_oct3"]
df1.columns =["temp", "PE", "swp_attempts", "swp_accepted", "n_fet3", "n_oct3"]

# Change units from kcal/mol to eV
df["acceptance_ratio_all"] = df["swp_accepted"] / df["swp_attempts"]
df1["acceptance_ratio_all"] = df1["swp_accepted"] / df1["swp_attempts"]

fig, axs = plt.subplots()
axs.text(0.145, 0.45, '(a)',verticalalignment='top', horizontalalignment='right',transform=axs.transAxes)
####################

axin = axs.inset_axes([0.62, 0.60, 0.35, 0.35])

axin.plot(df["temp"], df["acceptance_ratio_all"], linewidth=4,  color="blue", label="3x3x3")
axin.plot(df1["temp"], df1["acceptance_ratio_all"], linewidth=4, color="green", label="4x4x4")

axin.axvline(x=459, color="blue", ymax=1, ls="--", linewidth=3)
axin.axvline(x=333, color="green", ymax=1, ls="--", linewidth=3)

axin.set_xticks((333, 459))

axin.set_yticks([0, 1e-4])

axin.ticklabel_format(style="sci", axis="y")

axin.set_ylim(-0.0000183, 0.000183)

axin.set_xlim(600, 300)

#########################

axs.semilogx(df["temp"], df["acceptance_ratio_all"], linewidth=4, color="blue", label="3x3x3")
axs.semilogx(df1["temp"], df1["acceptance_ratio_all"], linewidth=4, color="green", label="4x4x4")

axs.set_xlim(axs.get_xlim()[::-1])
#axs.set_xticks((459, 1e3, 1e4, 1e5))

axs.legend(loc="lower left", frameon=False, fontsize=18, labelcolor="linecolor",)

axs.set_ylabel(r"$\frac{n_{\mathrm{accepted}}}{n_{\mathrm{attempts}}}$",labelpad=14,fontsize=24)
axs.set_xlabel(r"$T^{\mathrm{MC}}$ (K)",labelpad=12,fontsize=24)
#axs.axvline(x=459, color="black", ymax=1, ls="--", linewidth=2)
#axs.axhline(y=0.83, color="black", xmax=0.4, ls="--", linewidth=2)
axs.set_yticks((0.0, 0.3, 0.6, 0.9))


#fig.savefig('acceptance_vs_temp.pdf',format='pdf',bbox_inches = "tight")
#fig.savefig('acceptance_vs_temp.png', dpi=300.0,format='png', bbox_inches = "tight")
fig.savefig('acceptance_vs_temp.svg',format='svg',bbox_inches = "tight")
