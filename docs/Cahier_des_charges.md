# Cahier des Charges – Application de Tournoi FFTT

## Sommaire

1. **Contexte et objectifs**
2. **Glossaire**
3. **Périmètre fonctionnel**
4. **Rôles et parcours utilisateurs**
5. **Fonctionnalités du MVP**
6. **Fonctionnalités futures**
7. **Architecture technique**
8. **Modèle de données**
9. **Règles métier**
10. **Import / Export (CSV, JSON, SPID)**
11. **Impression et PDF**
12. **Accessibilité, i18n et sécurité**
13. **Performance, qualité et déploiement**
14. **Stratégie front (Django + HTMX (option))**
15. **Roadmap et lots**
16. **Annexes (Gherkin, formats, exemples)**

---

## 1. Contexte et objectifs

L’application vise à **gérer automatiquement un tournoi FFTT de club** : inscription, création de poules, génération du **Tableau à Élimination Directe (TED)**, saisie des scores et export vers le système **SPID**.

**Objectifs :**

* Création d’un tournoi via formulaire ou import JSON/YAML.
* Gestion des joueurs (points FFTT, club, licence, tableaux multiples).
* Génération des poules avec **règle du serpent** et **anti-club**.
* Gestion du TED (bracket simple, ajustable à la main).
* Édition manuelle des scores avec recalcul automatique des classements.
* Impression et export (CSV, PDF, SPID FFTT).

---

## 2. Glossaire

| Terme                                   | Définition                                                                                    |
| --------------------------------------- | --------------------------------------------------------------------------------------------- |
| **FFTT**                                | Fédération Française de Tennis de Table.                                                      |
| **SPID**                                | Système de gestion des résultats FFTT.                                                        |
| **TED**                                 | Tableau à Élimination Directe.                                                                |
| **Poule**                               | Groupe de joueurs s’affrontant avant la phase éliminatoire.                                   |
| **Seed**                                | Tête de série d’un joueur déterminée par ses points FFTT.                                     |
| **Serpentin**                           | Algorithme de répartition équilibrée des têtes de série dans les poules.                      |
| **OCR (Optical Character Recognition)** | Reconnaissance optique des caractères : extraction de scores depuis des feuilles papier.      |
| **CSV**                                 | Format de fichier tabulaire (Comma-Separated Values).                                         |
| **JSON / YAML**                         | Formats de configuration textuelle (JavaScript Object Notation / YAML Ain’t Markup Language). |
| **PWA**                                 | Progressive Web App : application web installable avec mode hors ligne.                       |

---

## 3. Périmètre fonctionnel

### MVP

* Tournoi FFTT avec un ou plusieurs **tableaux (Events)**.
* Import CSV joueurs avec colonnes d’inscription aux tableaux.
* Génération de **poules** selon les règles FFTT.
* Génération du **TED simple** (1 vs N).
* Saisie manuelle des scores.
* Export CSV/JSON + impression des feuilles de match.
* Page publique consultable (lecture seule).

### Évolutions futures

* Planification automatique (tables, horaires).
* Double élimination.
* OCR pour lecture automatique des feuilles de match.
* **Chatbot assistant d’organisation** (aide contextuelle, rappels, synthèse vocale).
* Rôles avancés (arbitre, table, spectateur authentifié).
* Statistiques détaillées (victoires, performances par club).
* API publique pour intégration avec d’autres systèmes.

---

## 4. Rôles et parcours utilisateurs

| Rôle              | Actions principales                                                                    |
| ----------------- | -------------------------------------------------------------------------------------- |
| **Organisateur**  | Crée un tournoi, importe joueurs, gère poules et TED, valide scores, imprime feuilles. |
| **Arbitre/Table** | Saisit les scores via interface mobile.                                                |
| **Spectateur**    | Consulte les résultats publics.                                                        |
| **Admin**         | Supervise les tournois, gère les utilisateurs et exports.                              |

**Parcours type :**

1. Création → import CSV joueurs → génération poules → affichage TED.
2. Saisie manuelle → mise à jour automatique des classements.
3. Impression feuilles → export SPID CSV.

---

## 5. Fonctionnalités du MVP

1. **Création / chargement d’un tournoi.**
2. **Import CSV joueurs** (vérification des colonnes, détection doublons, validation FFTT points/licence).
3. **Génération automatique des poules** (règle du serpent + anti-club).
4. **Ajustement manuel (drag & drop)**.
5. **Génération du TED** (2 premiers de chaque poule, placement croisé).
6. **Édition manuelle des scores** avec recalcul des classements.
7. **Impression des feuilles de match** (poules, TED, ou toutes).
8. **Export SPID FFTT (simples)** au format CSV.
9. **Page publique** (lecture seule, actualisation auto toutes les 10 s).

---

## 6. Fonctionnalités futures (post-MVP)

1. **OCR IA** pour reconnaître automatiquement les scores sur feuilles papier.
2. **Chatbot assistant tournoi** : aide à la configuration, rappel des horaires, correction des erreurs.
3. **Planification automatique** (tables, horaires, détection de conflits).
4. **Double élimination** + options de croisement avancées.
5. **Emails automatiques** (résultats, rappels).
6. **Tableaux doubles / équipes**.
7. **Tableau de statistiques** (performances, top clubs).
8. **PWA mobile offline**.

---

## 7. Architecture technique

* **Backend** : Django 6, SQLite (dev) → PostgreSQL (prod).
* **Frontend** : Tailwind CSS, Django Templates, HTMX.
* **Optionnel** : HTMX, Vite/Node ou Bun pour bundling.
* **Librairie TED** : [`brackets-viewer.js`](https://github.com/Drarig29/brackets-viewer.js) pour affichage graphique du tableau.
* **PDF** : WeasyPrint (serveur) + CSS @media print.
* **Sécurité** : Auth Django, CSRF, validation stricte des fichiers importés.

---

## 8. Modèle de données

* **Tournament(id, name, start_date, max_events_per_player, ranking_snapshot_date, is_public)**
* **Event(id, code, name, format, max_entries, group_layout_json, advancement_rules_json)**
* **Player(id, first_name, last_name, club, fftt_points, fftt_license)**
* **Group(id, event_id, name, size)**
* **Match(id, event_id, stage, round, player_a_id, player_b_id, score_json, status)**
* **Standing(id, group_id, player_id, wins, losses, points, rank)**

---

## 9. Règles métier principales

* Classement poule : Points → Confrontations → Diff. manches → Diff. points.
* Seeding par points FFTT → règle du serpent.
* Anti-club : swaps contrôlés (max 100 tentatives).
* Avancement : top 2 par poule → TED croisé (A1–B2, B1–A2).
* Verrouillage après validation organisateur.
* Imports et exports validés selon schémas JSON/Pydantic.

---

## 10. Import / Export

* **Import** : CSV (joueurs), JSON/YAML (config tournoi).
* **Export** : CSV (joueurs, matchs), JSON, PDF, SPID FFTT.
* **SPID FFTT CSV** : filtrage des simples validés, colonnes standard FFTT.

---

## 11. Impression et PDF

* Impression depuis **Poules**, **TED** ou **page dédiée** `/tournaments/{id}/print`.
* Filtres : event, poule, round, état.
* Contenu : entête tournoi, joueurs, sets, signatures, QR code (URL match).
* Génération PDF via WeasyPrint (<10 s pour 100 feuilles).

---

## 12. Accessibilité, i18n et sécurité

* **Accessibilité** : WCAG 2.1 niveau AA (contrastes, clavier, aria-labels).
* **Langues** : français / anglais via `django-i18n`.
* **Sécurité** : XSS, CSRF, gestion rôles, audit trail.
* **RGPD** : purge et suppression à la demande.

---

## 13. Performance, qualité et déploiement

* TTFB < 1.5 s, LCP < 2.5 s.
* Tests unitaires + intégration (pytest, Playwright).
* CI/CD Docker (Gunicorn + Whitenoise).
* Logs JSON et métriques (nb matchs, erreurs, temps moyen de saisie).

---

## 14. Stratégie front (Django + HTMX)

* MVP : Django Templates + Tailwind.
* Évolutif : HTMX (bracket, DnD poules).
* Bundler : Node.js **ou** Bun selon environnement.
* Communication : endpoints JSON sécurisés.
* Tests d’intégration via Playwright.

---

## 15. Roadmap

| Lot             | Contenu                                                                                  | Durée estimée |
| --------------- | ---------------------------------------------------------------------------------------- | ------------- |
| **Lot 1 (MVP)** | Création tournoi, import CSV, poules, TED simple, saisie scores, impression, export SPID | 3 sprints     |
| **Lot 2**       | Planning auto, bracket double élimination, IA OCR, chatbot assistant                     | 3 sprints     |
| **Lot 3**       | API publique, rôles avancés, PWA mobile, statistiques                                    | 3+ sprints    |

---

## 16. Annexes

### A. Exemples de formats CSV / YAML

(identiques au CdC précédent)

### B. Scénarios Gherkin clés

* Import CSV joueurs (validation limite par joueur).
* Génération poules (serpent + anti-club).
* Édition score → recalcul classement → TED.
* Export SPID FFTT (simples uniquement).
* Impression PDF (poules ou TED).

---

**Fin du document — version restructurée (Décembre 2025)**
