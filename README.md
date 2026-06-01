# High-Order Laplacian Spurious Eigenvalues

This repository contains the exact rational certificates used for the two auxiliary lemmas in the paper *On Spurious Eigenvalues of High-Order Finite Difference Schemes for the Laplace Operator*.

## Structure

```text
exact_rational.py                         # reusable exact rational arithmetic tools/classes
certificate_data.py                       # shared polynomial data and rectangle constants
lemma4_exact_rational_certificate.ipynb   # verification of Lemma 4 only
condition_a_exact_rational_certificate.ipynb # verification of condition (a) only
```

The `.py` files do **not** perform the mathematical verification.  They only provide common classes, functions, polynomial data, and exact constants.  The two notebooks are the unique verification documents:

- `lemma4_exact_rational_certificate.ipynb` verifies the branch-selection / extraneous-root exclusion lemma.
- `condition_a_exact_rational_certificate.ipynb` verifies the stronger Rouché bound for condition (a).

## Exactness policy

All arithmetic is performed over `fractions.Fraction`. The code avoids floating-point arithmetic entirely.  Modulus comparisons are reduced to squared rational inequalities whenever possible.

## How to use

Open each notebook and run all cells from top to bottom.  The expected output consists of `PASS: ...` messages.  A failed certificate raises an exception.

## Python version

The utilities use only the Python standard library and should work with Python 3.10 or later.

<!-- ## Citation

If you use these notebooks, please cite the associated paper:

> Yizhe Feng, Weiguo Gao, and Meiyue Shao,  
> *On Spurious Eigenvalues of High-Order Finite Difference Schemes for the Laplace Operator*.

If a journal reference, DOI, or arXiv link becomes available, it should be added here. -->
