import numpy as np
import matplotlib.pyplot as plt
from Nachbau_ati_sauber.Element import Element
from Nachbau_ati_sauber.Detektor import Detektor
from Nachbau_ati_sauber.Röhre import Röhre

# --- Daten holen ---
F = Element(Element="Cu")
D = Detektor()
T = Röhre()

# Erwartet: (E, μ/ρ(E)) in cm^2/g  und  (E, Det(E))
xF, mu_mass = map(lambda a: np.asarray(a, float).ravel(), F.Massenschwächungskoeffizient_array())
xD, det_y   = map(lambda a: np.asarray(a, float).ravel(), D.Detektorspektrum())
xT, tube_y = map(lambda a: np.asarray(a, float).ravel(), T.Röhrenspektrum)

# --- Beer–Lambert: μ/ρ -> Transmission ---
rho_g_cm3    = 8.96     # Dichte (Beispiel: Cu)
thick_cm     = 0.010    # Dicke in cm (100 µm = 0.010 cm)
areal_g_cm2  = rho_g_cm3 * thick_cm
T_F          = np.exp(-mu_mass * areal_g_cm2)  # T(E) = exp(-(μ/ρ)*ρ*d)

print(T_F)
# --- Punktweise multiplizieren ---
y_prod = T_F * det_y

y_prod2 = T_F * tube_y

# --- Plot ---
plt.figure(figsize=(9,5))
plt.plot(xF, T_F,    label="Filter T(E)")
plt.plot(xD, det_y,  label="Det(E)")
plt.plot(xD, y_prod, label="T(E) × Det(E)", linewidth=2)
plt.xlabel("Energie"); plt.ylabel("Wert"); plt.title("Filter × Detektor")
plt.legend(); plt.tight_layout(); plt.show()

plt.figure(figsize=(9,5))
plt.plot(xF, T_F,    label="Filter T(E)")
plt.plot(xD, tube_y,  label="Röhre(E)")
plt.plot(xD, y_prod2, label="T(E) × Röhre(E)", linewidth=2)
plt.xlabel("Energie"); plt.ylabel("Wert"); plt.title("Filter × Röhre")
plt.legend(); plt.tight_layout(); plt.show()
