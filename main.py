"""Cartographier la base et produire un jeu de données documenté."""

from src.export import (
    export_csv,
    export_dictionnaire,
    export_parquet,
    # export_tables_cartoghraphie
)

from src.extraction import dataset_to_dict, get_arrets_tram


def main():
    """La fonction main."""
    """
    J'ai commenté cette fonction et j'ai changé les nom de fichier.
    Cette fonction sert à générer un fichier md qui contient des informations 
    sur les tables et les colonnes.
    Cela permet de réduire le temps de rédaction.
    """
    # export_tables_cartoghraphie("docs/cartographie_exemple.md")

    """La récupération du jeux de données dans un dataframe"""
    df = get_arrets_tram()
    colonnes_dict = dataset_to_dict(df)
    """
    Cette fonction aide à rédiger le dictionnaire. J'ai changé le nom de fichier 
    pour ne pas remplacer le fichier livré.
    """
    export_dictionnaire("docs/dictionnaire_colonnes_arrêts_tram2.md", colonnes_dict)

    """
    Ces fonctions transforment le dataframe des arrêts des trams,
    aux fichiers csv et parquet.
    """
    export_csv(df, "data/tram_stops.csv")
    export_parquet(df, "data/tram_stops.parquet")


if __name__ == "__main__":
    main()
