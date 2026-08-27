# Dictionnaire de données

**Date d'extraction :** 27/08/2026 à 14:16:10

| Table | Colonne | Type | Nullable | Unité / domaine de valeurs | Source |
|---|---|---|---|---|---|
| `agency` | `agency_id` | `text` | NO | À documenter | GTFS:Scalingo:PostgreSQL |
| `agency` | `agency_name` | `text` | NO | À documenter | GTFS:Scalingo:PostgreSQL |
| `agency` | `agency_url` | `text` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `agency` | `agency_timezone` | `text` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `calendar` | `service_id` | `text` | NO | À documenter | GTFS:Scalingo:PostgreSQL |
| `calendar` | `monday` | `smallint` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `calendar` | `tuesday` | `smallint` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `calendar` | `wednesday` | `smallint` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `calendar` | `thursday` | `smallint` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `calendar` | `friday` | `smallint` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `calendar` | `saturday` | `smallint` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `calendar` | `sunday` | `smallint` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `calendar` | `start_date` | `date` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `calendar` | `end_date` | `date` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `calendar_dates` | `service_id` | `text` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `calendar_dates` | `date` | `date` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `calendar_dates` | `exception_type` | `smallint` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `routes` | `route_id` | `text` | NO | À documenter | GTFS:Scalingo:PostgreSQL |
| `routes` | `agency_id` | `text` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `routes` | `route_short_name` | `text` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `routes` | `route_long_name` | `text` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `routes` | `route_type` | `integer` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `stop_times` | `trip_id` | `text` | NO | À documenter | GTFS:Scalingo:PostgreSQL |
| `stop_times` | `stop_id` | `text` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `stop_times` | `arrival_time` | `text` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `stop_times` | `departure_time` | `text` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `stop_times` | `stop_sequence` | `integer` | NO | À documenter | GTFS:Scalingo:PostgreSQL |
| `stops` | `stop_id` | `text` | NO | À documenter | GTFS:Scalingo:PostgreSQL |
| `stops` | `stop_name` | `text` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `stops` | `stop_lat` | `double precision` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `stops` | `stop_lon` | `double precision` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `stops` | `location_type` | `integer` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `stops` | `parent_station` | `text` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `transfers` | `from_stop_id` | `text` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `transfers` | `to_stop_id` | `text` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `transfers` | `transfer_type` | `smallint` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `transfers` | `min_transfer_time` | `integer` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `trips` | `trip_id` | `text` | NO | À documenter | GTFS:Scalingo:PostgreSQL |
| `trips` | `route_id` | `text` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `trips` | `service_id` | `text` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `trips` | `trip_headsign` | `text` | YES | À documenter | GTFS:Scalingo:PostgreSQL |
| `trips` | `direction_id` | `smallint` | YES | À documenter | GTFS:Scalingo:PostgreSQL |