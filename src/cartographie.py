"""Cartographier la base avec du code."""

from src.connexion import get_connection

from datetime import datetime


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


def get_colonnes():
    """Liste les colonnes et les types de toutes les tables."""
    query = """
        SELECT
            table_name,
            column_name,
            data_type,
            is_nullable
        FROM information_schema.columns
        WHERE table_schema = 'public'
        ORDER BY table_name, ordinal_position;
    """

    with get_connection() as conn, conn.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


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


def get_nombre_des_doublons(table, colonnes):
    """Nombre des doublons."""
    colonnes_sql = ", ".join(colonnes)

    query = f"""
            SELECT COUNT(*)
            FROM (
                SELECT {colonnes_sql}
                FROM {table}
                GROUP BY {colonnes_sql}
                HAVING COUNT(*) > 1
            ) AS doublons;
        """

    with get_connection() as conn, conn.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchone()[0]


def tables_dict():
    """Retourne les informations des tables pour la cartographie."""
    tables = {}

    for table, column, data_type, is_nullable in get_colonnes():
        tables.setdefault(table, []).append((column, data_type, is_nullable))

    return tables


def colonnes_to_dict():
    """Retourne les informations sur les colonnes."""
    colonnes = []

    for table, column, data_type, is_nullable in get_colonnes():
        colonnes.append(
            {"name": column, "type": data_type, "is_nullable": is_nullable, "table": table}
        )

    return {"colonnes": colonnes, "extracted_at": datetime.now().strftime("%d/%m/%Y à %H:%M:%S")}


# print(tables_dict())
