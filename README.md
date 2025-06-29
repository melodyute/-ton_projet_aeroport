# Projet Python – Système de gestion des vols et passagers avec MongoDB

Ce projet est un mini système de gestion pour un aéroport, développé en Python avec MongoDB comme base de données. Il permet de :

- Ajouter / modifier / supprimer des vols et passagers
- Recommander des services personnalisés aux passagers
- Envoyer des emails simulés
- Visualiser des statistiques
- Utiliser un système CRUD simple via des fonctions

## Fichiers du projet

| Fichier                | Description |
|------------------------|-------------|
| `init_db.py`           | Initialisation de la base MongoDB |
| `crud.py`              | Opérations CRUD (Create, Read, Update, Delete) |
| `recommender.py`       | Système de recommandation de services |
| `email_suggestion.py`  | Simulation d'envoi d'emails |
| `test.py`              | Tests simples du système |
| `ton_notebook.ipynb`   | Démonstration du projet dans Jupyter Notebook |

## Technologies utilisées

- Python 3.12
- MongoDB (avec `pymongo`)
- Jupyter Notebook
- GitHub

## Auteur

Projet réalisé par Mélody Ute – 2025

## 📖 Guide d’utilisation

### 1. Cloner le projet

Télécharge ou clone ce dépôt GitHub :

```bash
git clone https://github.com/melodyute/-ton_projet_aeroport.git
cd -ton_projet_aeroport

pip install pymongo

python init_db.py

python test.py

jupyter notebook

### 2. Lancer le projet étape par étape

```bash
# 1. Installer pymongo
pip install pymongo

# 2. Initialiser la base MongoDB avec les données
python init_db.py

# 3. Lancer les tests (optionnel)
python test.py

# 4. Lancer le notebook pour tester les fonctionnalités
jupyter notebook


