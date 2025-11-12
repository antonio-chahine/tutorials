import ROOT

# Open the file
file = ROOT.TFile("/ceph/submit/data/group/cms/store/fccee/samples/winter2023/CLD_FullSim/wzp6_ee_mumuH_ecm240/mumuH_rec_16610_191.root")

# Get the tree of events
tree = file.Get("events")

# Create a histogram to store the energies
h = ROOT.TH1D("h", "Energy [GeV]", 100, 0, 1000)

# for loop over the first 10 events, and print information about the MC particles
for i in range(10):
    
    print("Processing event", i)
    tree.GetEntry(i)

    # get the MC particles for this event
    MCParticles = tree.MCParticles
    print("Number of MC particles:", len(MCParticles))

    # loop over all particles in the event
    for j in range(len(MCParticles)):

        # print their information
        print("MC Particle", j)
        print("Momentum (px, py, pz):", MCParticles[j].momentum.x, MCParticles[j].momentum.y, MCParticles[j].momentum.z)
        print("Charge:", MCParticles[j].charge)
        print("PDG ID:", MCParticles[j].PDG)

        # calculate the energy
        energy = (MCParticles[j].momentum.x**2 + MCParticles[j].momentum.y**2 + MCParticles[j].momentum.z**2 + MCParticles[j].mass**2)**0.5
        print("Energy:", energy)

        # if the particle has more than 10 GeV of energy, fill the histogram
        if energy > 10:
            h.Fill(energy)

# draw the histogram, this is done using a Canvas
c = ROOT.TCanvas()
h.Draw()

# label the axes
h.GetXaxis().SetTitle("Energy [GeV]")
h.GetYaxis().SetTitle("Number of particles")

# draw the canvas
c.Draw()

# save the plot to a file
c.SaveAs("energy.png")

# save the histogram to a .root file
file_out = ROOT.TFile("output.root", "RECREATE")
h.Write()
file_out.Close()

print("All done!")
