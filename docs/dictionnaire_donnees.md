# Dictionnaire de données

**Date d'extraction :** 27/08/2026 à 14:16:10

| Table | Colonne | Type | Nullable | Unité / domaine de valeurs | Source |
|---|---|---|---|---|---|
| `agency` | `agency_id` | `text` | NO | Identifiant unique de l'agence | GTFS:Scalingo:PostgreSQL |
| `agency` | `agency_name` | `text` | NO | Texte | GTFS:Scalingo:PostgreSQL |
| `agency` | `agency_url` | `text` | YES | URL | GTFS:Scalingo:PostgreSQL |
| `agency` | `agency_timezone` | `text` | YES | Fuseau horaire IANA, ex. Europe/Paris | GTFS:Scalingo:PostgreSQL |
| `calendar` | `service_id` | `text` | NO | Identifiant du service | GTFS:Scalingo:PostgreSQL |
| `calendar` | `monday` | `smallint` | YES | 0 ou 1 | GTFS:Scalingo:PostgreSQL |
| `calendar` | `tuesday` | `smallint` | YES | 0 ou 1 | GTFS:Scalingo:PostgreSQL |
| `calendar` | `wednesday` | `smallint` | YES | 0 ou 1 | GTFS:Scalingo:PostgreSQL |
| `calendar` | `thursday` | `smallint` | YES | 0 ou 1 | GTFS:Scalingo:PostgreSQL |
| `calendar` | `friday` | `smallint` | YES | 0 ou 1 | GTFS:Scalingo:PostgreSQL |
| `calendar` | `saturday` | `smallint` | YES | 0 ou 1 | GTFS:Scalingo:PostgreSQL |
| `calendar` | `sunday` | `smallint` | YES | 0 ou 1 | GTFS:Scalingo:PostgreSQL |
| `calendar` | `start_date` | `date` | YES | Date au format YYYYMMDD | GTFS:Scalingo:PostgreSQL |
| `calendar` | `end_date` | `date` | YES | Date au format YYYYMMDD | GTFS:Scalingo:PostgreSQL |
| `calendar_dates` | `service_id` | `text` | YES | Identifiant du service | GTFS:Scalingo:PostgreSQL |
| `calendar_dates` | `date` | `date` | YES | Date au format YYYYMMDD | GTFS:Scalingo:PostgreSQL |
| `calendar_dates` | `exception_type` | `smallint` | YES | 1 = service ajouté, 2 = service supprimé | GTFS:Scalingo:PostgreSQL |
| `routes` | `route_id` | `text` | NO | Identifiant unique de la ligne | GTFS:Scalingo:PostgreSQL |
| `routes` | `agency_id` | `text` | YES | Identifiant de l'agence | GTFS:Scalingo:PostgreSQL |
| `routes` | `route_short_name` | `text` | YES | Texte court / nom court de la ligne | GTFS:Scalingo:PostgreSQL |
| `routes` | `route_long_name` | `text` | YES | Texte / nom long de la ligne | GTFS:Scalingo:PostgreSQL |
| `routes` | `route_type` | `integer` | YES | Enumération GTFS du mode de transport | GTFS:Scalingo:PostgreSQL |
| `stop_times` | `trip_id` | `text` | NO | Identifiant du trajet| GTFS:Scalingo:PostgreSQL |
| `stop_times` | `stop_id` | `text` | YES | Identifiant de l'arrêt | GTFS:Scalingo:PostgreSQL |
| `stop_times` | `arrival_time` | `text` | YES | Heure HH:MM:SS, pouvant dépasser 24:00:00 | GTFS:Scalingo:PostgreSQL |
| `stop_times` | `departure_time` | `text` | YES | Heure HH:MM:SS, pouvant dépasser 24:00:00| GTFS:Scalingo:PostgreSQL |
| `stop_times` | `stop_sequence` | `integer` | NO | Entier positif représentant l'ordre de passage | GTFS:Scalingo:PostgreSQL |
| `stops` | `stop_id` | `text` | NO | Identifiant unique de l'arrêt | GTFS:Scalingo:PostgreSQL |
| `stops` | `stop_name` | `text` | YES | Texte | GTFS:Scalingo:PostgreSQL |
| `stops` | `stop_lat` | `double precision` | YES | Latitude WGS84 en degrés décimaux, -90 à 90 | GTFS:Scalingo:PostgreSQL |
| `stops` | `stop_lon` | `double precision` | YES | Longitude WGS84 en degrés décimaux, -180 à 180 | GTFS:Scalingo:PostgreSQL |
| `stops` | `location_type` | `integer` | YES | Enumération GTFS | GTFS:Scalingo:PostgreSQL |
| `stops` | `parent_station` | `text` | YES | Identifiant d'un arrêt/station parent | GTFS:Scalingo:PostgreSQL |
| `transfers` | `from_stop_id` | `text` | YES | Identifiant d'arrêt | GTFS:Scalingo:PostgreSQL |
| `transfers` | `to_stop_id` | `text` | YES | Identifiant d'arrêt | GTFS:Scalingo:PostgreSQL |
| `transfers` | `transfer_type` | `smallint` | YES | Enumération GTFS | GTFS:Scalingo:PostgreSQL |
| `transfers` | `min_transfer_time` | `integer` | YES | Secondes | GTFS:Scalingo:PostgreSQL |
| `trips` | `trip_id` | `text` | NO | Identifiant unique du trajet | GTFS:Scalingo:PostgreSQL |
| `trips` | `route_id` | `text` | YES | Identifiant de ligne | GTFS:Scalingo:PostgreSQL |
| `trips` | `service_id` | `text` | YES | Identifiant du service | GTFS:Scalingo:PostgreSQL |
| `trips` | `trip_headsign` | `text` | YES | Texte indiquant la destination affichée | GTFS:Scalingo:PostgreSQL |
| `trips` | `direction_id` | `smallint` | YES | 0 ou 1 | GTFS:Scalingo:PostgreSQL |