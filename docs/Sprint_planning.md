# Sprint Planning — Lot 1 (MVP)

## Sprint 1 : Création et gestion du tournoi

**Objectif :** disposer d’un socle fonctionnel permettant de créer un tournoi et d’importer les joueurs.

### Stories incluses

* US1.1 – Créer un tournoi
* US1.2 – Charger un tournoi existant
* US2.1 – Import CSV joueurs
* US2.3 – Visualiser liste joueurs inscrits

### Tâches techniques

1. Création modèle `Tournament`, `Player`, `Event`.
2. Formulaire Django + validations.
3. Vue Import CSV + parser Pandas / csv.
4. Interface liste joueurs + tri par FFTT points.
5. Tests unitaires et template Tailwind.

### Livrables

* Formulaire création tournoi fonctionnel.
* Import CSV avec rapport d’erreurs.
* Page joueurs avec tri et filtres.

---

## Sprint 2 : Génération poules et TED simple

**Objectif :** générer les poules, appliquer la règle du serpent et afficher le TED.

### Stories incluses

* US3.1 – Génération automatique des poules
* US3.2 – Ajustement manuel (drag & drop)
* US4.1 – Générer TED
* US4.2 – Afficher TED

### Tâches techniques

1. Implémentation algorithme serpent + anti-club.
2. Création modèle `Group`, `Match`, `Standing`.
3. Interface de visualisation des poules (HTML + HTMX).
4. Intégration librairie JS `brackets-viewer.js`.
5. Génération TED croisé (A1-B2, B1-A2).

### Livrables

* Génération complète des poules et TED.
* Visualisation TED côté navigateur.

---

## Sprint 3 : Gestion des scores, impression et export SPID

**Objectif :** permettre la saisie des scores, le recalcul automatique et les exports.

### Stories incluses

* US5.1 – Saisie des scores
* US5.3 – Recalcul automatique
* US6.1 – Impression feuilles de match
* US6.2 – Export SPID FFTT

### Tâches techniques

1. Formulaire modale édition score + validation.
2. Recalcul standings + qualifiés TED.
3. Gabarit PDF WeasyPrint (poules/TED).
4. Endpoint export CSV SPID.
5. Tests unitaires + e2e Playwright.

### Livrables

* Interface de saisie scores stable.
* PDF imprimable des matchs.
* Export CSV SPID valide.

---

## Sprint 4 : Page publique et statistiques de base

**Objectif :** ouvrir l’accès en lecture seule et commencer le suivi statistiques.

### Stories incluses

* US9.1 – Statistiques générales
* US9.2 – Joueurs actifs
* US9.3 – Joueurs en attente
* US9.4 – Alertes d’organisation

### Tâches techniques

1. Endpoint `/api/tournaments/{id}/stats` (agrégations ORM).
2. Page `/t/{slug}` publique avec auto-refresh 10 s.
3. Dashboard HTML/HTMX pour les KPI.
4. Notifications locales navigateur.

### Livrables

* Page publique fonctionnelle.
* Dashboard statistiques avec premiers indicateurs et alertes.

---

# Sprint Planning — Lots 2 & 3 (Post-MVP)

## Lot 2 : Automatisation & IA

* OCR IA pour reconnaissance des feuilles de match.
* Chatbot assistant tournoi (FAQ, rappels, erreurs).
* Planification automatique (tables, horaires, détection de conflits).
* Double élimination.

## Lot 3 : Expérience avancée & ouverture

* Rôles avancés (arbitre/table/spectateur connecté).
* PWA mobile offline.
* API publique.
* Tableau de statistiques avancées (performances joueurs/clubs).
* Historisation et export complet (JSON/CSV).

---

# Vue Kanban — Backlog MVP

## À faire

* [ ] US1.1 – Créer un tournoi
* [ ] US1.2 – Charger un tournoi existant
* [ ] US2.1 – Import CSV joueurs
* [ ] US2.3 – Visualiser liste joueurs inscrits
* [ ] US3.1 – Générer les poules automatiquement
* [ ] US3.2 – Ajuster manuellement les poules
* [ ] US4.1 – Générer le TED
* [ ] US4.2 – Afficher le TED
* [ ] US5.1 – Saisir les scores
* [ ] US5.3 – Recalcul automatique des classements
* [ ] US6.1 – Imprimer les feuilles de match
* [ ] US6.2 – Exporter les résultats SPID FFTT
* [ ] US9.1 – Statistiques générales du tournoi
* [ ] US9.2 – Joueurs actifs
* [ ] US9.3 – Joueurs en attente
* [ ] US9.4 – Alertes d’organisation

## En cours

* [ ] Intégration librairie JS `brackets-viewer.js`
* [ ] Développement du dashboard statistiques `/tournaments/{id}/stats`

## Terminé

* [x] Conception du modèle de données (Tournament, Event, Player, Match, Standing)
* [x] Cahier des charges complet validé
* [x] Sprint Planning MVP défini

---

# Vue Kanban — Post-MVP (Lots 2 & 3)

## À faire

* [ ] US8.1 – OCR des feuilles de match
* [ ] US8.2 – Chatbot assistant tournoi
* [ ] US8.3 – Planification automatique
* [ ] PWA mobile offline
* [ ] API publique

## En cours

* [ ] Recherche librairie OCR (Tesseract.js, PaddleOCR)
* [ ] Prototype chatbot tournoi (API GPT‑4/5 + règles FFTT)

## Terminé

* [x] Spécifications IA et automatisation ajoutées au CdC

---

**Mise à jour : Décembre 2025 — Vue Kanban simplifiée pour pilotage agile.**
