from Nachbau_ati_sauber.Calc_I import Calc_I
import numpy as np
from Nachbau_ati_sauber.Element import Element
from Nachbau_ati_sauber.packages.Funktionen_Calc_I import *
import re

Ver="10 H1 + 6 C1 + 1 N1 + 5 O1"
Ver="10 H1 + 6 C1 + 0 N1 + 5 O1"



Ver=("1 C38H76N2O2 + 2.08 Si1O2 + 2.07 Ti1O2")
#Ver=("1 Cu1 + 1 Zn1")
ele_soil,kon_soil,z_soil = (Verbindungen_Gewichtsprozent_vonMassenprozent(Ver))
print(ele_soil,kon_soil, z_soil)
