"""
Data shared by the two certificate notebooks.

The notebooks remain the only verification scripts.  This file only stores
polynomial data and exact rational constants used by both notebooks.
"""

from fractions import Fraction

from exact_rational import RationalComplex as CQ, poly_from_terms, poly_mul, poly_sub

# Rectangle I for the selected candidate root.
xL = Fraction(160734, 10**9)
xU = Fraction(160735, 10**9)
yL = Fraction(-6419166, 10**9)
yU = Fraction(-6419165, 10**9)

# Corner point used as rational approximation and simple rational overestimates.
s_hat = CQ(xL, yU)
delta = Fraction(2, 10**9)
R = Fraction(1, 100)

# f1(z)=2z^2-27z-2
f1 = poly_from_terms({0: -2, 1: -27, 2: 2})

# f2(z)=2z^2+27z-2
f2 = poly_from_terms({0: -2, 1: 27, 2: 2})

# f3(z)=4z^4-108z^3-1439z^2-108z+4
f3 = poly_from_terms({0: 4, 1: -108, 2: -1439, 3: -108, 4: 4})

f4 = poly_from_terms({
    16: -8192,
    15: 499712,
    14: -7077888,
    13: -31111168,
    12: 659681792,
    11: -326163456,
    10: -5979808768,
    9: 7396888576,
    8: 3606093312,
    7: -22677711616,
    6: 2524591872,
    5: 1298253312,
    4: -54335488,
    3: -8839168,
    2: 552960,
    1: -8192,
})

f5 = poly_from_terms({
    14: -4096,
    13: 194560,
    12: -2022400,
    11: -5172736,
    10: 72910848,
    9: -65459200,
    8: -205725696,
    7: 369364992,
    6: -284532480,
    5: -194358528,
    4: 16606208,
    3: 2543616,
    2: -221184,
    1: 4096,
})

# Numerators for the rational forms of s1* and s2*:
#   s1* = N1(s0*)/(4 f5(s0*))
#   s2* = N2(s0*)/(4 s0* f5(s0*))
N1 = poly_sub(poly_mul(f1, f5), f4)
N2 = poly_sub(f4, poly_mul(f2, f5))
