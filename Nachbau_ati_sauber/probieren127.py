from Nachbau_ati_sauber.Element import Element
import numpy as np
from Nachbau_ati_sauber.Calc_I import Calc_I#ohne al, si
from Nachbau_ati_sauber.Geoplot_klasse import Plot_einfach
import matplotlib.pyplot as plt

Elemente = [(140000, 'Ag'), (66746, 'SN'), (163000, 'TI'), (111267, 'CD'), (433090, 'CU'), (196370, 'V'), (544606, 'ZR')
, (464025, 'ZN'), (498315, 'GE'), (10844, 'AL'), (20692, 'SI'), (106785, 'BI'), (13396, 'CD'), (17196, 'SN'), (109041, 'PB'), (82738, 'TA'),(13240, 'Ag')]

Übergänge = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1]


kal_dat = []

for index, i in enumerate(Elemente):
    kal_dat.append([i[1], i[0], Übergänge[index]])
print(kal_dat)

elemente = [entry[0] for entry in kal_dat]
intensität = [entry[1] for entry in kal_dat]
print(elemente,Übergänge)

x_data=[]
y_data_scipy=[]
y_data_boby=[]
y_data_lm=[]
y_data_lm_scipy=[]

for kal in kal_dat:
    x_ele=Element(Element=kal[0])
    if kal[2]==0:
        x_data.append(x_ele.K_gemittel_ubergang())
    else:
        x_data.append(x_ele.L_gemittel_ubergang())



#for kal in kal_dat:
#    Ki = Calc_I(Konzentration=[1], P1=[kal[0]], Übergänge=[kal[2]], Einfallswinkelalpha=15, activeLayer=2.06872613, Totschicht=8.54277948e-04, charzucont_L=2.02373175e-01,
 #               charzucont=8.12735451e-01,Emax=4.49994894e+01,Kontaktmaterialdicke=3.98246503e+01)
  #  print(kal[1]/Ki.Intensität_alle_jit_fürMinimierung([1])[0][0], kal[0])
  #  y_data_scipy.append(kal[1]/(Ki.Intensität_alle_jit_fürMinimierung([1])[0][0]))


#python verwendet
for kal in kal_dat:
    Ki = Calc_I(Konzentration=[1], P1=[kal[0]], Übergänge=[kal[2]], Einfallswinkelalpha=15, activeLayer=2.06872613, Totschicht=8.56937060e-11, charzucont_L=0.3,
                charzucont=9.46173852e-01,Emax=40,Kontaktmaterialdicke=2.99882970e+01,sigma=8.30349567e-01)
    print(kal[1]/Ki.Intensität_alle_jit_fürMinimierung([1])[0][0], kal[0])
    y_data_scipy.append(kal[1]/(Ki.Intensität_alle_jit_fürMinimierung([1])[0][0]))




#boby random start
  #  Ki = Calc_I(Konzentration=[1], P1=[kal[0]], Übergänge=[kal[2]], Einfallswinkelalpha=19.464, activeLayer=3.141, Totschicht=0.2, charzucont_L=0.6457124120834289,
       #     charzucont=0.9891660,Emax=44.974,Kontaktmaterialdicke=25.6966503e+01)
#for kal in kal_dat:
   # Ki = Calc_I(Konzentration=[1], P1=[kal[0]], Übergänge=[kal[2]], Einfallswinkelalpha=15, activeLayer=3.21, Totschicht=0.0, charzucont_L=0.1,
   #             charzucont=1.078,Emax=44.97,Kontaktmaterialdicke=40)
  #  print(Ki.Intensität_alle_jit_fürMinimierung([1])[0][0])
  #  y_data_boby.append(kal[1]/(Ki.Intensität_alle_jit_fürMinimierung([1])[0][0]))




#for kal in kal_dat:
  #  Ki = Calc_I(Konzentration=[1], P1=[kal[0]], Übergänge=[kal[2]], Einfallswinkelalpha=15.082467912854321, activeLayer=2.8983779494032844,
  ##              Totschicht=0.11260379595056184, charzucont_L=0.1,
  #              charzucont=1.046154234152701,Emax=44.95743450053233,Kontaktmaterialdicke=10.792558496328677)
  #  print(Ki.Intensität_alle_jit_fürMinimierung([1])[0][0], kal[0])
 #   y_data_boby.append(kal[1]/(Ki.Intensität_alle_jit_fürMinimierung([1])[0][0]))


#for kal in kal_dat:
    #Ki = Calc_I(Konzentration=[1], P1=[kal[0]], Übergänge=[kal[2]], Einfallswinkelalpha=20.3249876386949,Einfallswinkelbeta=90-20.3249876386949, activeLayer=2.512950718140293,
     #           Totschicht=0, charzucont_L=0.1,sigma=0.8000015580225123,
    #            charzucont=0.8159733899831029,Emax=40,Kontaktmaterialdicke=24.838486060956864)
   # print(kal[1]/Ki.Intensität_alle_jit_fürMinimierung([1])[0][0], kal[0])
   # y_data_boby.append(kal[1]/(Ki.Intensität_alle_jit_fürMinimierung([1])[0][0]))

#verwendet boby
for kal in kal_dat:
    Ki = Calc_I(Konzentration=[1], P1=[kal[0]], Übergänge=[kal[2]], Einfallswinkelalpha=20.3249876386949,Einfallswinkelbeta=90-20.3249876386949, activeLayer=2.512950718140293,
                Totschicht=0, charzucont_L=0.1,sigma=0.8000015580225123,
                charzucont=0.8159733899831029,Emax=40,Kontaktmaterialdicke=24.838486060956864)
    print(kal[1]/Ki.Intensität_alle_jit_fürMinimierung([1])[0][0], kal[0])
    y_data_boby.append(kal[1]/(Ki.Intensität_alle_jit_fürMinimierung([1])[0][0]))



#for kal in kal_dat:
 #   Ki = Calc_I(Konzentration=[1], P1=[kal[0]], Übergänge=[kal[2]], Einfallswinkelalpha=15, activeLayer=2.993489938788493, Totschicht=0.0, charzucont_L=1.1997371366790963,
 #               charzucont=0.949251062884446,Emax=44.87403458252088,Kontaktmaterialdicke=10.0)
#    print(Ki.Intensität_alle_jit_fürMinimierung([1])[0][0])
#    y_data_boby.append(kal[1]/(Ki.Intensität_alle_jit_fürMinimierung([1])[0][0]))

#for kal in kal_dat:
  #  Ki = Calc_I(Konzentration=[1], P1=[kal[0]], Übergänge=[kal[2]], Einfallswinkelalpha=15, activeLayer= 2.9229864656423263, Totschicht=0.0, charzucont_L=1.2,
  #              charzucont=0.95,Emax=45,Kontaktmaterialdicke=14.442617636447068)
 #   print(Ki.Intensität_alle_jit_fürMinimierung([1])[0][0])
 #   y_data_lm.append(kal[1]/(Ki.Intensität_alle_jit_fürMinimierung([1])[0][0]))

#for kal in kal_dat:
  #  Ki = Calc_I(Konzentration=[1], P1=[kal[0]], Übergänge=[kal[2]], Einfallswinkelalpha=-30.48201104, activeLayer= 2.81941896, Totschicht=0.5695597, charzucont_L=-2.67399482,
  #              charzucont=1.09349746,Emax=45.66091736,Kontaktmaterialdicke=-9.49609831)
#    print(Ki.Intensität_alle_jit_fürMinimierung([1])[0][0])
#    y_data_lm_scipy.append(kal[1]/(Ki.Intensität_alle_jit_fürMinimierung([1])[0][0]))


#for kal in kal_dat:
 #   Ki = Calc_I(Konzentration=[1], P1=[kal[0]], Übergänge=[kal[2]], Einfallswinkelalpha=4.666493320690118, activeLayer= 1.5491262717716114, Totschicht=-5.666609973797417, charzucont_L=1.2,
 #               charzucont=0.95,Emax=49.47407058487551,Kontaktmaterialdicke=125.8230963435906)
 #   print(Ki.Intensität_alle_jit_fürMinimierung([1])[0][0])
 #   y_data_lm2.append(kal[1]/(Ki.Intensität_alle_jit_fürMinimierung([1])[0][0]))







for i in range(2):

   # Plot_einfach([x_data,y_data_lm,elemente], xy_format=True).plot_scatter(ylabel="lm",abweichung=True)
   # plt.show()


    Plot_einfach([x_data,y_data_boby,elemente], xy_format=True).plot_scatter(ylabel="boby",abweichung=True)
    plt.show()


    Plot_einfach([x_data,y_data_scipy,elemente], xy_format=True).plot_scatter(ylabel="Scipy",abweichung=True)
    plt.show()

  #  Plot_einfach([x_data,y_data_lm_scipy,elemente], xy_format=True).plot_scatter(ylabel="Scipy_lm",abweichung=True)
   # plt.show()








#Scipy
#[1.50000000e+01 2.06872613e+00 8.54277948e-04 2.02373175e-01
 #8.12735451e-01 4.49994894e+01 3.98246503e+01]

"""
Startwerte=[15,3,0,1.2,0.95,45,10]

Optimierte Parameter (BOBYQA):
Einfallswinkelalpha = 15.0
activeLayer = 2.993489938788493
Totschicht = 0.0
charzucont_L = 1.1997371366790963
charzucont = 0.949251062884446
Emax = 44.87403458252088
Kontaktmaterialdicke = 10.0



Optimierte Parameter (LM):
Einfallswinkelalpha = 15.0
activeLayer = 2.9229864656423263
Totschicht = 0.0
charzucont_L = 1.2
charzucont = 0.95
Emax = 45.0
Kontaktmaterialdicke = 14.442617636447068

"""
