from Nachbau_ati_sauber.Element import Element
import numpy as np



print(Element(Element="42").Kanten())

for i in range(90):
    x_ele = Element(Element=str(i+1))
    inelas = x_ele.Massenschwächungskoeffizient(19.3)[1]
    elas = x_ele.Massenschwächungskoeffizient(20.2)[1]
    #print(elas)

    print(i+1,(inelas+elas)/(elas+elas))
