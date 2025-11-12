import ROOT
import math

# Open the file and get the tree
file = ROOT.TFile("/ceph/submit/data/group/cms/store/fccee/samples/winter2023/CLD_FullSim/wzp6_ee_mumuH_ecm240/mumuH_rec_16610_191.root")
tree = file.Get("events")

# Create histogram for invariant mass
h = ROOT.TH1D("h", "Invariant Mass of Mu+ Mu- [GeV]", 100, 0, 200)

# Loop over events
for i in range(500):
    tree.GetEntry(i)
    MCParticles = tree.MCParticles

    # Lorentz vectors for highest-energy muon and anti-muon
    mu_minus = ROOT.TLorentzVector()
    mu_plus = ROOT.TLorentzVector()
    max_mu_e = 0
    max_anti_e = 0

    for j in range(len(MCParticles)):
        pdg = MCParticles[j].PDG
        p = MCParticles[j].momentum
        mass = MCParticles[j].mass
        energy = math.sqrt(p.x**2 + p.y**2 + p.z**2 + mass**2)

        # Most energetic mu-
        if pdg == 13 and energy > max_mu_e:
            mu_minus.SetPxPyPzE(p.x, p.y, p.z, energy)
            max_mu_e = energy

        # Most energetic mu+
        if pdg == -13 and energy > max_anti_e:
            mu_plus.SetPxPyPzE(p.x, p.y, p.z, energy)
            max_anti_e = energy

    # Only fill if both exist
    if max_mu_e > 0 and max_anti_e > 0:
        combined = mu_minus + mu_plus
        h.Fill(combined.M())

# Draw and save
c = ROOT.TCanvas()
h.Draw()
h.GetXaxis().SetTitle("m_{μ⁺μ⁻} [GeV]")
h.GetYaxis().SetTitle("Entries")
c.SaveAs("mumu_invariant_mass.png")

# Save histogram
out = ROOT.TFile("output.root", "RECREATE")
h.Write()
out.Close()

print("All done!")
