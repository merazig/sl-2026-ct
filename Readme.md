# Extraction et documentation de données GTFS

## Présentation

Ce projet a pour objectif d'explorer et de documenter une base de données
GTFS d'Île-de-France contenant notamment des données relatives au métro,
au RER et au tram.

Le projet suit trois étapes principales :

1. cartographier la base de données avec du code ;
2. extraire un jeu de données répondant à un cas d'usage précis ;
3. documenter et exporter ce jeu de données afin de faciliter sa réutilisation.

La base de données est une base PostgreSQL hébergée sur Scalingo.

## Cas d'usage

Le jeu de données extrait concerne les **arrêts de tram d'Île-de-France**.

Pour chaque arrêt et chaque ligne de tram desservant cet arrêt, le jeu de
données contient :

- l'identifiant de l'arrêt ;
- le nom de l'arrêt ;
- le nom de la ligne ;
- la latitude ;
- la longitude.

Une ligne du jeu de données correspond donc à une combinaison **arrêt × ligne
de tram**. Un même arrêt peut ainsi apparaître plusieurs fois lorsqu'il est
desservi par plusieurs lignes.

Le filtrage des lignes de tram est effectué à partir de `route_short_name`
et du préfixe `T`. Les lignes dont le nom commence par `T` sont retenues.

## Source des données

Les données proviennent d'une base PostgreSQL contenant des données au format
GTFS d'Île-de-France.

La connexion à la base est réalisée à partir de variables d'environnement
afin de ne pas stocker les informations de connexion dans le code.

Les principales tables utilisées pour l'extraction sont :

- `stops` : informations sur les arrêts et leurs coordonnées ;
- `stop_times` : association entre les arrêts et les trajets ;
- `trips` : trajets associés aux lignes ;
- `routes` : informations sur les lignes de transport.

La cartographie complète des tables de la base est disponible dans
`doc/cartographie_donnees.md`.

## Structure du projet

```text
├── main.py
├── src/
│   ├── __init__.py
│   ├── connexion.py
│   ├── cartographie.py
│   ├── extraction.py
│   └── export.py
│
├── doc/
│   ├── cartographie_donnees.md
│   └── dictionnaire_donnees.md
│
├── data/
│   ├── tram_stops.csv
│   └── tram_stops.parquet
│
├── .env.example
├── requirements.txt
└── README.md
```
Les fichiers CSV et Parquet du dossier `data/` sont générés par le programme
et ne sont pas versionnés dans Git.

## Cartographie de la base
La première étape consiste à explorer automatiquement la base PostgreSQL.

Le programme utilise notamment le `schéma information_schema` afin
d'identifier les tables, les colonnes et leurs types.

La cartographie contient notamment :

- les tables présentes dans la base ;
- les colonnes ;
- les types de données ;
- la volumétrie ;
- le nombre de valeurs NULL ;
- un premier contrôle des doublons ;
- des constats sur la qualité et les particularités des données.
Le document généré est disponible dans :
```
doc/cartographie_donnees.md
```

## Jeu de données extrait
Le jeu de données est généré à partir d'une requête SQL effectuant les
jointures nécessaires entre les tables `stops`, `stop_times`, `trips` et
`routes`.

Les données sont exportées dans deux formats :
```
data/tram_stops.csv
data/tram_stops.parquet
```
Le CSV est adapté à la consultation, au partage et à l'utilisation avec
de nombreux outils.

Le format Parquet est un format colonnaire mieux adapté aux traitements
analytiques et permet notamment une meilleure compression et une lecture
efficace des colonnes.

Pour un jeu de données de taille limitée, le CSV peut suffire. Lorsque les
volumes augmentent ou que les données doivent être utilisées dans des
traitements analytiques, Parquet devient plus intéressant.

## Dictionnaire de données
Le dictionnaire de données décrit les colonnes du jeu de données extrait.

Il permet à une personne qui ne connaît pas la base source de comprendre
et d'utiliser les données sans devoir connaître la structure PostgreSQL
d'origine.

Pour chaque colonne, le dictionnaire précise notamment :

- son nom ;
- son type ;
- son unité ou domaine de valeurs ;
- sa source ;
- la date et l'heure d'extraction.

Le dictionnaire est disponible dans :
```
doc/dictionnaire_donnees.md
```
La date d'extraction permet également d'identifier la fraîcheur du jeu
de données.

## Installation
Les dépendances Python sont listées dans `requirements.txt`.

Créer un environnement virtuel puis installer les dépendances :
```Bash
python -m venv env
```
Activer l'environnement virtuel.

Sous Linux/macOS :
```Bash
source env/bin/activate
```
Sous Windows :
```Bash
env\Scripts\activate
```
Installer les dépendances :
```Bash
pip install -r requirements.txt
```

## Configuration
Les paramètres de connexion à PostgreSQL sont stockés dans des variables
d'environnement.

Un fichier `.env.example` est fourni comme modèle.

Créer le fichier `.env` à partir de ce modèle et renseigner les informations
de connexion à la base PostgreSQL.

Le fichier `.env` ne doit pas être versionné.

## Génération des livrables
Depuis la racine du projet, exécuter :
```Bash
python main.py
```
Le programme permet de générer les différents livrables du projet,
notamment le jeu de données extrait en CSV et en Parquet ainsi que sa
documentation.

Les fichiers générés sont placés dans les dossiers `data/` et `doc/`.

Le jeu de données n'est pas fourni dans le repository afin de permettre
sa régénération à partir du code et de la base source.

## Réutilisation
Le jeu de données peut être utilisé pour différents besoins liés aux
arrêts de tram en Île-de-France, par exemple :

- analyse géographique des arrêts ;
- visualisation cartographique ;
- analyse de la desserte des lignes ;
- croisement avec d'autres données géographiques ou de transport.

Le dictionnaire de données doit être utilisé conjointement avec les fichiers
CSV ou Parquet afin d'interpréter correctement les colonnes et leur provenance.