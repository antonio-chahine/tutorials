import ROOT

ROOT.gInterpreter.ProcessLine("""
#include "invariant_energy.h"
"""
)

# Open the file
f = ROOT.TFile.Open("/ceph/submit/data/group/cms/store/fccee/samples/winter2023/CLD_FullSim/wzp6_ee_mumuH_ecm240/mumuH_rec_16610_191.root")

# Get the tree
tree = f.Get("events")

# Create the RDF
df = ROOT.RDataFrame(tree)

df = df.Define("DimuonMass", "get_invariant_mass(MCParticles)")
h = df.Histo1D(("DimuonMassHist", "", 100, 0, 200), "DimuonMass")


# Draw the histogram
c = ROOT.TCanvas()
h.Draw()
c.Draw()

# save the histogram
c.SaveAs("energy.png")