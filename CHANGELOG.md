# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/)
et ce projet suit le versionnement sémantique (SemVer).

---

## [1.0.0] - 2025-12-17

### Added
- Pipeline Python d’automatisation des données (extraction → nettoyage → transformation → export)
- Interface en ligne de commande (CLI) avec paramètres :
  - fichier d’entrée (`--input`)
  - dossier de sortie (`--outdir`)
  - mode verbose (`--verbose`)
- Nettoyage automatique des données :
  - suppression des valeurs invalides
  - sécurisation des champs numériques
- Transformation des données avec agrégation par critères métiers
- Génération automatique :
  - d’un fichier de données nettoyées
  - d’un rapport synthétique
- Système de logs structuré (INFO / WARNING / ERROR)
- Environnement virtuel Python (venv)
- Documentation initiale du projet (README)

### Notes
- Première version stable du projet
- Base saine pour l’ajout de nouvelles sources de données et transformations
