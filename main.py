"""Cartographier la base et produire un jeu de données documenté."""

from src.export import export_dictionnaire


def main():
    """La fonction main."""
    export_dictionnaire("docs/dictionnaire_donnees.md")


if __name__ == "__main__":
    main()
