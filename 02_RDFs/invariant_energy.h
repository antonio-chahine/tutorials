
#include "FCCAnalyses/MCParticle.h"

ROOT::VecOps::RVec<float> get_invariant_mass(const ROOT::VecOps::RVec<edm4hep::MCParticleData>& particles) {
  ROOT::VecOps::RVec<float> result;

  TLorentzVector mu, antimu;
  double max_mu_E = 0, max_antimu_E = 0;

  for (auto & p: particles) {
    double E = sqrt(p.momentum.x*p.momentum.x + p.momentum.y*p.momentum.y + p.momentum.z*p.momentum.z + p.mass*p.mass);
    if (p.PDG == 13 && E > max_mu_E) {
      mu.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
      max_mu_E = E;
    }
    else if (p.PDG == -13 && E > max_antimu_E) {
      antimu.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
      max_antimu_E = E;
    }
  }

  if (max_mu_E > 0 && max_antimu_E > 0) {
    TLorentzVector combined = mu + antimu;
    result.push_back(combined.M());
  }

  return result;
}
