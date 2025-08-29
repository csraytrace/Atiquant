# We'll parse the user's expression, extract roots, and plot the function.
import re
import numpy as np
import matplotlib.pyplot as plt

expr = "(x - 3.062144931715438e-06)*(x - -3.085719448288124e-06)*(x - -1.784357092634246e-06)*(x - 7.112593928313048e-07)*(x - -8.158627321816250e-07)*(x - -2.292826890970271e-06)*(x - 3.545908910029008e-06)*(x - -1.410892353148881e-07)*(x - -1.089949974155210e-08)*(x - -4.827531559920985e-06)*(x - 9.173299332250394e-07)*(x - -1.093115818573087e-06)*(x - -6.660329347045005e-07)*(x - 3.637242520163354e-06)*(x - -6.870860388790806e-07)*(x - 8.425240859225171e-08)*(x - 3.446383154651928e-06)"

# Extract roots of the form (x - r)
pattern = r'\(x\s*-\s*([+-]?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)\)'
root_strs = re.findall(pattern, expr)
roots = np.array([float(s) for s in root_strs], dtype=float)

print(roots)
# Build x-range around the roots
rmin, rmax = float(roots.min()), float(roots.max())
span = rmax - rmin
pad = 0.15 * span if span > 0 else 1e-6
x = np.linspace(rmin - pad, rmax + pad, 4000)

# Evaluate product polynomial
y = np.ones_like(x)
for r in roots:
    y = y * (x - r)

# Plot y vs x (linear scale)
plt.figure()
plt.plot(x, y)
plt.axhline(0)
plt.title("Produktfunktion f(x) = " + "⋯".join(["(x - r)"] * 3) + " …")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()

# Plot log10(|y|) to see structure
y_abs = np.abs(y)
y_abs[y_abs == 0] = np.finfo(float).tiny
logy = np.log10(y_abs)

plt.figure()
plt.plot(x, logy)
plt.title("log10(|f(x)|)")
plt.xlabel("x")
plt.ylabel("log10(|f(x)|)")
plt.grid(True)
plt.show()

# Print a quick summary
rmin, rmax, span, pad, len(roots)
