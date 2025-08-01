from Nachbau_ati_sauber.Calc_I import Calc_I
import numpy as np
from Nachbau_ati_sauber.Element import Element
from Nachbau_ati_sauber.packages.Funktionen_Calc_I import *
import re


#Z
#24.482182138686074
#21.188896476645528
#32.62505141737517

Ver=("1.04 C38H76N2O2 + 1 Ce1O2 + 0.84 Zn1O1 + 1.06 Cr2O3 + 0.98 Ti1O2 + 0.6 Al2O3")
#Ver=("1 Cu1 + 1 Zn1")
ele_soil,kon_soil,z_soil = (Verbindungen_Gewichtsprozent_vonMassenprozent(Ver))
print(ele_soil,np.array(kon_soil)*100, z_soil)



Elemente = [(0,"H"), (0,"C"), (0,"N"),(0,"O"),(1401, 'Al'), (31881, 'Ti'), (56833, 'Cr'), (99343, 'Zn'), (21562, 'Ce')]
Übergänge = [0,0,0,0,0,    0, 0, 0, 1]

Verteilung = [0,0,0,1]


Konzentration = []
P1 = []
for i in Elemente:
    Konzentration.append(i[0])
    P1.append(i[1])



Ki = Calc_I(Konzentration=Konzentration, P1=P1, Übergänge=Übergänge, Röhrenstrom=0.01, Messzeit=500, Emax=40, Kontaktmaterialdicke=2.99882970e+01, Totschicht=8.56937060e-11, sigma=8.30349567e-01,charzucont_L=0.3,charzucont=9.46173852e-01)

#Startkonzentration=np.array([15, 13,  14,14.4, 16])
###op_Konz=np.array([40, 13,  14,14.4, 16])
op_Konz=np.array([40, 12,  14.5,14.4, 16.5])
op_Geo=4.6*10e-6
Start = np.append(op_Konz, op_Geo)
Start = op_Konz
Start=Start.tolist()



op_Konz, op_Geo = Ki.Minimierung_dark( Z_mittelwert=21.47,low_verteilung=Verteilung,binder=[[4.48,1.04],["1C38H76N2O2"]], latex=True)    #,low_verteilung_volumenprozent=True,
print(Konzentration)
print(P1)
print((Ki.Intensität_alle_jit_fürMinimierung(op_Konz)[0]*op_Geo))




#op_Konz, op_Geo = Ki.Minimierung_dark( Z_mittelwert=22.8,low_verteilung=Verteilung,binder=[[3.88,1],["1C38H76N2O2"]])    #,low_verteilung_volumenprozent=True,
#print(Konzentration)
#print(P1)
#print((Ki.Intensität_alle_jit_fürMinimierung(op_Konz)[0]*op_Geo))






