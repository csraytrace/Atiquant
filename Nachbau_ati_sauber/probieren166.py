import numpy as np
import matplotlib.pyplot as plt
from Nachbau_ati_sauber.packages.Funktionen_Calc_I import Filter






print(Filter("1 Cu1", 0.00996094, 8.04,))
print(Filter("1 Cu1 + 9 H2", 0.8725, 8.04,))



from Nachbau_ati_sauber.packages.Funktionen_Calc_I import Filter

def find_thickness_for_target_T(
    material: str,
    energy_keV: float,
    T_target: float = 0.01,
    d_lo_init: float = 0.0,     # cm
    d_hi_init: float = 0.01,    # cm, Startschätzer fürs obere Intervallende
    grow_factor: float = 2.0,
    d_hi_max: float = 100.0,    # cm, Sicherheitslimit
    tol_T: float = 1e-4,        # Toleranz in Transmission
    tol_d: float = 1e-6,        # Toleranz in Dicke [cm]
    max_iter: int = 80
):
    """
    Finde Dicke d [cm], so dass Filter(material, d, energy_keV) ≈ T_target.
    Vorgehen:
      1) Bracketing: d_hi wird multiplikativ vergrößert, bis T(d_hi) <= T_target.
      2) Bisection im Intervall [d_lo, d_hi] bis Ziel erreicht.
    """
    if not (0.0 < T_target < 1.0):
        raise ValueError("T_target muss zwischen 0 und 1 liegen (exklusiv).")

    # Untere Grenze
    d_lo = float(d_lo_init)
    try:
        T_lo = float(Filter(material, d_lo, energy_keV))
    except Exception:
        # Manche Implementationen mögen d=0 nicht -> sehr kleine Dicke nehmen
        d_lo = 1e-9
        T_lo = float(Filter(material, d_lo, energy_keV))

    if T_lo < T_target:
        # Schon bei praktisch 0 Dicke unter Ziel -> numerischer Sonderfall
        return d_lo, T_lo

    # Obere Grenze (bracket)
    d_hi = float(d_hi_init)
    T_hi = float(Filter(material, d_hi, energy_keV))
    n_grow = 0
    while T_hi > T_target and d_hi < d_hi_max:
        d_hi *= grow_factor
        T_hi = float(Filter(material, d_hi, energy_keV))
        n_grow += 1
        if n_grow > 200:
            break

    if T_hi > T_target:
        raise RuntimeError(
            f"Kein Intervall gefunden: selbst bei d={d_hi:.6g} cm ist T={T_hi:.6g} > T_target={T_target}"
        )

    # Jetzt gilt: T(d_lo) >= T_target >= T(d_hi); führe Bisection aus
    it = 0
    while it < max_iter:
        d_mid = 0.5 * (d_lo + d_hi)
        T_mid = float(Filter(material, d_mid, energy_keV))

        # Abbruchkriterien
        if abs(T_mid - T_target) <= tol_T or abs(d_hi - d_lo) <= tol_d:
            return d_mid, T_mid

        # Entscheide Intervallhälfte (T fällt monoton mit d)
        if T_mid > T_target:
            d_lo, T_lo = d_mid, T_mid
        else:
            d_hi, T_hi = d_mid, T_mid

        it += 1

    # Falls max_iter erreicht, beste Annäherung zurückgeben
    d_best = 0.5 * (d_lo + d_hi)
    T_best = float(Filter(material, d_best, energy_keV))
    return d_best, T_best


if __name__ == "__main__":
    # Beispiel: Deine beiden Fälle bei 8.04 keV
    energy = 8.04  # keV
    #energy = 7.5  # keV
    targets = [
        ("1 Cu1", 0.01),           # wir suchen d für T=0.01
        ("1 Cu1 + 9 H2", 0.01),
    ]

    for material, T_target in targets:
        d, T = find_thickness_for_target_T(
            material=material,
            energy_keV=energy,
            T_target=T_target,
            d_lo_init=0.0,
            d_hi_init=0.01,   # bei Cu ist das schon nah dran
            grow_factor=2.0,
            d_hi_max=50.0,
            tol_T=1e-4,
            tol_d=1e-6,
            max_iter=80
        )
        print(f"Material: {material}")
        print(f"  Ziel: T = {T_target}")
        print(f"  Gefundene Dicke: d = {d:.6g} cm  (≈ {d*10:.6g} mm)")
        print(f"  Prüfe: T(d) = {T:.6g}")
        print("-" * 50)



