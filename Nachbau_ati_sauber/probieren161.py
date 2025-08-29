import numpy as np
import matplotlib.pyplot as plt


def g(x):
    return abs(0.9263909163385223)*((x - 25.19196900066341)/(-3.089013320898953))*((x - 4.507980015896446)/(17.59497566386801))*((x - 23.10792994876348)/(-1.004974268999025)) + (1.087038793472508)*((x - 22.10295567976446)/(3.089013320898953))*((x - 4.507980015896446)/(20.68398898476696))*((x - 23.10792994876348)/(2.084039051899929)) + (1.048549186883834)*((x - 22.10295567976446)/(-17.59497566386801))*((x - 25.19196900066341)/(-20.68398898476696))*((x - 23.10792994876348)/(-18.59994993286703)) + (0.9818783769613152)*((x - 22.10295567976446)/(1.004974268999025))*((x - 25.19196900066341)/(-2.084039051899929))*((x - 4.507980015896446)/(18.59994993286703))


# Wertebereich wählen (z. B. 0 bis 30)
x = np.linspace(0, 25, 2000)
yfkt = g(x)

xeinfach=[22.1030, 25.1920, 4.50798, 23.1079]
yeinfach=[4.16001e-05, 3.54522e-05, 3.67536e-05, 3.92492e-05]
yeinfach = np.array(yeinfach)
for index, i in enumerate(xeinfach):
    yeinfach[index]*= g(i)

print(yeinfach)
# Plot
plt.figure(figsize=(10,6))
plt.axhline(0, color="black", linewidth=0.8)
plt.scatter(xeinfach, yeinfach, color="red", marker="o", s=50, label="Datenpunkte")
#plt.plot(x, yfkt, label="g(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Plot der gegebenen Funktion")
plt.legend()
plt.grid(True)
plt.show()
