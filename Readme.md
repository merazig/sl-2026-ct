# Analyse et cartographie de données GTFS

## Description

Ce projet a pour objectif d'explorer, analyser et documenter une base de données
issue de données de transport au format GTFS.

L'objectif est dans un premier temps de comprendre la structure de la base,
d'identifier les différentes tables et leurs colonnes, puis de réaliser quelques
contrôles de qualité sur les données.

Le projet permettra notamment de produire :

- une cartographie des tables de la base ;
- un dictionnaire de données ;
- des indicateurs simples de qualité des données ;
- des jeux de données extraits et exploitables.

---

## Structure du projet

```text
.
├── main.py
├── src/
│   ├── __init__.py
│   ├── connexion.py
│   ├── cartographie.py
│   ├── extraction.py
│   └── export.py
│
├── doc/
│   └── cartographie_donnees.md
│
└── README.md

```

Description des fichiers
main.py

Point d'entrée du projet. Il permet d'orchestrer les différentes étapes
du traitement.

src/connexion.py

Contient les fonctions permettant d'établir une connexion à la base
de données PostgreSQL.

src/cartographie.py

Contient les fonctions permettant d'explorer la structure de la base de données.

Les informations récupérées comprennent notamment :

les tables ;
les colonnes ;
les types de données ;
la possibilité d'avoir des valeurs NULL ;
le nombre de lignes par table ;
certains contrôles de qualité.

Les informations sont récupérées notamment à partir du schéma
information_schema de PostgreSQL.

src/extraction.py

Contient les requêtes permettant d'extraire des jeux de données spécifiques
à partir de la base GTFS.

Une première extraction concerne notamment les arrêts de tram, avec :

l'identifiant de l'arrêt ;
le nom de l'arrêt ;
la ligne ;
la latitude ;
la longitude.
src/export.py

Contient les fonctions permettant d'exporter les données et les résultats
du projet dans différents formats.

Les formats envisagés comprennent notamment :

Markdown (.md) ;
CSV (.csv) ;
Parquet (.parquet).
doc/cartographie_donnees.md

Document généré automatiquement contenant la cartographie de la base de données.

Pour chaque table, le document présente notamment :

le volume de la table ;
les colonnes ;
les types ;
la possibilité d'avoir des valeurs NULL ;
le nombre de valeurs NULL.
Base de données

La base utilisée est une base PostgreSQL contenant des données de transport
au format GTFS.

Les principales tables actuellement identifiées sont :

agency
calendar
calendar_dates
routes
stop_times
stops
transfers
trips

Certaines tables sont particulièrement volumineuses. Par exemple,
stop_times contient plusieurs millions de lignes.

Premières analyses réalisées
Cartographie

Une première cartographie automatique de la base a été réalisée à partir
des catalogues PostgreSQL et du schéma information_schema.

Les informations suivantes sont actuellement récupérées :

nom des tables ;
nom des colonnes ;
type des colonnes ;
caractère nullable des colonnes ;
nombre de lignes ;
nombre de valeurs NULL.
Contrôle des doublons

Des contrôles de doublons potentiels sont également réalisés.

Un doublon potentiel correspond à plusieurs lignes présentant les mêmes
valeurs pour un ensemble de colonnes choisies pour l'analyse, indépendamment
de leur identifiant.

Par exemple, pour la table stops, les colonnes suivantes peuvent être

utilisées :

stop_name
stop_lat
stop_lon

La présence de plusieurs lignes identiques sur ces colonnes ne signifie
cependant pas nécessairement une erreur : plusieurs arrêts peuvent avoir
des caractéristiques identiques ou très proches selon le contexte.

Clés et identifiants

Les colonnes telles que stop_id, trip_id, route_id ou service_id
constituent des identifiants définis par le format GTFS.

À ce stade, les tables étudiées ne semblent pas disposer de contraintes
PRIMARY KEY ou FOREIGN KEY déclarées dans PostgreSQL.

L'unicité des identifiants est donc vérifiée directement dans les données
lorsque cela est nécessaire.

Extraction de données

Une première extraction porte sur les arrêts de tram.

Les informations extraites sont :

stop_id
stop_name
route_name
latitude
longitude

La sélection des arrêts de tram repose sur route_type = 0, conformément
à la codification GTFS utilisée.

Les tables stops, stop_times, trips et routes sont utilisées pour
relier les arrêts aux lignes qui les desservent.

Formats d'export

Les données extraites sont manipulées sous forme de DataFrame Pandas.

CSV

Le format CSV est utilisé pour produire des fichiers facilement consultables
et réutilisables, notamment avec des tableurs.

Parquet

Le format Parquet est utilisé pour conserver un format adapté à l'analyse
et au traitement de données.

Il présente notamment l'avantage de conserver les types de données et d'être
plus efficace que le CSV pour certains traitements sur des volumes importants.

Documentation

La documentation produite par le projet est actuellement organisée autour
de deux éléments :

Cartographie des données

Elle donne une vue d'ensemble de la structure de la base :

doc/cartographie_donnees.md
Dictionnaire de données

Un dictionnaire de données sera également développé afin de documenter
chaque colonne, notamment :

son nom ;
son type ;
sa signification ;
son unité ou domaine de valeurs ;
sa source ;
sa date d'extraction.

État actuel du projet
Réalisé
 Connexion à PostgreSQL
 Identification des tables
 Identification des colonnes et de leurs types
 Comptage du nombre de lignes par table
 Comptage des valeurs NULL
 Premier contrôle des doublons potentiels
 Génération d'une cartographie au format Markdown
 Première extraction de données GTFS
 Préparation des exports CSV et Parquet
À poursuivre
 Finaliser le dictionnaire de données
 Documenter les domaines de valeurs des colonnes
 Documenter les relations entre les tables
 Approfondir les contrôles de qualité
 Identifier les valeurs aberrantes
 Documenter les particularités du format GTFS
 Finaliser les jeux de données à exporter
 Améliorer et automatiser la génération des rapports

Installation

Les dépendances Python nécessaires sont notamment :

pip install pandas psycopg pyarrow

Selon l'évolution du projet, d'autres dépendances pourront être ajoutées.

Exécution

Le programme principal est lancé depuis la racine du projet :

python main.py

Les modules présents dans src/ sont utilisés par main.py.

Remarques

Le projet est actuellement en phase d'exploration et de documentation.
Le contenu du README, la structure des fichiers et les traitements pourront
évoluer au fur et à mesure de l'avancement du projet. 