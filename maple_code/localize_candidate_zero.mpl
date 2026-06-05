# localize_candidate_zero.mpl
# Purpose: certify that the rectangle I contains exactly one common zero
#          of g_R(x,y) and g_I(x,y), where g_R+i g_I = g(x+i y).
# Maple version used by the authors: Maple 2024.0
# Expected final output: 1

restart:
with(RegularChains):
with(RegularChains:-SemiAlgebraicSetTools):

# Real variables: s0 = x + I*y.
R := PolynomialRing([x,y]):

# Univariate polynomial g(z) from the paper.
g := z ->
    149120*z^19
  + 194192832*z^18
  + 82027451488*z^17
  - 430493413392*z^16
  + 1513738384232*z^15
  - 3581184876460*z^14
  + 8434713321906*z^13
  - 12701597216051*z^12
  - 82611517277291*z^11
  + 274946173437226*z^10
  + 41939474247020*z^9
  - 588919414498034*z^8
  + 857422100242584*z^7
  + 125502290312144*z^6
  + 5962472764256*z^5
  + 143684505600*z^4
  + 2023787392*z^3
  + 17621248*z^2
  + 71168*z
  + 512:

# Define g_R and g_I by exact symbolic expansion.
gxy := expand(g(x + I*y)):
gR  := expand(evalc(Re(gxy))):
gI  := expand(evalc(Im(gxy))):

# The rectangular interval I:
#   x in [160734/10^9, 160735/10^9],
#   y in [-6419166/10^9, -6419165/10^9].
# All endpoints are encoded by integer polynomial inequalities.
s0_real_lb := 10^9*x - 160734:
s0_real_ub := -10^9*x + 160735:
s0_imag_lb := 10^9*y + 6419166:
s0_imag_ub := -10^9*y - 6419165:

F := [gR, gI]:
N := []:
P := [s0_real_lb, s0_real_ub, s0_imag_lb, s0_imag_ub]:
H := []:

ans := RealRootCounting(F, N, P, H, R):
printf("RealRootCounting output = %a\n", ans):
printf("Expected output = 1\n"):

if ans <> 1 then
    error "Localization certificate failed: expected exactly one root in I";
end if:

printf("PASS: the rectangle I contains exactly one common zero of g_R and g_I.\n"):
