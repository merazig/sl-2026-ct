"""Gestion de la connexion à PostgreSQL."""

import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """Crée et retourne une connexion à PostgreSQL."""
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise RuntimeError("DATABASE_URL n'est pas définie.")

    try:
        return psycopg2.connect(database_url)
    except psycopg2.OperationalError as exc:
        raise RuntimeError("Impossible de se connecter à la base PostgreSQL.") from exc
