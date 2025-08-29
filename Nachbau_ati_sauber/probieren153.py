from Nachbau_ati_sauber.Calc_I import Calc_I
import numpy as np
from Nachbau_ati_sauber.Element import Element
from Nachbau_ati_sauber.packages.Funktionen_Calc_I import *
import re


Elemente = [(0,"O"),(1,"si"), (12,"cu"),(11,"ca"),(14,"K"),(16,"Ni")]
Übergänge = [0,0,0 ,0,0,0]

Verteilung = [1]


Konzentration = []
P1 = []
for i in Elemente:
    Konzentration.append(i[0])
    P1.append(i[1])



Ki = Calc_I(Konzentration=Konzentration, P1=P1, Übergänge=Übergänge, Messzeit=30, Emax=30, step = 0.01)



op_Konz,op_Geo = Ki.Minimierung_dark(20, Verteilung)
#print(Ki.Minimierung_dark(17, Verteilung))
#print(Ki.Intensität_alle_jit_fürMinimierung(op_Konz)[0]*op_Geo)

print(Ki.Minimierung_dark_einfach(20, Verteilung))
#print(Ki.Atiquant())



