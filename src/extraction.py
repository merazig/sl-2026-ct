"""Fonctions d'extraction de données depuis la base GTFS."""

from src.connexion import get_connection

import pandas as pd
from datetime import datetime


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
            WHERE r.route_short_name LIKE 'T%'
            ORDER BY route_name, stop_name;
        """

    with get_connection() as conn:
        return pd.read_sql(query, conn)


def dataset_to_dict(df):
    """Retourne les informations sur les colonnes du jeu de données."""
    colonnes = []

    for column in df.columns:
        colonnes.append(
            {
                "name": column,
                "type": str(df[column].dtype),
            }
        )

    return {"colonnes": colonnes, "extracted_at": datetime.now().strftime("%d/%m/%Y à %H:%M:%S")}
