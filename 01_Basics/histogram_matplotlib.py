import matplotlib.pyplot as plt
import mplhep as hep 
import uproot

file = uproot.open("output.root")
h=file["h"]
values = h.values()       # bin contents
edges = h.axis().edges()  # bin edges
centers = 0.5*(edges[1:] + edges[:-1])


hep.style.use("CMS")
plt.style.use(hep.style.CMS)

fig = plt.figure()
ax = fig.subplots()

hep.histplot(values, bins=edges, label="$e^+e^-\\to\mu^+\mu^-$", ax=ax)

ax.set_ylabel("Events")
ax.legend(loc=(1.01, 0), fontsize='x-small')
ax.set_yscale("log")
ax.set_xlabel("$E$ [GeV]")


hep.label.exp_label(exp="FCC-ee", ax=ax, lumi=1, data=False, com=240)

fig.savefig("pretty_energy.png", bbox_inches="tight")