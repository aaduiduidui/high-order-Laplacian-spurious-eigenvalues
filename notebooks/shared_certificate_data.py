"""
Data shared by the two certificate notebooks.

The notebooks remain the only verification scripts.  This file only stores
polynomial data and exact rational constants used by both notebooks.
"""

from fractions import Fraction

from rational_tools import RationalComplex as CQ, poly_from_terms, poly_mul, poly_sub

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


# f6 and f7 for lambda* = f6(s0*) / f7(s0*).
# Here f7 includes the scaling factor 180, so lambda* is the eigenvalue of L.
f6 = poly_from_terms({
    15: 64,
    14: 12640,
    13: 464928,
    12: -16178896,
    11: 47914340,
    10: 5454430,
    9: -156127576,
    8: 357613692,
    7: -182559273,
    6: 1201642441,
    5: -636151748,
    4: -31972716,
    3: 21662864,
    2: -371152,
    1: -12224,
    0: -64,
})

f7 = poly_from_terms({
    14: 5760,
    13: -273600,
    12: 2844000,
    11: 7274160,
    10: -102530880,
    9: 92052000,
    8: 289301760,
    7: -519419520,
    6: 400123800,
    5: 273316680,
    4: -23352480,
    3: -3576960,
    2: 311040,
    1: -5760,
})