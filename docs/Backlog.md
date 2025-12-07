# Backlog produit – Application Ping Manager

## Structure du backlog

* **Epics** : grandes thématiques fonctionnelles (niveau produit).
* **Features** : fonctionnalités livrables dans un lot ou sprint.
* **User Stories** : tâches concrètes à implémenter avec critères d’acceptation.

---

## EPIC 1 : Gestion des tournois

**Objectif :** Permettre la création, modification et gestion complète d’un tournoi FFTT.

### Features

* Création et chargement de tournoi.
* Import configuration JSON/YAML.
* Gestion multi-tableaux.

### User Stories

1. **US1.1 – Créer un tournoi**
   *En tant qu’organisateur, je veux créer un tournoi avec nom, date et options pour pouvoir démarrer un nouveau tournoi.*
   **Critères :** formulaire valide, enregistrement DB, redirection dashboard.

2. **US1.2 – Charger un tournoi existant**
   *En tant qu’organisateur, je veux recharger un tournoi enregistré pour le poursuivre.*

3. **US1.3 – Importer configuration JSON/YAML**
   *En tant qu’organisateur, je veux importer une configuration pour pré-remplir les tableaux.*

---

## EPIC 2 : Gestion des joueurs et inscriptions

**Objectif :** Gérer les participants et leurs inscriptions aux différents tableaux.

### Features

* Import CSV joueurs.
* Validation et dédoublonnage.
* Gestion FFTT (licence, points, club).

### User Stories

1. **US2.1 – Import CSV joueurs**
   *En tant qu’organisateur, je veux importer la liste des joueurs via un fichier CSV.*
   **Critères :** contrôle colonnes, max_events_per_player, rapport erreurs.

2. **US2.2 – Modifier un joueur**
   *Je veux corriger les infos d’un joueur depuis l’interface.*

3. **US2.3 – Visualiser la liste des joueurs inscrits**
   *Je veux voir les joueurs triés par points FFTT.*

---

## EPIC 3 : Génération des poules

**Objectif :** Créer les poules automatiquement et permettre des ajustements manuels.

### Features

* Algorithme de serpent.
* Gestion anti-club.
* Drag & drop d’ajustement.

### User Stories

1. **US3.1 – Générer les poules automatiquement**
   *En tant qu’organisateur, je veux générer les poules selon les seeds FFTT.*

2. **US3.2 – Ajuster manuellement les poules**
   *Je veux pouvoir déplacer des joueurs entre poules sans rompre les règles.*

3. **US3.3 – Verrouiller la génération**
   *Je veux pouvoir verrouiller les poules pour éviter des changements accidentels.*

---

## EPIC 4 : Phase éliminatoire (TED)

**Objectif :** Générer et visualiser le tableau à élimination directe.

### Features

* Placement croisé (A1–B2, etc.).
* Affichage graphique via brackets-viewer.js.
* Recalcul automatique après forfait.

### User Stories

1. **US4.1 – Générer le TED depuis les poules**
   *Je veux générer le TED avec les deux premiers de chaque poule.*

2. **US4.2 – Afficher le TED**
   *Je veux visualiser le TED sur une page interactive.*

3. **US4.3 – Modifier manuellement le TED**
   *Je veux pouvoir ajuster le placement avant validation.*

---

## EPIC 5 : Gestion des matchs et scores

**Objectif :** Saisir, modifier et valider les scores des matchs.

### Features

* Saisie manuelle des scores.
* Recalcul automatique des classements.
* Historique et verrouillage.

### User Stories

1. **US5.1 – Saisir les scores**
   *En tant qu’arbitre, je veux saisir les scores d’un match pour mettre à jour la poule.*

2. **US5.2 – Modifier un score validé (admin)**
   *En tant qu’admin, je peux corriger une erreur de score.*

3. **US5.3 – Recalcul automatique**
   *Le classement et le TED sont mis à jour automatiquement après modification.*

---

## EPIC 6 : Impression et export

**Objectif :** Fournir les documents nécessaires au bon déroulement du tournoi.

### Features

* Impression feuilles de match (poules/TED).
* Export CSV JSON.
* Export SPID FFTT.

### User Stories

1. **US6.1 – Imprimer feuilles de match**
   *Je veux imprimer toutes les feuilles d’une poule ou d’un tour.*

2. **US6.2 – Exporter les résultats SPID FFTT**
   *Je veux exporter les simples validés au format FFTT.*

3. **US6.3 – Générer un rapport global du tournoi (CSV/JSON)**
   *Je veux exporter l’ensemble des données pour archivage.*

---

## EPIC 7 : Expérience utilisateur et accessibilité

**Objectif :** Offrir une interface fluide, accessible et responsive.

### Features

* Responsive design.
* i18n FR/EN.
* Accessibilité AA.

### User Stories

1. **US7.1 – Interface responsive mobile**
   *L’application doit être utilisable sur smartphone pour la saisie de scores.*

2. **US7.2 – Accessibilité clavier et contraste**
   *Toutes les actions doivent être accessibles sans souris.*

---

## EPIC 8 : Évolutions IA et automatisation (Futur)

**Objectif :** Automatiser et enrichir l’application.

### Features futures

* OCR IA pour lecture des feuilles.
* Chatbot assistant tournoi.
* Planification automatique.

### User Stories

1. **US8.1 – OCR des feuilles de match**
   *Je veux photographier une feuille et que le système reconnaisse les scores.*

2. **US8.2 – Chatbot assistant**
   *Je veux poser des questions sur le tournoi (poules, scores, rappels).*

3. **US8.3 – Planification automatique**
   *Je veux que les matchs soient affectés à des tables et horaires disponibles.*

---

**Fin du backlog – version initiale (Décembre 2025)**

---

## EPIC 9 : Statistiques et alertes de suivi du tournoi

**Objectif :** Fournir à l’organisateur une vision en temps réel de l’avancement du tournoi et l’aider à fluidifier son déroulement grâce à des indicateurs et alertes.

### Features

* Tableau de bord statistiques.
* Calcul automatique des indicateurs clés.
* Système d’alertes et notifications.

### User Stories

1. **US9.1 – Consulter les statistiques générales du tournoi**
   *En tant qu’organisateur, je veux visualiser le nombre total de matchs, matchs joués et restants afin de suivre la progression.*
   **Indicateurs :** nb total matchs, nb joués, nb restants, taux de complétion, temps moyen par match.

2. **US9.2 – Identifier les joueurs les plus actifs**
   *Je veux savoir quels joueurs ont disputé le plus de matchs pour anticiper la fatigue et l’organisation.*

3. **US9.3 – Détecter les joueurs en attente depuis longtemps**
   *Je veux identifier les joueurs dont le dernier match remonte à longtemps pour fluidifier la rotation des tables.*
   **Calcul :** durée depuis dernier match > seuil paramétrable (ex : 20 min) → alerte visuelle.

4. **US9.4 – Alertes et notifications d’organisation**
   *Je veux recevoir des alertes automatiques si le tournoi prend du retard ou si des déséquilibres sont détectés.*
   **Exemples :** retard global, table inoccupée > X minutes, joueur en double attente, poule incomplète.

5. **US9.5 – Export des statistiques**
   *Je veux pouvoir exporter les statistiques globales du tournoi au format CSV ou JSON.*

### Données calculées

| Indicateur              | Description                                          |
| ----------------------- | ---------------------------------------------------- |
| **matchs_total**        | Nombre total de matchs planifiés (poules + TED).     |
| **matchs_joués**        | Nombre de matchs avec statut « terminé ».            |
| **matchs_restants**     | Différence totale.                                   |
| **taux_progression**    | Ratio matchs_joués / matchs_total.                   |
| **joueurs_actifs_top5** | Joueurs ayant disputé le plus de matchs.             |
| **joueurs_en_attente**  | Liste triée par temps écoulé depuis dernier match.   |
| **tables_inactives**    | Tables sans match en cours depuis plus de X minutes. |

### Technologies et intégration

* Calculs périodiques via tâche planifiée (Celery beat ou cron).
* Alertes visuelles (icônes + bandeau) + notifications locales navigateur.
* Historisation journalière (séries temporelles).
* Export CSV/JSON via bouton « Exporter statistiques ».

### Critères d’acceptation

* Tableau de bord accessible depuis `/tournaments/{id}/stats`.
* Données rafraîchies automatiquement toutes les 30 s.
* Alertes affichées clairement avec couleurs (vert = normal, orange = attention, rouge = critique).
* Export CSV/JSON fonctionnel.

---

---

## Maquette fonctionnelle — Page **Statistiques & Alertes**

**URL :** `/tournaments/{id}/stats`
**Objectif :** donner à l’organisateur une vision temps réel et des alertes actionnables.

### 1) Layout (wireframe fonctionnel)

* **Header**

  * Titre + sélecteur d’**Event** (Tous | SEN | VET …) + **Phase** (Poules | TED | Toutes)
  * Boutons : **Exporter CSV**, **Exporter JSON**, **Rafraîchir** (auto 30 s / manuel)
* **KPI Cards (4)**

  * `Matchs total` | `Matchs joués` | `Matchs restants` | `Taux progression %`
* **Section A — Avancement global**

  * Barre de progression + mini-sparklines (matchs/j effectués sur 60 min)
* **Section B — Joueurs**

  * **Top joueurs actifs** (table 5 lignes : Joueur, Club, Matchs joués, Dernier match il y a …)
  * **Joueurs en attente** (table scrollable : Joueur, Club, Dernier match, Attente, Nb matchs prévus restants)
* **Section C — Tables** (si la notion de table est activée)

  * `Tables inactives > X min` (liste) + `Taux d’occupation` (% du temps depuis T‑0)
* **Section D — Alertes**

  * Liste triée par sévérité : **critique** (rouge), **attention** (orange), **info** (bleu)
  * Actions rapides : *Accuser réception*, *Masquer 15 min*, *Ouvrir la page liée*

> Mobile : KPI en 2 colonnes, sections en accordéons.

### 2) Filtres & interactions

* Filtres globaux : **Event**, **Phase**, **Plage horaire** (Dernière heure | 3h | Aujourd’hui)
* Auto‑refresh 30 s (toggle ON/OFF) + bouton **Rafraîchir**
* Export : **CSV** et **JSON** reflétant les filtres courants

### 3) Contrat d’API `/api/tournaments/{id}/stats`

```json
{
  "tournament_id": 12,
  "generated_at": "2025-12-07T06:40:00+04:00",
  "filters": {"event": "ALL", "phase": "ALL", "window": "1h"},
  "kpis": {
    "matches_total": 128,
    "matches_done": 46,
    "matches_left": 82,
    "progress_pct": 35.9
  },
  "players": {
    "top_active": [
      {"player_id": 101, "name": "A. Durand", "club": "USC", "played": 5, "last_match_ago_min": 8},
      {"player_id": 102, "name": "B. Martin", "club": "USC", "played": 4, "last_match_ago_min": 5}
    ],
    "waiting": [
      {"player_id": 207, "name": "C. Leroy", "club": "ASTT", "last_match_at": "2025-12-07T05:55:00+04:00", "waiting_min": 45, "remaining": 2}
    ]
  },
  "tables": {
    "inactive_over_threshold": [
      {"table": "T3", "inactive_min": 22}
    ],
    "utilization_pct": 74.5
  },
  "alerts": [
    {"id": "AL-0093", "severity": "critical", "code": "DELAY_GLOBAL", "message": "Retard global estimé 35 min", "href": "/tournaments/12/schedule", "acknowledged": false},
    {"id": "AL-0112", "severity": "warning", "code": "PLAYER_WAIT_LONG", "message": "C. Leroy en attente depuis 45 min", "href": "/tournaments/12/players/207", "acknowledged": false}
  ]
}
```

### 4) Définitions de calcul (MVP)

* `matches_total` = nb de **Match** planifiés (filtre phase/event)
* `matches_done` = nb de **Match.status = completed**
* `matches_left` = `total - done`
* `progress_pct` = `done / max(total,1) * 100`
* `top_active` = joueurs triés par `count(matches completed)` desc (top 5)
* `waiting` = joueurs triés par `now - last_completed_match_at` desc (≥ seuil)
* `inactive_over_threshold` = tables dont `now - last_activity_at` ≥ seuil
* `utilization_pct` = `temps_occupé / temps_total_observé`

### 5) Règles d’alertes (par défaut)

* **DELAY_GLOBAL (critique)** : si `progress_pct` en dessous de la courbe théorique de plus de **15 points** sur la dernière heure
* **PLAYER_WAIT_LONG (warning)** : joueur `waiting_min ≥ 25`
* **TABLE_IDLE (warning)** : table inactive `≥ 15 min`
* **UNBALANCED_LOAD (info)** : écart `écart-type(matches par table) ≥ 1.5`

> Paramétrables dans `/settings` (seuils, activation).

### 6) Implémentation (indicative)

* **Endpoint** Django REST (ou view JSON) : agrégations via ORM + annotations, cache 15–30 s
* **Tâches planifiées** (Celery beat) pour calculs lourds / historisation
* **Front** : composant HTMX (MVP) ou pour tables triables et ack alertes
* **Accessibilité** : tableaux avec entêtes `<th scope="col">`, focus visible, messages ARIA live pour alertes

### 7) Critères d’acceptation

* Page accessible aux rôles `organisateur` et `admin`
* KPI exacts sur un jeu de données de test connu (tests d’or)
* Alertes créées/supprimées correctement selon franchissement des seuils
* Export CSV et JSON reproduisent fidèlement les KPI et listes visibles
