# Stratégie de Sélection de Perche - Saut à la Perche (TIPE)

Ce projet de **TIPE (2023-2024)** présente une étude physique et numérique du saut à la perche. L'objectif est de modéliser le transfert d'énergie lors d'un saut pour déterminer les caractéristiques optimales de la perche (rigidité $EI$ et longueur $L$) en fonction du profil de l'athlète.

---

## 🎯 Problématique
**Quelles sont les caractéristiques de la perche à retenir en fonction des particularités (masse, vitesse) du perchiste ?**

---

## ⚙️ Modélisation Théorique
Le projet repose sur l'application du **Principe Fondamental de la Dynamique (PFD)** dans un référentiel galiléen. 

### 1. Détermination de la force
La force exercée par la perche est modélisée à partir du module d'Young ($E$) et du moment quadratique ($I$) du matériau:
$$F(x) = 12\frac{EI}{L^{2}}(1+\frac{3}{5}\frac{x}{L})$$

### 2. Équations du mouvement
Le système d'équations différentielles projeté selon les axes $x$ et $z$ est le suivant:
* **Axe x** : $m\frac{d^{2}x}{dt^{2}}=\frac{12}{5}\frac{EI}{L^{2}}(\frac{8}{\sqrt{x^{2}+(z+p^{2})}}-\frac{3}{L})x$
* **Axe z** : $m\frac{d^{2}z}{dt^{2}}=\frac{12}{5}\frac{EI}{L^{2}}(\frac{8}{\sqrt{x^{2}+(z+p^{2})}}-\frac{3}{L})z-mg$



---

## 💻 Simulations Numériques (Python)
Le dépôt contient plusieurs scripts permettant de simuler et d'optimiser le saut.

### 📊 Analyse Énergétique (`saut_perche_modelisation.py`)
Ce script utilise la **méthode d'Euler** pour résoudre les équations du mouvement. Il permet de visualiser la conversion de l'énergie cinétique en énergie potentielle élastique puis en énergie de pesanteur.

![Modélisation Énergétique](img/modelisation.PNG)
*Figure 1 : Phases du saut : (1) Pliage, (2) Dépliage, (3) Perche lâchée, (4) Chute.*

### 📉 Comparaison Expérimentale (`Mesure_video.py`)
Traitement de données issues d'une acquisition réelle pour valider le modèle théorique.

![Acquisition Réelle](img/Acquisition.PNG)
*Figure 2 : Évolution des énergies cinétique et potentielle issue de mesures réelles.*

---

## 🚀 Optimisation 3D (`Modélisation3D.py`)
Pour identifier la perche idéale, le script génère une surface 3D représentant la hauteur maximale $Z$ atteinte en fonction de la rigidité ($EI$) et de la longueur ($L$).

![Surface d'Optimisation](img/Figure_1.png)
*Figure 3 : Recherche du maximum de hauteur Z selon les paramètres de la perche.*
