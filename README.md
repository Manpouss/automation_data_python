# 🐍 Automation – Extraction & Transformation de données (Python)

Ce projet présente une mini-pipeline Python permettant d’automatiser des tâches de traitement de données.
Il montre comment :
- **extraire** des données (CSV, API ou fichiers bruts)
- **nettoyer** et **transformer** les données (pandas)
- **exporter** un fichier propre ou un rapport prêt à l’usage

**🎯 Objectif** : automatiser des tâches manuelles récurrentes (reporting, nettoyage de fichiers, consolidation…).

---

## 📂 Structure du projet

```
automation-data-python/
├── data/             # Fichiers d'entrée
├── output/           # Résultats transformés
├── scripts/          # Logique Python
│ └── transform.py
├── utils/            # Fonctions utilitaires (Lecture, formatage, logs,...)
└── README.md
```
---

## 🚀 Fonctionnalités

- Import de données **CSV** ou **API** 
- Nettoyage automatique (drop, rename, formatage)  
- Transformations simples 
    - GroupBy
    - Merge
    - Filtrage dynamique
- Export CSV + rapport  
- Exécution en **script unique** (automatisation simple)

---

## 🛠️ Technologies utilisées

- Python 3  
- pandas  
- requests  
- pathlib  

---

## ▶️ Lancer le projet

```md
```bash

pip install -r requirements.txt
python scripts/transform.py
```
---

## 📈 Améliorations prévues

- Ajout d'un graphique simple (matplotlib)
- Possibilité d’utiliser une API source configurable
- Interface CLI plus propre (click / argparse)
- Création d'une version modulable pour enchaîner plusieurs transformations

---

## 📬 Contact

- Email : diawaramantcha@gmail.com
- LinkedIn : @mantcha-diawara
