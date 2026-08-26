"""Cartographier la base avec du code."""

from src.connexion import get_connection


def get_tables():
    """Liste les tables."""
    query = """
            SELECT
                DISTINCT table_name
            FROM information_schema.columns
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """

    with get_connection() as conn, conn.cursor() as cursor:
        cursor.execute(query)
        return [row[0] for row in cursor.fetchall()]

def get_colonnes(table):
    """Liste les colonnes et les types."""
    query = f"""
            SELECT
                ordinal_position,
                column_name,
                data_type,
                is_nullable
            FROM information_schema.columns
            WHERE table_schema = 'public' 
            AND table_name = '{table}'
            ORDER BY table_name, ordinal_position;
        """

    with get_connection() as conn, conn.cursor() as cursor:
        cursor.execute(query)
        return [row for row in cursor.fetchall()]


print(get_colonnes("agency"))
