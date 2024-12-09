import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter, NullFormatter

font = {'size'   : 32}
plt.rc('font', **font)

#### X
df = pd.read_csv("fe_comp_x.txt", delimiter=" ")
df.columns =["layer","fe_3","fe_2"]
df["fe3_ratio"] = df["fe_3"]/(df["fe_2"]+df["fe_3"])

#### Y
df1 = pd.read_csv("fe_comp_y.txt", delimiter=" ")
df1.columns =["layer","fe_3","fe_2"]
df1["fe3_ratio"] = df1["fe_3"]/(df1["fe_2"]+df1["fe_3"])

#### Z
df2 = pd.read_csv("fe_comp_z.txt", delimiter=" ")
df2.columns =["layer","fe_3","fe_2"]
df2["fe3_ratio"] = df2["fe_3"]/(df2["fe_2"]+df2["fe_3"])

###############
fig, axs = plt.subplots(1,3, sharey=True, figsize=(9,3))

axs[0].plot(df["fe3_ratio"], df["layer"], "b",linewidth=4, label=r"$E_{charge\_ordered}-E_{sa,linear}$")
axs[1].plot(df1["fe3_ratio"], df1["layer"], "b",linewidth=4, label=r"$E_{charge\_ordered}-E_{sa,linear}$")
axs[2].plot(df2["fe3_ratio"], df2["layer"], "b",linewidth=4, label=r"$E_{charge\_ordered}-E_{sa,linear}$")

axs[0].set_ylabel(r'$\mathrm{Fe_{oct}}$ layer',labelpad=15 )

axs[0].set_xticks([0.2, 0.8])
axs[1].set_xticks([0.2, 0.8 ])
axs[2].set_xticks([0.2, 0.8])

#axs[0].set_xticklabels(axs[0].get_xticks(), rotation = 70)
#axs[1].set_xticklabels(axs[1].get_xticks(), rotation = 70)
#axs[2].set_xticklabels(axs[2].get_xticks(), rotation = 70)

axs[0].title.set_text('X')
axs[1].title.set_text('Y')
axs[2].title.set_text('Z')
#axs[0].set_xlabel(r"$\frac{N_{\mathrm{{Fe_{oct}}^{III}}}}{N_{\mathrm{{Fe_{oct}}^{III}}}+N_{\mathrm{{Fe_{oct}}^{II}}}}$",labelpad=15)

#fig.subplots_adjust(wspace=0.05)
fig.text(0.5, -0.3, r"$\frac{N_{\mathrm{{Fe}_{oct}^{III}}}}{N_{\mathrm{{Fe}_{oct}^{III}}}+N_{\mathrm{{Fe}_{oct}^{II}}}}$", ha='center')


#fig.savefig('bulk_charge_ordering.pdf',format='pdf', bbox_inches = "tight")
#fig.savefig('bulk_charge_ordering.png', dpi=300.0,format='png', bbox_inches = "tight")
fig.savefig('bulk_charge_ordering.svg',format='svg', bbox_inches = "tight")
