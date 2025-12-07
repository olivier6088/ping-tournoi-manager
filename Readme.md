# 🏓 Ping Tournoi Manager

Prototype Django + Tailwind centré sur la page « Créer un nouveau tournoi ». Les anciens modèles et l’app `competitions` ont été supprimés pour repartir sur une base légère dédiée au design du parcours.

## 🎯 Objectif actuel

* Construire une page de saisie claire pour nommer un tournoi, définir sa date, son lieu, le nombre de tables et noter des contraintes globales.
* Prévisualiser les informations saisies sans encore les enregistrer en base.
* Préparer l’interface à accueillir plus tard les imports CSV/JSON et la persistance.

## 🚀 Lancer le projet en local

```bash
python -m venv .venv
source .venv/Scripts/activate  # ou source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate  # uniquement les apps Django de base
python manage.py runserver
```

## 🧭 Parcours disponible

* **Accueil** : carte de présentation et lien direct vers la création de tournoi.
* **Créer un tournoi** : formulaire épuré + bloc de prévisualisation. Aucune sauvegarde n’est réalisée pour l’instant.

## ⚙️ Stack

* Backend : Django 6.x
* Front : Tailwind via `django-tailwind`
* Base de données : SQLite (utilisée uniquement pour les apps Django par défaut)

## 🔮 Prochaines étapes

* Brancher la persistance (modèle Tournoi et stockage réel).
* Ajouter l’import CSV/JSON et les écrans de configuration de tableaux.
* Étendre le tableau de bord tournoi et les exports.
