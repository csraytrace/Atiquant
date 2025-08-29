from Nachbau_ati_sauber.Calc_I import Calc_I
import numpy as np
from Nachbau_ati_sauber.Element import Element
from Nachbau_ati_sauber.packages.Funktionen_Calc_I import *
import re


#Z
#12.142098048608489
#11.50987415793951
#9.56354727039737

Ver=("1 C38H76N2O2 + 2.34 Si1O2 + 2.33 Ti1O2")
#Ver=("1 Cu1 + 1 Zn1")
ele_soil,kon_soil,z_soil = (Verbindungen_Gewichtsprozent_vonMassenprozent(Ver))
print(ele_soil,np.array(kon_soil)*100, z_soil)



Elemente = [(0,"H"), (0,"C"), (0,"N"),(0,"O"),(8785, 'Si'), (98652, 'Ti')]
Übergänge = [0,0,0,0,    0,0]

Verteilung = [0,0,0,1]


Konzentration = []
P1 = []
for i in Elemente:
    Konzentration.append(i[0])
    P1.append(i[1])



Ki = Calc_I(Konzentration=Konzentration, P1=P1, Übergänge=Übergänge, Röhrenstrom=0.01, Messzeit=500, Emax=40, Kontaktmaterialdicke=2.99882970e+01, Totschicht=8.56937060e-11, sigma=8.30349567e-01,charzucont_L=0.3,charzucont=9.46173852e-01,step=0.01)


#op_Konz, op_Geo = Ki.Minimierung_dark( Z_mittelwert=12.1,low_verteilung=Verteilung,binder=[[4.67,1],["1C38H76N2O2"]], latex=True)    #,low_verteilung_volumenprozent=True,
print(Konzentration)
print(P1)
#print(("berechneteIntNormal",Ki.Intensität_alle_jit_fürMinimierung(op_Konz)[0]*op_Geo))
op_Konz,op_Geo = Ki.Minimierung_dark_einfach( Z_mittelwert=12.1,low_verteilung=Verteilung,binder=[[4.67,1],["1C38H76N2O2"]])


print("berechneteIntEinfach",Ki.Intensität_alle_jit_fürMinimierung(op_Konz)[0]*op_Geo)









