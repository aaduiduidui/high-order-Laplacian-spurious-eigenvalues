"""
Exact rational arithmetic utilities for the certificate notebooks.

This module intentionally contains only reusable tools/classes.  The actual
mathematical verification of the two lemmas is performed in the notebooks.

Design principles
-----------------
1. All real quantities are represented by fractions.Fraction.
2. Complex quantities are represented by RationalComplex.
3. No floating-point arithmetic is used.
4. All exponentiation used in the certificates is integer exponentiation.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, List, Sequence


def frac(num=0, den=None) -> Fraction:
    """Create a Fraction, rejecting floats to avoid accidental inexact input."""
    if isinstance(num, float) or isinstance(den, float):
        raise TypeError("Do not construct exact certificates from float literals.")
    if den is None:
        return Fraction(num)
    return Fraction(num, den)


@dataclass(frozen=True)
class RationalComplex:
    """A complex number with rational real and imaginary parts."""

    re: Fraction = Fraction(0)
    im: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        if isinstance(self.re, float) or isinstance(self.im, float):
            raise TypeError("RationalComplex entries must not be floats.")
        object.__setattr__(self, "re", Fraction(self.re))
        object.__setattr__(self, "im", Fraction(self.im))

    def __add__(self, other) -> "RationalComplex":
        other = as_rational_complex(other)
        return RationalComplex(self.re + other.re, self.im + other.im)

    def __radd__(self, other) -> "RationalComplex":
        return self + other

    def __sub__(self, other) -> "RationalComplex":
        other = as_rational_complex(other)
        return RationalComplex(self.re - other.re, self.im - other.im)

    def __rsub__(self, other) -> "RationalComplex":
        return as_rational_complex(other) - self

    def __neg__(self) -> "RationalComplex":
        return RationalComplex(-self.re, -self.im)

    def __mul__(self, other) -> "RationalComplex":
        other = as_rational_complex(other)
        return RationalComplex(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def __rmul__(self, other) -> "RationalComplex":
        return self * other

    def __truediv__(self, other) -> "RationalComplex":
        other = as_rational_complex(other)
        return self * other.inv()

    def __rtruediv__(self, other) -> "RationalComplex":
        return as_rational_complex(other) / self

    def __pow__(self, n: int) -> "RationalComplex":
        """Exact integer powers only."""
        if not isinstance(n, int):
            raise TypeError("Only integer powers are supported in this certificate.")
        if n < 0:
            return self.inv() ** (-n)
        out = RationalComplex(1, 0)
        base = self
        k = n
        while k:
            if k & 1:
                out = out * base
            base = base * base
            k >>= 1
        return out

    def conj(self) -> "RationalComplex":
        return RationalComplex(self.re, -self.im)

    def norm2(self) -> Fraction:
        """Return |z|^2 exactly."""
        return self.re * self.re + self.im * self.im

    def inv(self) -> "RationalComplex":
        n2 = self.norm2()
        if n2 == 0:
            raise ZeroDivisionError("division by zero in RationalComplex")
        return RationalComplex(self.re / n2, -self.im / n2)

    def __repr__(self) -> str:
        return f"RationalComplex(re={self.re}, im={self.im})"


def as_rational_complex(z) -> RationalComplex:
    if isinstance(z, RationalComplex):
        return z
    if isinstance(z, float):
        raise TypeError("Do not coerce floats into RationalComplex.")
    return RationalComplex(Fraction(z), Fraction(0))


def require(name: str, condition: bool) -> None:
    """Certificate assertion, not disabled by Python optimization flags."""
    if not condition:
        raise AssertionError(f"FAILED: {name}")
    print(f"PASS: {name}")


# ---------------------------------------------------------------------------
# Polynomial utilities
# ---------------------------------------------------------------------------

def trim(poly: Sequence[Fraction]) -> List[Fraction]:
    out = [Fraction(a) for a in poly]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def poly_from_terms(terms: Dict[int, int | Fraction]) -> List[Fraction]:
    """Convert {degree: coefficient} into ascending coefficient order."""
    if not terms:
        return [Fraction(0)]
    deg = max(terms)
    out = [Fraction(0) for _ in range(deg + 1)]
    for k, v in terms.items():
        if isinstance(v, float):
            raise TypeError("Polynomial coefficients must not be floats.")
        out[k] = Fraction(v)
    return trim(out)


def poly_add(p: Sequence[Fraction], q: Sequence[Fraction]) -> List[Fraction]:
    n = max(len(p), len(q))
    out = [Fraction(0) for _ in range(n)]
    for i in range(n):
        out[i] = (p[i] if i < len(p) else Fraction(0)) + (q[i] if i < len(q) else Fraction(0))
    return trim(out)


def poly_sub(p: Sequence[Fraction], q: Sequence[Fraction]) -> List[Fraction]:
    n = max(len(p), len(q))
    out = [Fraction(0) for _ in range(n)]
    for i in range(n):
        out[i] = (p[i] if i < len(p) else Fraction(0)) - (q[i] if i < len(q) else Fraction(0))
    return trim(out)


def poly_mul(p: Sequence[Fraction], q: Sequence[Fraction]) -> List[Fraction]:
    out = [Fraction(0) for _ in range(len(p) + len(q) - 1)]
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += Fraction(a) * Fraction(b)
    return trim(out)


def poly_eval(poly: Sequence[Fraction], z: RationalComplex) -> RationalComplex:
    """Evaluate p(z)=sum_k poly[k] z^k exactly by Horner's rule."""
    z = as_rational_complex(z)
    acc = RationalComplex(0, 0)
    for a in reversed(poly):
        acc = acc * z + RationalComplex(a, 0)
    return acc


def derivative_majorant(poly: Sequence[Fraction], R: Fraction) -> Fraction:
    """Return sum_{k>=1} |a_k| k R^{k-1}."""
    R = Fraction(R)
    total = Fraction(0)
    for k, a in enumerate(poly):
        if k >= 1 and a != 0:
            total += abs(Fraction(a)) * k * (R ** (k - 1))
    return total


def polynomial_perturbation_bound(poly: Sequence[Fraction], delta: Fraction, R: Fraction) -> Fraction:
    """If |z-w|<=delta and |z|,|w|<=R, bound |p(z)-p(w)|."""
    return Fraction(delta) * derivative_majorant(poly, Fraction(R))


# ---------------------------------------------------------------------------
# Rectangle and comparison utilities
# ---------------------------------------------------------------------------

def rectangle_distance_bound(xL: Fraction, xU: Fraction, yL: Fraction, yU: Fraction,
                             center: RationalComplex, delta: Fraction) -> bool:
    """Verify every corner of the rectangle is within distance delta of center."""
    delta2 = Fraction(delta) * Fraction(delta)
    for x in (xL, xU):
        for y in (yL, yU):
            dx = Fraction(x) - center.re
            dy = Fraction(y) - center.im
            if dx * dx + dy * dy > delta2:
                return False
    return True


def rectangle_modulus_bound(xL: Fraction, xU: Fraction, yL: Fraction, yU: Fraction,
                            R: Fraction) -> bool:
    """Verify every corner of the rectangle lies in |z|<=R."""
    R2 = Fraction(R) * Fraction(R)
    for x in (xL, xU):
        for y in (yL, yU):
            if Fraction(x) * Fraction(x) + Fraction(y) * Fraction(y) > R2:
                return False
    return True


def im_div_numerator(A: RationalComplex, B: RationalComplex) -> Fraction:
    """Return numerator of Im(A/B): Im(A/B)=(A.im*B.re-A.re*B.im)/|B|^2."""
    return A.im * B.re - A.re * B.im


def square_less_than_norm2(bound: Fraction, z: RationalComplex) -> bool:
    """Check bound^2 < |z|^2 exactly, without taking square roots."""
    bound = Fraction(bound)
    return bound * bound < z.norm2()


def norm2_less_than_square(z: RationalComplex, bound: Fraction) -> bool:
    """Check |z|^2 < bound^2 exactly, without taking square roots."""
    bound = Fraction(bound)
    return z.norm2() < bound * bound
