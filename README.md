# High-Order Laplacian Spurious Eigenvalues

Supplementary notebooks for the paper
*On Spurious Eigenvalues of High-Order Finite Difference Schemes for the Laplace Operator*.

This repository contains the exact-rational verification notebooks used in the appendix-level symbolic computations for the candidate zero and the exclusion of the extraneous branch.

## Repository Contents

- `condition_a_exact_rational_certificate.ipynb`  
  Exact rational verification of condition (a) in Theorem 5 for the selected candidate
  \((\lambda^\ast, s_0^\ast, s_1^\ast, s_2^\ast)\).

- `lemma4_exact_rational_certificate.ipynb`  
  Exact rational verification of the branch-selection step used in Lemma 4, excluding the extraneous branch.

## Requirements

- Python 3
- Jupyter Notebook or JupyterLab

The notebooks were saved with a Python kernel named `high_order_Lap`.

## How to Run

1. Clone the repository.
2. Launch Jupyter Notebook or JupyterLab in the repository root.
3. Open the notebook of interest.
4. Run all cells from top to bottom.

The notebooks are intended to be self-contained supplementary computations. Outputs stored in the notebooks should allow quick inspection without additional scripts.

## Relation to the Manuscript

These notebooks support the verification steps referenced in the appendix section
`Verification for the Candidate Zero`.

In particular, they document the exact-rational computations behind:

- the verification of condition (a) in Theorem 5;
- the proof of the lemma excluding the extraneous branch.

<!-- ## Citation

If you use these notebooks, please cite the associated paper:

> Yizhe Feng, Weiguo Gao, and Meiyue Shao,  
> *On Spurious Eigenvalues of High-Order Finite Difference Schemes for the Laplace Operator*.

If a journal reference, DOI, or arXiv link becomes available, it should be added here. -->

## Notes

- This repository currently contains only the supplementary notebooks needed for the exact-rational verification steps.
- No claim is made that the notebooks provide a complete computational pipeline for the full paper.
