import numpy as np
import matplotlib.pyplot as plt
from Nachbau_ati_sauber.Element import Element
from Nachbau_ati_sauber.Detektor import Detektor
from Nachbau_ati_sauber.Röhre import Röhre

# --- Daten holen ---
F = Element(Element="Cu")
D = Detektor()
T = Röhre()

F.K_gemittel_ubergang()
print(F.K_gemittel_ubergang())
print(F.Ubergange())
print(F.Kanten())

H = Element(Element="H")
print(H.Ubergange())

# Erwartet: (E, μ/ρ(E)) in cm^2/g  und  (E, Det(E))
#xF, mu_mass = map(lambda a: np.asarray(a, float).ravel(), F.Massenschwächungskoeffizient_array())
mu_mass = F.Massenschwächungskoeffizient(20)
print(mu_mass)



for i in range(30):
    areal_g_cm2 = np.array(F.Get_Density()) * 0.01 * i
    T_F          = np.exp(-np.array(mu_mass[1]) * areal_g_cm2)
    print(T_F)


import numpy as np
mu = float(np.array(mu_mass[1]))        # [cm^2/g]
rho = float(np.array(F.Get_Density()))  # [g/cm^3]

T_target = 0.01                         # 99% absorbiert
x_cm = -np.log(T_target) / (mu * rho)   # gesuchte Dicke in cm

# Wenn du das i der Schleife (0.01 cm Schritte) willst:
i_exact = x_cm / 0.01
i_nearest = int(np.round(i_exact))      # nächstliegendes i
i_up = int(np.ceil(i_exact))            # garantiert T <= 0.01

print(f"x = {x_cm:.6g} cm, i_exact = {i_exact:.3f}, i≈{i_nearest}, i_ceiling={i_up}")

