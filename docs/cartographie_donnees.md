# Cartographie des données

## Table `agency`

**Rôle :** Décrit les agences de transport et leurs informations générales.

**Volume :** 7 lignes

**Nombre des doublons :** 0 lignes

| Colonne | Type | Nullable | Nb NULL |
|---|---|---|---:|
| `agency_id` | text | NO | 0 |
| `agency_name` | text | NO | 0 |
| `agency_url` | text | YES | 0 |
| `agency_timezone` | text | YES | 0 |

## Table `calendar`

**Rôle :** Définit les jours et la période de circulation des services de transport.

**Volume :** 858 lignes

**Nombre des doublons :** 155 lignes

| Colonne | Type | Nullable | Nb NULL |
|---|---|---|---:|
| `service_id` | text | NO | 0 |
| `monday` | smallint | YES | 0 |
| `tuesday` | smallint | YES | 0 |
| `wednesday` | smallint | YES | 0 |
| `thursday` | smallint | YES | 0 |
| `friday` | smallint | YES | 0 |
| `saturday` | smallint | YES | 0 |
| `sunday` | smallint | YES | 0 |
| `start_date` | date | YES | 0 |
| `end_date` | date | YES | 0 |

## Table `calendar_dates`

**Rôle :** Définit les exceptions de calendrier,
                            en ajoutant ou supprimant des dates de circulation pour un service.

**Volume :** 2603 lignes

**Nombre des doublons :** 55 lignes

| Colonne | Type | Nullable | Nb NULL |
|---|---|---|---:|
| `service_id` | text | YES | 0 |
| `date` | date | YES | 0 |
| `exception_type` | smallint | YES | 0 |

## Table `routes`

**Rôle :** Décrit les lignes ou itinéraires de transport proposés par les agences.

**Volume :** 38 lignes

**Nombre des doublons :** 0 lignes

| Colonne | Type | Nullable | Nb NULL |
|---|---|---|---:|
| `route_id` | text | NO | 0 |
| `agency_id` | text | YES | 0 |
| `route_short_name` | text | YES | 0 |
| `route_long_name` | text | YES | 0 |
| `route_type` | integer | YES | 0 |

## Table `stop_times`

**Rôle :** Décrit les horaires de passage des trajets à chaque arrêt.

**Volume :** 2219678 lignes

**Nombre des doublons :** 0 lignes

| Colonne | Type | Nullable | Nb NULL |
|---|---|---|---:|
| `trip_id` | text | NO | 0 |
| `stop_id` | text | YES | 0 |
| `arrival_time` | text | YES | 0 |
| `departure_time` | text | YES | 0 |
| `stop_sequence` | integer | NO | 0 |

## Table `stops`

**Rôle :** Décrit les arrêts et leurs informations géographiques.

**Volume :** 2396 lignes

**Nombre des doublons :** 25 lignes

| Colonne | Type | Nullable | Nb NULL |
|---|---|---|---:|
| `stop_id` | text | NO | 0 |
| `stop_name` | text | YES | 0 |
| `stop_lat` | double precision | YES | 0 |
| `stop_lon` | double precision | YES | 0 |
| `location_type` | integer | YES | 0 |
| `parent_station` | text | YES | 0 |

## Table `transfers`

**Rôle :** Décrit les possibilités de correspondance entre deux arrêts 
                        et les conditions de transfert.

**Volume :** 3441 lignes

**Nombre des doublons :** 0 lignes

| Colonne | Type | Nullable | Nb NULL |
|---|---|---|---:|
| `from_stop_id` | text | YES | 0 |
| `to_stop_id` | text | YES | 0 |
| `transfer_type` | smallint | YES | 0 |
| `min_transfer_time` | integer | YES | 0 |

## Table `trips`

**Rôle :** Décrit les trajets associés à une ligne et à un calendrier de service.

**Volume :** 103914 lignes

**Nombre des doublons :** 0 lignes

| Colonne | Type | Nullable | Nb NULL |
|---|---|---|---:|
| `trip_id` | text | NO | 0 |
| `route_id` | text | YES | 0 |
| `service_id` | text | YES | 0 |
| `trip_headsign` | text | YES | 0 |
| `direction_id` | smallint | YES | 0 |


## Définitions et méthode d'analyse

### Doublon

Dans cette cartographie, un doublon désigne plusieurs lignes ayant les mêmes valeurs 
pour l'ensemble des colonnes retenues pour l'analyse de la table, indépendamment 
de leur identifiant.

Un doublon détecté de cette manière constitue un **doublon potentiel** et ne signifie
pas nécessairement une erreur dans les données. Plusieurs enregistrements présentant 
les mêmes caractéristiques peuvent être légitimes selon le contexte métier.

### Valeurs NULL

Le nombre de valeurs NULL correspond au nombre de lignes pour lesquelles 
une colonne ne contient aucune valeur.

Une colonne déclarée comme nullable dans le schéma n'implique pas nécessairement 
qu'elle contient effectivement des valeurs NULL.

### Valeurs aberrantes

Une valeur est considérée comme aberrante lorsqu'elle semble inhabituelle 
ou incohérente au regard des règles métier ou du domaine étudié. 
Une valeur inhabituelle n'est toutefois pas nécessairement invalide.

Dans le cas du GTFS, certaines valeurs peuvent notamment respecter des conventions 
spécifiques au format. Par exemple, des horaires supérieurs à `24:00:00` 
peuvent être valides et ne doivent donc pas être considérés automatiquement 
comme aberrants.

