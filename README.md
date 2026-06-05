# High-Order Laplacian Spurious Eigenvalues

This repository contains exact certificate files for the paper *On Spurious Eigenvalues of High-Order Finite Difference Schemes for the Laplace Operator*.

## Repository Structure

```text
.
├── maple_code/
│   └── localize_candidate_zero.mpl
├── notebooks/
│   ├── condition_a_exact_rational_certificate.ipynb
│   ├── lambda_nonreal_exact_rational_certificate.ipynb
│   ├── lemma4_exact_rational_certificate.ipynb
│   ├── rational_tools.py
│   └── shared_certificate_data.py
└── README.md
```

## Maple Code

The Maple script uses `RegularChains:-SemiAlgebraicSetTools` for an exact real-root-counting certificate.

Maple version used for these certificates: **Maple 2024.0**.

- `localize_candidate_zero.mpl` certifies that the target rectangle contains exactly one common zero of the real and imaginary parts of `g(x+i y)`.

Expected final output:

```text
localize_candidate_zero.mpl: RealRootCounting output = 1
```

To run the Maple certificate manually from the repository root:

```bash
maple -q maple_code/localize_candidate_zero.mpl
```

## Notebooks

The notebooks provide exact rational certificate checks using Python's standard library only:

- `lemma4_exact_rational_certificate.ipynb` verifies the branch-selection / extraneous-root exclusion lemma.
- `condition_a_exact_rational_certificate.ipynb` verifies the stronger Rouché bound for condition (a).
- `lambda_nonreal_exact_rational_certificate.ipynb` verifies that the candidate eigenvalue from the plus-sign branch is nonreal.

All Python arithmetic is performed over `fractions.Fraction`. The code avoids floating-point arithmetic entirely. Modulus comparisons are reduced to squared rational inequalities whenever possible.

The expected output consists of `PASS: ...` messages. A failed certificate raises an exception.

## Python Version

The Python utilities use only the standard library and should work with Python 3.10 or later.

## Citation

If you use these certificates, please cite the associated paper:

> Yizhe Feng, Weiguo Gao, and Meiyue Shao,  
> *On Spurious Eigenvalues of High-Order Finite Difference Schemes for the Laplace Operator*.

If a journal reference, DOI, or arXiv link becomes available, it should be added here.
