"""Export d'un fichier tables.md, un fichier CSV et un fichier Parquet pour le jeux des données."""

from src.cartographie import (
    # colonnes_to_dict,
    get_nombre_des_doublons,
    get_nombre_des_lignes,
    get_nombre_des_valeurs_nulles,
    tables_dict,
)


def export_tables_cartoghraphie(file_path):
    """Exporter un fichier.md."""
    tables = tables_dict()

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("# Cartographie des données\n\n")

        for table, columns in tables.items():
            # Calcul du volume
            nb_rows = get_nombre_des_lignes(table)
            columns_names = [row[0] for row in columns]

            file.write(f"## Table `{table}`\n\n")

            file.write(f"**Volume :** {nb_rows} lignes\n\n")

            if table in ("agency", "calendar", "calendar_dates", "stops"):
                columns_names = columns_names[1:]
            nb_doublons = get_nombre_des_doublons(table, columns_names)
            file.write(f"**Nombre des doublons :** {nb_doublons} lignes\n\n")

            file.write("| Colonne | Type | Nullable | Nb NULL |\n")
            file.write("|---|---|---|---:|\n")

            for colonne, data_type, nullable in columns:
                nb_nulls = get_nombre_des_valeurs_nulles(table, colonne)

                file.write(f"| `{colonne}` | {data_type} | {nullable} | {nb_nulls} |\n")

            file.write("\n")
        file.write("\n")


def export_csv(df, filename):
    """Génère un fichier CSV."""
    df.to_csv(filename, index=False, encoding="utf-8-sig")


def export_parquet(df, filename):
    """Génère un fichier Parquet."""
    df.to_parquet(filename, index=False)


def colonnes_to_markdown(data):
    """Transforme le dictionnaire des colonnes en Markdown."""
    lines = []

    lines.append("# Dictionnaire de données")
    lines.append("")
    lines.append(f"**Date d'extraction :** {data['extracted_at']}")
    lines.append("")
    lines.append("| Colonne | Type | Unité / domaine de valeurs | Source |")
    lines.append("|---|---|---|---|")
    for colonne in data["colonnes"]:
        lines.append(f"| `{colonne['name']}` | `{colonne['type']}` | À documenter | À documenter ")

    return "\n".join(lines)


def export_dictionnaire(filename, data):
    """Génère le dictionnaire de données au format Markdown."""
    markdown = colonnes_to_markdown(data)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(markdown)


# export_tables_cartoghraphie()
