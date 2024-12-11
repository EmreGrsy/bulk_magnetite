# Bulk Magnetite

[![DOI](https://img.shields.io/badge/DOI-10.1021/acs.jpclett.3c01290-blue)](https://pubs.acs.org/doi/full/10.1021/acs.jpclett.3c01290)  

This repository contains scripts and data related to the bulk section of [**Oxidation-State Dynamics and Emerging Patterns in Magnetite**](https://pubs.acs.org/doi/full/10.1021/acs.jpclett.3c01290)  

[<img src="bulk.png" alt="Table of Contents Figure" width="35%">](https://pubs.acs.org/doi/full/10.1021/acs.jpclett.3c01290) 

## Overview  
This repository includes scripts and data used for studing the structural and thermodynamic properties of bulk magnetite through oxidation state swaps. The scripts support tasks such as oxidation state minimization, analyzing radial distribution functions (RDF), comparing ensembles, exploring different minimization schemes, and investigating phenomena like trimerons and phase transitions.

## Repository Structure  
```
bulk_magnetite/
│
├── 211119_bulk_magnetite/                       # Scripts for bulk magnetite oxidation state swaps
│   ├── 1_generate_bulk/                         # Generate bulk structures
│   ├── 2_oxidation_state_min/                   # Basic oxidation state minimization
│   ├── 3_NVT_MC_comparison/                     # Comparison of NVT and NVT+MC ensembles
│   │   ├── 1_NVT/
│   │   ├── 2_NVT_MC/
│   │   ├── 3_analyze/
│   ├── 4_NPT_MC_comparison/                     # Comparison of NPT and NPT+MC ensembles
│   ├── 5_oxidation_state_min_different_scheme/  # Alternative minimization schemes
│
├── 220602_bulk_magnetite_production/            # Results used in the publication
│   ├── 220730_charge_ordering_and_swap_prob/    # Charge ordering and MC swap probabilities
│   ├── 220908_RDF/                              # Radial distribution function analysis
│   ├── 220919_varying_size/                     # Size effects and convergence checks
│   ├── 221021_trimeron_analysis/                # Trimeron fingerprint analysis
│   ├── 230406_heating_up_hysteresis/            # Swap probability with increasing MC temperature
│
├── 230207_example_input_script/                 # Example oxidation state swap scripts shared in the publication

├── 230308_bulk_magnetite_transition/            # Fd3m -> Cc transition modeling
│   ├── 1_Fd3m/
│   ├── 2_Cc/

└── README.md              
```

## Related Publications  
If you use this repository, please cite the original paper:  
```bibtex
@article{Grsoy2023,
  title = {Oxidation-State Dynamics and Emerging Patterns in Magnetite},
  volume = {14},
  ISSN = {1948-7185},
  url = {http://dx.doi.org/10.1021/acs.jpclett.3c01290},
  DOI = {10.1021/acs.jpclett.3c01290},
  number = {30},
  journal = {The Journal of Physical Chemistry Letters},
  publisher = {American Chemical Society (ACS)},
  author = {G\"{u}rsoy,  Emre and Vonbun-Feldbauer,  Gregor B. and Meißner,  Robert H.},
  year = {2023},
  month = jul,
  pages = {6800–6807}
}
```
