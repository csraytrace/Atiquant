# Plot der angegebenen stückweisen linearen Segmente
import numpy as np
import matplotlib.pyplot as plt

# Segmente: (a, b, m, c, inclA, inclB)
segments = [
    (1.48700000, 1.73933498, -0.659661941, 2.12412323, True,  False),
    (1.73933498, 2.98339082, -0.0472948995, 1.05901181, True,  False),
    (2.98339082, 3.13239081, 0.668951846,  -1.07783216, True,  False),
    (3.13239081, 3.44318779, -0.334069322,  2.06402213, True,  False),
    (3.44318779, 4.50798002, 0.126588512,   0.477890706,True,  False),
    (4.50798002, 4.94930454, 0.0333308449,  0.898294404,True,  False),
    (4.94930454, 8.04121575, -0.0134643765, 1.12989821, True,  False),
    (8.04121575, 8.13911110, -0.243215824,  2.97737916, True,  False),
    (8.13911110, 8.63118987, 0.0119004307,  0.900959622,True,  False),
    (8.63118987, 9.87646221, -0.00272357614,1.02718220, True,  False),
    (9.87646221, 10.5405621, 0.0269079223,  0.734527828,True,  False),
    (10.5405621, 10.8279481, 0.0384160932,  0.613225238,True,  False),
    (10.8279481, 15.7461512, -0.0230675441, 1.27896687, True,  False),
    (15.7461512, 22.1029557, 0.00167522596, 0.889363471,True,  False),
    (22.1029557, 23.1079299, 0.0552128172, -0.293975536,True,  False),
    (23.1079299, 25.1919690, 0.0504599069, -0.184145617,True,  True )
]

# Datenpunkte für eine einzige durchgehende Linie erzeugen
x_plot = []
y_plot = []
for i, (a,b,m,c,inclA,inclB) in enumerate(segments):
    if i == 0:
        x_plot.append(a)
        y_plot.append(m*a + c)
    x_plot.append(b)
    y_plot.append(m*b + c)

x_plot = np.array(x_plot)
y_plot = np.array(y_plot)

# Knoten (Segment-Endpunkte) für Scatter
x_knots = [segments[0][0]] + [seg[1] for seg in segments]
y_knots = [segments[0][2]*segments[0][0] + segments[0][3]] + [seg[2]*seg[1] + seg[3] for seg in segments]

plt.figure(figsize=(10,6))
plt.plot(x_plot, y_plot, label="stückweise linear")
plt.scatter(x_knots, y_knots, s=25, label="Knoten")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot der angegebenen Segmente")
plt.legend()
plt.grid(True)
plt.show()
