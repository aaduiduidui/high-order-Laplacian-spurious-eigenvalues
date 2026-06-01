# Exact rational certificates

This repository fragment contains the exact rational certificates used for the two auxiliary lemmas in the paper.

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

All arithmetic is performed over `fractions.Fraction`.  Decimal endpoints are encoded as rational numbers such as `Fraction(160734, 10**9)`.  The code avoids floating-point arithmetic entirely.  Modulus comparisons are reduced to squared rational inequalities whenever possible.

## How to use

Open each notebook and run all cells from top to bottom.  The expected output consists of `PASS: ...` messages.  A failed certificate raises an exception.

## Python version

The utilities use only the Python standard library and should work with Python 3.10 or later.
