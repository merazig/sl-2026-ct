# Cartographie des données

## Table `agency`

**Rôle :** Décrit les agences de transport et leurs informations générales.

**Volume :** 7 lignes

| Colonne | Type | Nullable | Nb NULL |
|---|---|---|---:|
| `agency_id` | text | NO | 0 |
| `agency_name` | text | NO | 0 |
| `agency_url` | text | YES | 0 |
| `agency_timezone` | text | YES | 0 |

## Table `calendar`

**Rôle :** Définit les jours et la période de circulation des services de transport.

**Volume :** 858 lignes

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

| Colonne | Type | Nullable | Nb NULL |
|---|---|---|---:|
| `service_id` | text | YES | 0 |
| `date` | date | YES | 0 |
| `exception_type` | smallint | YES | 0 |

## Table `routes`

**Rôle :** Décrit les lignes ou itinéraires de transport proposés par les agences.

**Volume :** 38 lignes

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

| Colonne | Type | Nullable | Nb NULL |
|---|---|---|---:|
| `from_stop_id` | text | YES | 0 |
| `to_stop_id` | text | YES | 0 |
| `transfer_type` | smallint | YES | 0 |
| `min_transfer_time` | integer | YES | 0 |

## Table `trips`

**Rôle :** Décrit les trajets associés à une ligne et à un calendrier de service.

**Volume :** 103914 lignes

| Colonne | Type | Nullable | Nb NULL |
|---|---|---|---:|
| `trip_id` | text | NO | 0 |
| `route_id` | text | YES | 0 |
| `service_id` | text | YES | 0 |
| `trip_headsign` | text | YES | 0 |
| `direction_id` | smallint | YES | 0 |

