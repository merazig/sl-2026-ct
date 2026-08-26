"""Export d'un fichier tables.md, un fichier CSV et un fichier Parquet pour le jeux des données."""

from pathlib import Path
from textwrap import dedent

from src.cartographie import (
    get_nombre_des_doublons,
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

    notes = """
            ## Définitions et méthode d'analyse

            ### Doublon

            Dans cette cartographie, un doublon désigne plusieurs lignes ayant les mêmes valeurs 
            pour l'ensemble des colonnes retenues pour l'analyse de la table, indépendamment 
            de leur identifiant.

            Un doublon détecté de cette manière constitue un **doublon potentiel** et ne signifie
            pas nécessairement une erreur dans les données. Plusieurs enregistrements présentant 
            les mêmes caractéristiques peuvent être légitimes selon le contexte métier.

            ### Valeurs NULL

            Le nombre de valeurs NULL correspond au nombre de lignes pour lesquelles 
            une colonne ne contient aucune valeur.

            Une colonne déclarée comme nullable dans le schéma n'implique pas nécessairement 
            qu'elle contient effectivement des valeurs NULL.

            ### Valeurs aberrantes

            Une valeur est considérée comme aberrante lorsqu'elle semble inhabituelle 
            ou incohérente au regard des règles métier ou du domaine étudié. 
            Une valeur inhabituelle n'est toutefois pas nécessairement invalide.

            Dans le cas du GTFS, certaines valeurs peuvent notamment respecter des conventions 
            spécifiques au format. Par exemple, des horaires supérieurs à `24:00:00` 
            peuvent être valides et ne doivent donc pas être considérés automatiquement 
            comme aberrants.
            """
    
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("# Cartographie des données\n\n")

        for table, columns in tables.items():
            # Calcul du volume
            nb_rows = get_nombre_des_lignes(table)
            columns_names = [row[0] for row in columns]
            
            file.write(f"## Table `{table}`\n\n")

            role = roles.get(table, "Description non renseignée.")
            file.write(f"**Rôle :** {role}\n\n")

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
        file.write(dedent(notes))
        file.write("\n")


def export_csv(df, filename):
    """Génère un fichier CSV."""
    df.to_csv(filename, index=False, encoding="utf-8-sig")


def export_parquet(df, filename):
    """Génère un fichier Parquet."""
    df.to_parquet(filename, index=False)
    
export_tables_cartoghraphie()