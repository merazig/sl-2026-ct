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
    """Liste les colonnes et les types d'une table."""
    query = f"""
            SELECT
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


def get_nombre_des_lignes(table):
    """Le nombre des lignes d'une table."""
    query = f"""
            SELECT
                count(*)
            FROM {table}
        """

    with get_connection() as conn, conn.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchone()[0]


def get_nombre_des_valeurs_nulles(table, colonne):
    """Le nombre des valeurs nulles d'une colonnes."""
    query = f"""
            SELECT
                count(*)
            FROM {table}
            WHERE '{colonne}' IS NULL;
        """

    with get_connection() as conn, conn.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchone()[0]


def tables_dict():
    """Les infos des tables qui seront utiisées pour créer un fichier de cartographie."""
    tables = {}
    tables_names = get_tables()
    for name in tables_names:
        colonnes = get_colonnes(name)
        tables[name] = colonnes

    return tables


# print(tables_dict())
