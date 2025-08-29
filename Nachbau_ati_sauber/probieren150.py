from Nachbau_ati_sauber.packages.Funktionen_Calc_I import *
import numpy as np

konz_low=np.array([1,1])
konz_high=np.array([3,3])
z_low=np.array([6,8])
z_high=np.array([14,20])
z_gewünscht=10

#print(Z_anpassen(konz_low, z_low, konz_high, z_high, z_gewünscht))

x,y = Z_anpassen(konz_low, z_low, konz_high, z_high, z_gewünscht)

print(x,y)
print("konz")
print(konz_low*x)
print(konz_high*y)

start= np.concatenate([konz_low, konz_high])
start = start / start.sum()
gesamt_konz = np.concatenate([konz_low*x, konz_high*y])

# Normieren
gesamt_konz_norm = gesamt_konz / gesamt_konz.sum()

print("Neue, unnormierte Konzentrationen:", gesamt_konz)
print("Neue, normierte Konzentrationen:", gesamt_konz_norm)
print((np.concatenate([z_low, z_high])*gesamt_konz_norm).sum())
print("start",(start*np.concatenate([z_low, z_high])).sum())

