# 🏓 Ping FFTT Manager

Application **Django 6 + Tailwind CSS** pour la **création et la gestion de tournois de tennis de table FFTT**.

Le flux principal :

1. **Créer** un tournoi (formulaire rapide ou **fichier JSON/YAML**).
2. **Entrer** dans le tournoi pour gérer joueurs, tableaux, poules, planning, matchs et exports.

---

## 🎯 Objectifs

* Création rapide de **tournoi** (nom, date, lieu, nb de tables, contraintes globales).
* Gestion **joueurs / clubs / tableaux / inscriptions** (simples & doubles).
* **Contraintes automatiques** : max **2 simples + 1 double** par joueur/jour, partenaire **obligatoire** en double, **interdit** en simple.
* **Tirage au serpent** + anti-club, poules, feuilles, classement de poule (set average).
* **Élimination directe** (1/16 → Finale), exports **PDF/CSV** et futur export **FFTT**.

---

## ⚙️ Stack

* **Backend** : Django 6.x
* **Front** : Tailwind via `django-tailwind`
* **DB** : SQLite (local), PostgreSQL (prod future)
* **Déploiement** : Azure (prévu)
* **Workflow** : VS Code, Git/GitHub, micro‑sprints (≤5 min)

---

## 🚀 Installation rapide

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows Git Bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py tailwind start
```

---

## 🧱 Modèles principaux

* **Tournoi**(nom, date, lieu, nb_tables, contraintes globales)
* **Club**, **Joueur**(licence, points, sexe, date_naissance, club)
* **Tableau**(libellé, bornes points, simple/double, mixte, capacité, date)
* **Inscription**(joueur, tableau, partenaire?, statut)

---

## 🧩 Nouveau : configuration d’un tournoi via **JSON ou YAML**

Vous pouvez décrire un tournoi complet (métadonnées, contraintes, tableaux, joueurs à importer) dans un fichier **YAML** ou **JSON** et le charger.

### 📄 Schéma attendu (conceptuel)

```yaml
nom: "Open de Saint-Paul"
date: "2026-02-15"      # YYYY-MM-DD
lieu: "Gymnase Nelson"
nb_tables: 16
contraintes:
  max_simples_par_joueur: 2
  max_doubles_par_joueur: 1
  serpent_anti_club: true
# (optionnel) chemins d'import
imports:
  joueurs_csv: "data/joueurs_demo.csv"  # séparateur ; ou ,
# Définition des tableaux
tableaux:
  - libelle: "Simple -900"
    date: "2026-02-15"
    min_points: 0
    max_points: 900
    is_double: false
    mixte: false
    capacite: 64
  - libelle: "Toutes séries"
    date: "2026-02-15"
    min_points: 0
    max_points: 4000
    is_double: false
    mixte: false
    capacite: 64
  - libelle: "Double mixte TS"
    date: "2026-02-15"
    min_points: 0
    max_points: 4000
    is_double: true
    mixte: true
    capacite: 64
```

### 🔁 Version JSON équivalente

```json
{
  "nom": "Open de Saint-Paul",
  "date": "2026-02-15",
  "lieu": "Gymnase Nelson",
  "nb_tables": 16,
  "contraintes": {
    "max_simples_par_joueur": 2,
    "max_doubles_par_joueur": 1,
    "serpent_anti_club": true
  },
  "imports": { "joueurs_csv": "data/joueurs_demo.csv" },
  "tableaux": [
    { "libelle": "Simple -900", "date": "2026-02-15", "min_points": 0, "max_points": 900, "is_double": false, "mixte": false, "capacite": 64 },
    { "libelle": "Toutes séries", "date": "2026-02-15", "min_points": 0, "max_points": 4000, "is_double": false, "mixte": false, "capacite": 64 },
    { "libelle": "Double mixte TS", "date": "2026-02-15", "min_points": 0, "max_points": 4000, "is_double": true, "mixte": true, "capacite": 64 }
  ]
}
```

### ▶️ Chargement (ligne de commande)

> *Le chargeur est livré sous forme de commande de management.*

```bash
# YAML ou JSON indifféremment
python manage.py load_tournoi --file configs/tournoi.yaml
# ou
python manage.py load_tournoi --file configs/tournoi.json
```

**Ce que fait `load_tournoi` :**

1. Crée l'objet **Tournoi** et applique les **contraintes globales**.
2. Crée les **Tableaux** associés.
3. Si `imports.joueurs_csv` est fourni, effectue un **import CSV** (prévisualisation possible en UI) et associe les joueurs.

> Si le tournoi existe déjà (même nom + date), la commande peut **mettre à jour** (option `--update`) au lieu de dupliquer.

### 📥 Chargement via l’UI (prévu)

* Page **Créer un tournoi** : choix entre saisie manuelle **ou** dépôt d’un fichier **YAML/JSON** → prévisualisation → confirmation → redirection vers le **Tableau de bord du tournoi**.

---

## 🧭 Navigation (MVP)

* Accueil (cartes d’accès rapide)
* **Créer un tournoi** → formulaire / upload YAML/JSON
* **Tableau de bord tournoi** → liens : joueurs, tableaux, poules, planning, feuilles, élimination directe, exports
* Admin Django pour gestion avancée

---

## 🧠 Micro‑sprints (réalisés / à venir)

* [x] Base Django + Tailwind
* [x] Modèles Club/Joueur/Tableau/Inscription
* [x] Validations : partenaire simple/double + quotas/jour
* [x] Import CSV joueurs (prévisualisation)
* [x] Thème clair + sombre (toggle)
* [x] Page d’accueil (cartes + boutons)
* [x] **Modèle Tournoi** + admin
* [ ] **Commande `load_tournoi`** YAML/JSON (WIP)
* [ ] UI “Créer un tournoi” (saisie / upload) + dashboard
* [ ] Tirage au serpent + anti-club
* [ ] Classements poules (set average) + feuilles PDF
* [ ] Bracket élimination directe + exports

---

## 📜 Licence

MIT (à confirmer selon ton choix).

## 👤 Auteur

**Olivier Savriama** — Île de La Réunion 🇷🇪
