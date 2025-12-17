# 🐍 Automation – Extraction & Transformation de données (Python)

Ce projet présente une mini-pipeline Python permettant d’automatiser le traitement de données à partir de fichiers bruts (CSV, API).

Il illustre comment transformer un fichier difficile à exploiter en **données propres** et en **rapport synthétique prêt à l’usage**, sans intervention manuelle.

Il montre comment :
- **extraire** des données (CSV, API ou fichiers bruts)
- **nettoyer** et **transformer** les données (pandas)
- **exporter** un fichier propre ou un rapport prêt à l’usage

---
## 🎯 Objectif

Réduire le temps passé sur des tâches manuelles répétitives et limiter les erreurs humaines en automatisant :
- la préparation des données,
- leur transformation,
- et la génération de résultats exploitables.

---
## 🧹 Nettoyage & 🔄 Transformation des données

Le traitement se fait en deux grandes étapes :

**🔹 Nettoyage (Cleaning)**
- vérification et sécurisation des données,
- suppression des valeurs invalides,
- mise au bon format des champs numériques et dates.

👉 Résultat : un fichier fiable et cohérent, prêt à être analysé.

**🔹 Transformation (Transform)**
- regroupement des données par critères métiers (client, catégorie, etc.),
- calcul automatique de totaux,
- génération d’un rapport synthétique.

👉 Résultat : une vision claire et exploitable des données, sans calcul manuel.

---

## 📂 Structure du projet

```
automation-data-python/
├── data/                # Fichiers d'entrée
├── output/              # Fichiers générés
├── scripts/             # Pipeline principale
│   └── transform.py
├── utils/               # Fonctions utilitaires
│   └── helpers.py
├── CHANGELOG.md         # Historique des versions
├── README.md
├── requirements.txt

```
---

## 🚀 Fonctionnalités

- Import de données depuis :
    - fichiers CSV
    - sources API
- Nettoyage automatique des données
- Transformation et agrégation des informations
- Export :
    - fichier nettoyé
    - rapport synthétique
- Exécution en une seule commande (automatisation simple)

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
python scripts/transform.py --verbose

```
---

## 📈 Améliorations prévues

- Ajout de graphiques simples (matplotlib)
- Source API configurable
- Interface CLI enrichie
- Enchaînement de plusieurs transformations
- Tests automatisés

---
## 🛠️ Ce que ce projet démontre

- capacité à automatiser un processus métier,
- gestion de données imparfaites (robustesse),
- structuration d’un outil réutilisable,
- approche orientée valeur et fiabilité.

---
## 📬 Contact

- Email : diawaramantcha@gmail.com
- LinkedIn : @mantcha-diawara
