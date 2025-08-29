from Nachbau_ati_sauber.Element import Element
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def Z_ber(a,b,x):
    return (x/a)**(1/b)
def power_law(x, a, b):
    return a * np.power(x, b)

x = list(range(2, 31))  # Ordnungszahlen 1 bis 100
Energie=20.2    #oder Emax? (oder Röhrenspek)

print(x)

data = [
443.53691517902,
46.59629434217225,
15.924916608251612,
10.282781464138203,
7.405802739489465,
5.292824681420467,
4.933044284795231,
4.2315828278609215,
3.8096573417240522,
3.6422004054505517,
3.5676772037736706,
3.3667892798155714,
2.434179388172177,
1.888668544643762,
1.4707290817259857,
1.2399643546372285,
1.0450635115221827,
0.9248568313608383,
0.8280079271998009,
0.7444132896518968,
0.7187934676717527,
0.6495745615155007,
0.5914125887674707,
0.5885695802327504,
0.5685563391902734,
0.5408630390224256,
0.49874874579892553,
0.46465784718194697,
0.4753644348562404



]

arr = np.array(data)



R= arr


# Curve Fit durchführen
popt, pcov = curve_fit(power_law, x[0:10], R[0:10], p0=[200, -2])  # p0 = Startwerte für a, b

a_fit, b_fit = popt
print(f"Gefundene Parameter: a = {a_fit:.3f}, b = {b_fit:.3f}")

# Fit-Kurve berechnen
x_fit = np.linspace(min(x), max(x), 100)
y_fit = power_law(x_fit, a_fit, b_fit)

# Plotten
plt.scatter(x, R, label="Daten", color="red")
plt.plot(x_fit, y_fit, label=f"Fit: $y = {a_fit:.2f} \cdot x^{{{b_fit:.2f}}}$")



plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


