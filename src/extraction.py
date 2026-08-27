"""Fonctions d'extraction de données depuis la base GTFS."""

from src.connexion import get_connection

import pandas as pd


def get_arrets_tram():
    """Retourne les arrêts de tram avec leur ligne et leurs coordonnées."""
    query = """
            SELECT DISTINCT
                s.stop_id,
                s.stop_name,
                r.route_short_name AS route_name,
                s.stop_lat AS latitude,
                s.stop_lon AS longitude
            FROM stops s
            JOIN stop_times st
                ON s.stop_id = st.stop_id
            JOIN trips t
                ON st.trip_id = t.trip_id
            JOIN routes r
                ON t.route_id = r.route_id
            WHERE r.route_type = 0
            ORDER BY route_name, stop_name;
        """

    with get_connection() as conn:
        return pd.read_sql(query, conn)
