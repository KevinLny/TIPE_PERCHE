import matplotlib.pyplot as plt
import numpy as np
from math import *

# Données numériques
m = 77  # masse perchiste (kg)
g = 9.8  # accélération pesanteur (N/kg)
h = 2.0  # hauteur initiale perche / sol
L = 40.5  # longueur de la piste
l0 = 4.6  # longueur perche (m)
p = 0.2  # profondeur du butoir (m)
a0 = 1  # Accélération constante du perchiste (m/s²)
vz0 = 1  # dernière impulsion du pied (donne une vitesse verticale)
EI = 450  # rigidité de flexion de la perche (N/m)
pas = 0.1  # pas de temps
w = sqrt(EI/m)

def saut():
    # Phase 1: Course d'élan
    ti = 0
    tt = [0]
    x = 0
    vx = 0
    xt = [0]
    vxt = [0]
    Epp = [0]
    Ec = [0]
    while (vx<sqrt(2*a0*L)):
        vx = vx + (1 / 2) * a0 * pas ** 2
        ti = ti + pas
        vxt.append(vx)
        tt.append(ti)
        Ec.append(0.5 * m * vx ** 2)
        Epp.append(0)
    # Phase 2: La flexion de la perche
    t = 0 # Palier au probleme du temps
    while (vx>0):
        ti = ti + pas
        t = t + pas
        x = x + L*cos(w*t) +sqrt(2*a0*L)*(1/w)*sin(w*t)
        vx = vx - L*w*sin(w*t) + sqrt(2*a0*L)*cos(w*t)
        vxt.append(vx)
        tt.append(ti)
        Ec.append(0.5 * m * vx ** 2)
        Epp.append(0)
    return tt, vxt, Ec, Epp

tt, vxt, Ec, Epp = saut()

# Affichage du résultat
# Première figure pour la position et la vitesse
plt.figure(figsize=(8, 4))
plt.plot(tt, vxt, label='Vitesse (m/s)')
plt.xlabel('Temps (s)')
plt.ylabel('Position / Vitesse')
plt.legend()
plt.title('Position et Vitesse en fonction du temps')

# Deuxième figure pour l'énergie cinétique et potentielle
plt.figure(figsize=(8, 4))
plt.plot(tt, Ec, label='Énergie cinétique')
plt.plot(tt, Epp, label='Énergie potentielle')
plt.xlabel('Temps (s)')
plt.ylabel('Énergie')
plt.legend()
plt.title('Énergie Cinétique et Potentielle en fonction du temps')

# Afficher les graphiques
plt.show()
