import numpy as np
import matplotlib.pyplot as plt

class DataPlotter:
    def __init__(self, xs, ys, labels=None):
        self.xs = np.array(xs)
        self.ys = np.array(ys)
        self.labels = labels
        self.mean_y = np.mean(self.ys)
        self.mean_deviation = np.mean(np.abs(self.ys - self.mean_y))

    def plot(self):
        plt.figure(figsize=(10, 6))
        # Punkte plotten
        plt.scatter(self.xs, self.ys, label="Geometriefaktoren", color="blue")

        # Beschriftungen einfügen (falls vorhanden)
        if self.labels is not None and len(self.labels) == len(self.xs):
            for x, y, label in zip(self.xs, self.ys, self.labels):
                plt.text(x, y, label, fontsize=9, ha="right", va="bottom")

        # Mittelwert-Linie
        plt.axhline(self.mean_y, color="red", linestyle="--", label=f"Mittlere Geometriefaktor")
        plt.title("Mittlere Abweichung 4,7%")
        plt.xlabel("Energie [keV]")
        plt.ylabel("Geometriefaktoren")
        plt.legend()
        plt.grid(True)
        plt.savefig("C:\\Users\\julia\\OneDrive\\Dokumente\\A_Christian\\Masterarbeit\\Masterarbeit\\Geometriefaktoren.png",
                dpi=500, bbox_inches='tight')


        plt.show()

    def report(self):
        print(f"Mittelwert der y-Werte: {self.mean_y:.6e}")
        print(f"Mittlere Abweichung von der Linie: {self.mean_deviation:.6e}")
        print(f"Mittlere Abweichung von der Linie: {self.mean_deviation/self.mean_y:.6e}")


# --- Beispiel-Nutzung ---
xs = [22.10295567976446, 25.19196900066341, 4.507980015896446, 23.10792994876348,
      8.041215748748293, 4.949304535637149, 15.74615118298751, 8.631189867640346,
      9.876462210974347, 1.487000000000000, 1.739334980440601, 10.82794806552806,
      3.132390809206833, 3.443187787468415, 10.54056208267398, 8.139111104249773,
      2.983390817647193]

ys = [4.16001e-05, 3.54522e-05, 3.67536e-05, 3.92492e-05, 3.77221e-05, 3.62451e-05,
      4.20839e-05, 3.83969e-05, 3.85271e-05, 3.37104e-05, 3.94553e-05, 3.74448e-05,
      3.78719e-05, 4.21752e-05, 3.78509e-05, 3.86222e-05, 4.19843e-05]

labels = ["Ag", "Sn", "Ti", "Cd", "Cu", "V", "Zr", "Zn", "Ge", "Al",
          "Si", "Bi", "Cd", "Sn", "Pb", "Ta", "Ag"]

plotter = DataPlotter(xs, ys, labels=labels)
plotter.plot()
plotter.report()
