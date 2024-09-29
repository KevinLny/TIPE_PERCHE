
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Données numériques
m = 77 # masse perchiste ((kg))
g = 9.8 # accélération pesanteur (N/kg)
h = 2.0 # hauteur initiale perche / sol
l = 4 # longueur perche (m)
p = 0.2 # profondeur du butoir (m)
v0 = 27/3.6 # vitesse initiale perchiste (m/s)
vz0 = 1 # dernière impulsion du pied (donne une vitesse verticale)
EI = 1400 # rigidité de flexion de la perche
pas = 0.001 # pas de temps

# Redéfinition de la fonction euler à l'intérieur du même script pour éviter les problèmes d'importation
def euler(pas, EI, L):
    """
    renvoie les listes : temps, x, z, vx, vz, énergie potentielle
    de pesanteur, énergie cinétique, énergie potentielle de la perche.
    """
    tk = 0  # date initiale
    t = [tk]  # liste des temps
    xk, zk = -np.sqrt(L**2 - (h + p)**2), h  # coordonnées initiales du perchiste
    x, z = [xk], [zk]
    vxk, vzk = v0, vz0  # composantes vitesse initiale
    vx, vz = [vxk], [vzk]
    Epp = [m * g * zk]  # énergie potentielle de pesanteur
    Ec = [1 / 2 * m * (vxk**2 + vzk**2)]  # énergie cinétique
    Em = Epp[0] + Ec[0]  # énergie mécanique
    Ept = [0]  # énergie potentielle de la perche
    appui = True  # indique si le perchiste est encore accroché à la perche
    while zk > 0:  # on arrête quand le perchiste retombe au sol
        if appui:  # le perchiste s'appuie
            d = np.sqrt(xk**2 + (zk + p)**2)  # distance perchiste-butoir
            tk = tk + pas
            xk = xk + vxk * pas
            zk = zk + vzk * pas
            vxk = vxk + xk / d * (12 * EI / L**2 / m) * (((8 - 3 * d / L) / 5 * pas))
            vzk = vzk + ((zk + p) / d * 12 * EI / L**2 / m * (8 - 3 * d / L) / 5 - g) * pas
            if xk**2 + (zk + p)**2 > L**2:  # le perchiste lâche la perche quand elle n'est plus pliée
                appui = False
        else:  # le perchiste a lâché la perche
            tk = tk + pas
            xk = xk + vxk * pas
            zk = zk + vzk * pas
            vxk = vxk
            vzk = vzk - g * pas  # chute libre
        x.append(xk)
        z.append(zk)
        vx.append(vxk)
        vz.append(vzk)
        t.append(tk)
        Epp.append(m * g * zk)
        Ec.append(1 / 2 * m * (vxk**2 + vzk**2))
        Ept.append(Em - m * g * zk - 1 / 2 * m * (vxk**2 + vzk**2))
    return t, x, z, vx, vz, Epp, Ec, Ept

# Définir la fonction à deux variables
def f(EI, L):
    t, x, z, vx, vz, Epp, Ec, Ept = euler(0.001, EI, L)
    return max(z)

# Générer les données
EI_values = np.linspace(1400, 1600, 50)
L_values = np.linspace(3, 5, 50)
EI, L = np.meshgrid(EI_values, L_values)

# Calculer z pour chaque paire (EI, L)
z = np.array([[f(ei, l) for ei in EI_values] for l in L_values])

# Créer le graphique en surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(EI, L, z, cmap='viridis')

# Ajouter des étiquettes
ax.set_xlabel('EI axis')
ax.set_ylabel('L axis')
ax.set_zlabel('Z axis')

plt.show()

