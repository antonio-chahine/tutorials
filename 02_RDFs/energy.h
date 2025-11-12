#include "FCCAnalyses/MCParticle.h"

ROOT::VecOps::RVec<float> get_energy(const ROOT::VecOps::RVec<edm4hep::MCParticleData>& particles) {
  ROOT::VecOps::RVec<float> result;
  for (auto & p: particles) {
    TLorentzVector tlv;
    tlv.SetXYZM(p.momentum.x, p.momentum.y, p.momentum.z, p.mass);
    float energy = tlv.E();
    if (energy > 10) {
      result.push_back(energy);
    }
  }
  return result;
}