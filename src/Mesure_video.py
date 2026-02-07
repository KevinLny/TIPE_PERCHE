import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Données numériques
m = 55 # masse perchiste ((kg))

# Acquisition point par point du centre de gravité de l'athlète

temps =[0.100,0.200,0.300,0.400,0.500,0.600,0.700,0.800,0.900,1.000,1.100,1.200,1.300,1.400,1.500,1.600,1.700,1.800,1.900,2.000,2.100,2.200,2.300,2.400,2.500,2.600,2.700,2.800,2.900,3.000,3.100,3.200]
Ec = [2206.455,2262.219,2298.968,2230.072,2312.166,2463.235,2369.937,2206.583,1715.449,1163.783,825.003,522.586,407.888,380.838,408.960,507.155,591.486,623.954,576.991,449.738,301.291,176.629,96.567,68.676,136.175,272.308,415.432,618.060,915.811,1196.185,1410.057,1511.585]
Epp = [521.309,499.381,554.408,532.066,565.579,570.130,535.376,551.098,639.637,761.276,865.952,903.188,1000.416,1069.924,1191.149,1399.672,1597.852,1832.028,2094.751,2350.854,2517.590,2655.364,2751.765,2769.142,2666.949,2528.347,2336.373,2117.092,1864.299,1552.341,1127.020,753.415]

temps_bis =[0.000,0.100,0.200,0.300,0.400,0.500,0.600,0.700,0.800,0.900,1.000,1.100,1.200,1.300,1.400,1.500,1.600,1.700,1.800,1.900,2.000,2.100,2.200,2.300,2.400,2.500,2.600,2.700,2.800,2.900,3.000,3.100,3.200,3.300]
x = [0.487,1.319,2.294,3.176,4.093,4.989,5.887,6.864,7.888,8.629,9.461,9.943,10.367,10.795,11.100,11.347,11.594,11.860,12.031,12.163,12.296,12.412,12.547,12.738,12.922,13.080,13.101,13.150,13.312,13.508,13.678,13.793,13.922,13.988]
y = [0.951,0.966,0.926,1.028,0.986,1.048,1.057,0.992,1.021,1.186,1.411,1.605,1.674,1.854,1.983,2.208,2.594,2.961,3.395,3.882,4.357,4.666,4.921,5.100,5.132,4.943,4.686,4.330,3.924,3.455,2.877,2.089,1.396,0.666]

temps_bis2 = [0.100,0.200,0.300,0.400,0.500,0.600,0.700,0.800,0.900,1.000,1.100,1.200,1.300,1.400,1.500,1.600,1.700,1.800,1.900,2.000,2.100,2.200,2.300,2.400,2.500,2.600,2.700,2.800,2.900,3.000,3.100,3.200]
vx = [8.957,9.069,9.140,9.001,9.169,9.464,9.280,8.912,7.731,6.273,5.238,4.131,3.541,3.006,2.624,2.374,2.069,1.707,1.370,1.281,1.399,1.576,1.711,1.450,1.004,0.850,1.067,1.513,1.651,1.505,1.205,0.930]
vy = [0.090,0.132,0.225,0.283,0.000,0.015,0.239,0.902,1.615,1.725,1.600,1.393,1.514,2.194,2.826,3.579,4.151,4.447,4.371,3.836,3.000,1.985,0.765,-0.628,-1.986,-3.030,-3.737,-4.493,-5.530,-6.421,-7.059,-7.355]

# Affichage du résultat
# Première figure pour la position et la vitesse
plt.figure(figsize=(8, 4))
plt.plot(temps_bis2, vx, label='Vitesse selon x (m/s)')
plt.xlabel('Temps (s)')
plt.ylabel('Position / Vitesse')
plt.legend()
plt.title('Position et Vitesse en fonction du temps')

# Deuxième figure pour la position en fonction de la hauteur

plt.figure(figsize=(8, 4))
plt.plot(x, y, label='y en fonction de x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Position et Vitesse en fonction du temps')

# Troisième figure pour l'énergie cinétique et potentielle
plt.figure(figsize=(10, 8))
plt.plot(temps, Ec, label='Énergie cinétique')
plt.plot(temps, Epp, label='Énergie potentielle')
plt.xlabel('Temps (s)')
plt.ylabel('Énergie (J)')
plt.legend()
plt.title('Acquisition : Énergie Cinétique et Potentielle en fonction du temps')

t2 = temps[17]
t3 = temps[Epp.index(max(Epp))]


for date in [t2,t3]:
    plt.axvline(date, ls='--', color='red',
                linewidth='1',alpha=0.5)

z_phase=0 # ordonnée des flèches des phases

props = dict(boxstyle='circle', facecolor='white', pad=0.2)

plt.annotate("", xy=(t2, z_phase), xytext=(t3, z_phase),arrowprops=dict(arrowstyle="<|-|>"))
plt.text((t3+t2)/2, z_phase, "3", fontsize=12, bbox=props, ha='center',
         va='center')

plt.annotate("", xy=(t3, z_phase), xytext=(max(temps), z_phase),arrowprops=dict(arrowstyle="<|-|>"))
plt.text((max(temps)+t3)/2, z_phase, "4", fontsize=12, bbox=props, ha='center',
         va='center')

plt.text(0,2000,"1 : pliage de la perche\n2 : dépliage\n3 : perche lâchée\n4 : chute",
         va='top')

#attribution
ax = plt.gca()

# Afficher les graphiques
plt.show()
