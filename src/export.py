"""Export d'un fichier tables.md, un fichier CSV et un fichier Parquet pour le jeux des données."""

from pathlib import Path

from src.carthographie import (
    get_nombre_des_lignes,
    get_nombre_des_valeurs_nulles,
    tables_dict,
)

ROOT_DIR = Path(__file__).resolve().parent.parent
DOC_DIR = ROOT_DIR / "docs"

DOC_DIR.mkdir(exist_ok=True)

file_path = DOC_DIR / "cartographie_donnees.md"


def export_tables_cartoghraphie():
    """Exporter un fichier.md."""
    tables = tables_dict()
    roles = {
        "agency": "Décrit les agences de transport et leurs informations générales.",
        "calendar": "Définit les jours et la période de circulation des services de transport.",
        "calendar_dates": """Définit les exceptions de calendrier,
                            en ajoutant ou supprimant des dates de circulation pour un service.""",
        "routes": "Décrit les lignes ou itinéraires de transport proposés par les agences.",
        "stop_times": "Décrit les horaires de passage des trajets à chaque arrêt.",
        "stops": "Décrit les arrêts et leurs informations géographiques.",
        "transfers": """Décrit les possibilités de correspondance entre deux arrêts 
                        et les conditions de transfert.""",
        "trips": "Décrit les trajets associés à une ligne et à un calendrier de service.",
    }

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("# Cartographie des données\n\n")

        for table, columns in tables.items():
            # Calcul du volume
            nb_rows = get_nombre_des_lignes(table)

            file.write(f"## Table `{table}`\n\n")

            role = roles.get(table, "Description non renseignée.")
            file.write(f"**Rôle :** {role}\n\n")

            file.write(f"**Volume :** {nb_rows} lignes\n\n")

            file.write("| Colonne | Type | Nullable | Nb NULL |\n")
            file.write("|---|---|---|---:|\n")

            for colonne, data_type, nullable in columns:
                nb_nulls = get_nombre_des_valeurs_nulles(table, colonne)

                file.write(f"| `{colonne}` | {data_type} | {nullable} | {nb_nulls} |\n")

            file.write("\n")


export_tables_cartoghraphie()
