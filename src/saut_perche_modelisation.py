import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Données numériques
m = 77 # masse perchiste ((kg))
g = 9.8 # accélération pesanteur (N/kg)
h = 2.0 # hauteur initiale perche / sol
L = 4.6 # longueur perche (m)
p = 0.2 # profondeur du butoir (m)
v0 = 27/3.6 # vitesse initiale perchiste (m/s)
vz0 = 1 # dernière impulsion du pied (donne une vitesse verticale)
EI = 1450 # rigidité de flexion de la perche
pas = 0.001 # pas de temps

def euler(pas,EI):
    """
    renvoie les listes : temps, x, z, vx, vz, énergie potentielle
    de pesanteur, énergie cinétique, énergie potentielle de la perche.
    """
    tk = 0 # date initiale
    t = [tk]# liste des temps
    xk, zk = -np.sqrt(L**2-(h+p)**2),h # coordonnées initiales du perchiste
    x, z = [xk], [zk]
    vxk, vzk = v0, vz0# composantes vitesse intiale
    vx, vz = [vxk], [vzk]
    Epp = [m*g*zk]# énergie pot. pesanteur
    Ec = [1/2*m*(vxk**2+vzk**2)]# énergie cinétique
    Em = Epp[0] + Ec[0]# énergie mécanique
    Ept = [0]# énergie pot. perche
    appui = True # indique si le perchiste est encore accroché à la perche
    while zk > 0 :# on arrête quand le perchiste retombe au sol
        if appui:# le perchiste s'appuie
            d = np.sqrt(xk**2+(zk+p)**2)# distance perchiste-butoir
            tk = tk + pas
            xk = xk + vxk*pas
            zk = zk + vzk*pas
            vxk = vxk + xk/d*(12*EI/L**2/m)*(((8-3*d/L)/5*pas))
            vzk = vzk + ((zk+p)/d*12*EI/L**2/m*(8-3*d/L)/5-g)*pas
            if xk**2+(zk+p)**2 > L**2:# le perchiste lâche la perche quand elle n'est plus pliée
                appui = False
        else: # le perchiste a lâché la perche
            tk = tk+pas
            xk = xk+vxk*pas
            zk = zk+vzk*pas
            vxk = vxk
            vzk = vzk - g*pas# chute libre
        x.append(xk)
        z.append(zk)
        vx.append(vxk)
        vz.append(vzk)
        t.append(tk)
        Epp.append(m*g*zk)
        Ec.append(1/2*m*(vxk**2+vzk**2))
        Ept.append(Em-m*g*zk - 1/2*m*(vxk**2+vzk**2))
    return t, x, z, vx, vz, Epp, Ec, Ept

fig = plt.figure(figsize=(10,8))
plt.title("modélisation d'un saut à la perche",fontsize=16)
plt.xlabel("temps (s)")
plt.ylabel("Énergie (J)")


# calcul des paramètres :
t, x, z, vx, vz, Epp, Ec, Ept = euler(pas,EI)

print("t",t)
print("x",x)
print("z",z)
print("vx",vx)
print("vz",vz)
print("vx",vx)
print("vz",vz)
print("Epp de l'atlhète",Epp)
print("Ec de l'atlhète",Ec)
print("Ept energie potntielle elastique de la perche ",Ept)

# tracé des courbes :
plt.plot(t, Ec, label="Énergie cinétique de l'athlète")
plt.plot(t, Epp, label="Énergie potentielle de pesanteur")
plt.plot(t, Ept, label="Énergie potentielle de la perche")

plt.legend()

# phases du saut :
# création de dataframe des énergies :
df = pd.DataFrame(
        {'t':t, 'Ec':Ec, 'Epp':Epp, 'Ept':Ept}
        )

t1=float(df.loc[df['Ept']==max(Ept),'t'])#date de fin de phase 1
t3=float(df.loc[df['Epp']==max(Epp),'t'])#date de fin de phase 3

df=df[1500:2000]# sélection d'une tranche contenant le maximum local de E cinétique
Ec=df['Ec']

t2=float(df.loc[df['Ec']==max(Ec),'t'])#date de fin de phase 2

for date in [t1,t2,t3]:
    plt.axvline(date, ls='--', color='red',
                linewidth='1',alpha=0.5)

z_phase=-100 # ordonnée des flèches des phases

props = dict(boxstyle='circle', facecolor='white', pad=0.2)
plt.annotate("", xy=(0, z_phase), xytext=(t1, z_phase),arrowprops=dict(arrowstyle="<|-|>"))
plt.text(t1/2, z_phase, "1", fontsize=12, bbox=props, ha='center',
         va='center')

plt.annotate("", xy=(t1, z_phase), xytext=(t2, z_phase),arrowprops=dict(arrowstyle="<|-|>"))
plt.text((t2+t1)/2, z_phase, "2", fontsize=12, bbox=props, ha='center',
         va='center')

plt.annotate("", xy=(t2, z_phase), xytext=(t3, z_phase),arrowprops=dict(arrowstyle="<|-|>"))
plt.text((t3+t2)/2, z_phase, "3", fontsize=12, bbox=props, ha='center',
         va='center')

plt.annotate("", xy=(t3, z_phase), xytext=(max(t), z_phase),arrowprops=dict(arrowstyle="<|-|>"))
plt.text((max(t)+t3)/2, z_phase, "4", fontsize=12, bbox=props, ha='center',
         va='center')

plt.text(0,3000,"1 : pliage de la perche\n2 : dépliage\n3 : perche lâchée\n4 : chute",
         va='top')

#attribution
ax = plt.gca()

plt.show()
#fig.savefig("saut_perche_modelisation.png", dpi=200)
#fig.savefig("saut_perche_modelisation.pdf")
