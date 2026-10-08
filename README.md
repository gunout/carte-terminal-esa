# 🌍 Carte Terminal ESA

**Carte du monde ASCII dans le terminal avec logo ESA**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Platform](https://img.shields.io/badge/Platform-Terminal-000000?style=for-the-badge&logo=gnubash&logoColor=white)](https://github.com/gunout/carte-terminal-esa)
[![Data](https://img.shields.io/badge/Data-Natural%20Earth-4B8BBE?style=for-the-badge)](https://www.naturalearthdata.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge)](https://github.com/gunout/carte-terminal-esa/pulls)
[![Stars](https://img.shields.io/github/stars/gunout/carte-terminal-esa?style=for-the-badge&logo=github&color=gold)](https://github.com/gunout/carte-terminal-esa/stargazers)

---

<img width="1138" height="704" alt="ESA_MAP" src="https://github.com/user-attachments/assets/b540a09e-19eb-406c-94dd-98622a5e13e2" />

---

## 📖 Description

Un script Python qui affiche une **carte du monde en ASCII** directement dans votre terminal, accompagnée du logo de l'**Agence spatiale européenne (ESA)**.

Les continents sont dessinés à partir de données géographiques réelles (Natural Earth 110m) et rendus avec des caractères Unicode colorés via des codes ANSI. Paris est marqué d'un `X` rouge.

```
   ███████ ███████  █████
   ██      ██      ██   ██
   █████   ███████ ███████
   ██           ██ ██   ██
   ███████ ███████ ██   ██
   ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★

+--------------------------------------------------------+
|        •·•·•  •·•·•·•·•      •·•·•·•·•·•·•·•             |
|   •·•·•·•·•·•·•·•·•·•·•·•·•·•·•·•·•  ·•·•·•·•·•      |
|  •·•·•·•·•·•·•·X·•·•·•·•·•·•·•·•·•·•·•·•·•·•·•     |
|        •·•·•·•·•·•·•·•·•·•·•·•·•·•·•·•·•·•              |
+--------------------------------------------------------+
X = Paris (48.85°N, 2.35°E)   • · = Terre
★ Agence spatiale européenne — ESA
```

---

## ✨ Fonctionnalités

- 🗺️ **Carte mondiale ASCII** générée à partir de vraies données géographiques
- 🎨 **Couleurs ANSI** (bleu, jaune, rouge) pour un rendu terminal soigné
- 🛰️ **Logo ESA** en ASCII art intégré
- 📍 **Marqueur de Paris** positionné par coordonnées réelles
- ⚡ **Léger et rapide** : aucune dépendance lourde (seulement `pyshp`)
- 🧩 **Code lisible** et facilement personnalisable (résolution, couleurs, marqueurs)

---

## 🚀 Installation

### Prérequis

- Python **3.8+**
- Un terminal supportant les **couleurs ANSI** (Linux, macOS, WSL, Windows Terminal)

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/gunout/carte-terminal-esa.git
cd carte-terminal-esa

# 2. (Optionnel) Créer un environnement virtuel
python3 -m venv venv
source venv/bin/activate   # Linux / macOS
# venv\Scripts\activate    # Windows

# 3. Installer les dépendances
pip install pyshp
```

### Données géographiques

Téléchargez le fichier **Natural Earth 110m Land** et placez les fichiers dans `data/` :

```bash
mkdir -p data
# Télécharger ne_110m_land.shp, .shx, .dbf, .prj depuis :
# https://www.naturalearthdata.com/downloads/110m-physical-vectors/110m-land/
```

Structure attendue :

```
carte-terminal-esa/
├── carte_esa.py
└── data/
    ├── ne_110m_land.shp
    ├── ne_110m_land.shx
    ├── ne_110m_land.dbf
    └── ne_110m_land.prj
```

---

## 🎮 Utilisation

```bash
python3 carte_esa.py
```

La carte s'affiche immédiatement dans le terminal avec le logo ESA.

---

## ⚙️ Personnalisation

Ouvrez `carte_esa.py` et modifiez les constantes en haut du fichier :

| Constante | Description | Valeur par défaut |
|-----------|-------------|-------------------|
| `COLS` | Largeur de la carte (en caractères) | `120` |
| `ROWS` | Hauteur de la carte (en caractères) | `50` |
| `BLEU` / `BLEU_FONCE` | Couleurs des points terrestres | `94` / `34` |
| `ROUGE` | Couleur du marqueur | `91` |
| `JAUNE` | Couleur des étoiles | `93` |

### Changer le marqueur (ex. Kourou, Centre spatial guyanais)

```python
# Coordonnées de Kourou : 5.16°N, 52.65°O
kourou_i = int((90 - 5.16) / 180 * ROWS)
kourou_j = int((-52.65 + 180) / 360 * COLS)
grid[kourou_i][kourou_j] = f"{ROUGE}O{RESET}"
```

---

## 🛠️ Comment ça marche ?

1. **Chargement** des polygones terrestres via `pyshp` (fichier Shapefile Natural Earth).
2. **Génération d'une grille** `ROWS × COLS` : pour chaque cellule, on convertit `(i, j)` en `(lat, lon)`.
3. **Test d'appartenance** : algorithme *ray casting* (`point_in_polygon`) avec pré-filtrage par *bounding box* pour accélérer.
4. **Rendu** : chaque cellule terrestre reçoit un caractère `•` ou `·` coloré, l'océan reste vide.
5. **Marqueurs** ajoutés par conversion directe de coordonnées géographiques en indices de grille.

---

## 📦 Dépendances

| Paquet | Rôle |
|--------|------|
| [`pyshp`](https://pypi.org/project/pyshp/) | Lecture des fichiers Shapefile |

Aucune autre bibliothèque externe n'est requise (pas de `numpy`, pas de `matplotlib`).

---

## 🤝 Contribution

Les contributions sont les bienvenues !

1. Fork le projet
2. Créez votre branche (`git checkout -b feature/ma-fonctionnalite`)
3. Commit (`git commit -m 'Ajout de ma fonctionnalité'`)
4. Push (`git push origin feature/ma-fonctionnalite`)
5. Ouvrez une **Pull Request**

---

## 📄 Licence

Distribué sous licence **MIT**. Voir [`LICENSE`](LICENSE) pour plus d'informations.

---

## 🙏 Remerciements

- [Natural Earth](https://www.naturalearthdata.com/) pour les données géographiques libres de droits
- [pyshp](https://github.com/GeospatialPython/pyshp) pour la lecture des Shapefiles
- [Agence spatiale européenne (ESA)](https://www.esa.int/) pour l'inspiration

---

<p align="center">
  <b>⭐ Si ce projet vous plaît, n'hésitez pas à lui donner une étoile ! ⭐</b><br>
  <i>Fait avec 🛰️ et du Python</i>
</p>

---

<div align="center">

### 🇫🇷 Gunout · 2026

![Made in France](https://img.shields.io/badge/Made_in-France-002395?style=flat-square&labelColor=FFFFFF&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5MDAgNjAwIj48cmVjdCB3aWR0aD0iOTAwIiBoZWlnaHQ9IjYwMCIgZmlsbD0iIzAwMjM5NSIvPjxyZWN0IHdpZHRoPSI5MDAiIGhlaWdodD0iNDAwIiB5PSIxMDAiIGZpbGw9IiNmZmYiLz48cmVjdCB3aWR0aD0iOTAwIiBoZWlnaHQ9IjIwMCIgeT0iNDAwIiBmaWxsPSIjZWQyOTM5Ii8+PC9zdmc+)
![GitHub](https://img.shields.io/badge/GitHub-gunout-181717?style=flat-square&logo=github&logoColor=white)
![Year](https://img.shields.io/badge/2026-ED2939?style=flat-square&labelColor=FFFFFF)

<sub>© 2026 <strong>Gunout</strong> — Tous droits réservés.</sub>

</div>
