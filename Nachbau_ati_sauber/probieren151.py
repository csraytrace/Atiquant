from Nachbau_ati_sauber.Calc_I import Calc_I
import numpy as np
from Nachbau_ati_sauber.Element import Element
from Nachbau_ati_sauber.packages.Funktionen_Calc_I import *
import re



Elemente = [(0,"O"),(12,"si"), (55,"cu")]
Übergänge = [0,0,0]

Verteilung = [1]


Konzentration = []
P1 = []
for i in Elemente:
    Konzentration.append(i[0])
    P1.append(i[1])



Ki = Calc_I(Konzentration=Konzentration, P1=P1, Übergänge=Übergänge, Messzeit=30, Emax=30, step = 0.01)


print(Ki.Residuen(np.array([18.53361483, 54.05293923, 27.41344593]),[1],17))
print(Ki.Residuen(np.array([30.,29., 34. ]),[1],17))
print(Ki.Residuen(np.array([2.,5., 8.]),[1],17))


print(Ki.ResiduenEinfach(np.array([2.,5., ]),[1],17,2,8))
print(Ki.ResiduenEinfach(np.array([30.,29. ]),[1],17,2,34))



#op_Konz,op_Geo = Ki.Minimierung_dark(17, Verteilung)
#print(Ki.Minimierung_dark(17, Verteilung))
#print(Ki.Intensität_alle_jit_fürMinimierung(op_Konz)[0]*op_Geo)
#print(Ki.Atiquant())
