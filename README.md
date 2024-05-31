# ISOC - Etude de la structure de l'Internet mondial

## Introduction
Dans le cadre ce projet, nous avons fait une API ainsi qu'une application en python.

Le but était de réaliser une étude de la structure de l'internet mondial, en analysant les diffèrents points d'accès au réseau dans le monde ainsi que les tables de routage de chacun des points. 

Nous avons utilisé la bibliothèque CustomTkinter pour réaliser une interface en python, OSMNX et folium pour créer une visualisation des points d'accès réseau sur une carte ainsi que tout l'aspect géographique (calculs de distance)

## Fonctionnement

### Application

Pour lancer l'application, exécuter le fichier `fenetreIsoc.py` pour que la fenêtre de dialogue s'ouvre.

Lors du lancement du programme, une fenêtre s'ouvre afin de dialoguer avec l'utilisateur. Ce dernier peut alors entrer le nom d'une ville (celle qui doit être le centre du périmètre de recherche) et un rayon maximum. Il est aussi possible de sélectionner les pays dans lesquels les points d'accès seront recherchés, par défaut tous les pays sont pris en compte. 

Une fois les informations saisies, une nouvelle fenêtre contenant les résultats s'ouvre. Celle-ci contient tous les points IXP trouvés, le pourcentage de couverture réseau, le pourcentage de connexion des routeurs ainsi que le nombre de points triés par distance. Un bouton permet également de visionner les différents points d'accès sur une carte OpenStreetMap. Il est possible d'obtenir les informations sur le point (ville, distance, pays, IATA...) en cliquant sur son marqueur sur la carte.

### API
Pour lancer l'API, exécutez le fichier `api.py`

Une fois le programme lancé, il est possible de faire une requête à l'API en allant à l'url suivante : `0.0.0.0:8000/ixps/<ville>/<distance>`, où `<ville>` et `<distance>` correspondent respectivement au nom de la ville qui sera le centre du cercle de rayon <distance> dans lequel les points seront cherchés.

Le résultat d'une requête est un dictionnaire avec les clés suivantes : 
- Le pourcentage de couverture
- Le nombre de points dans un petit rayon
- Le nombre de points dans un rayon moyen
- Le nombre de points dans un large rayon
- La liste des ixps dans la zone, avec pour chacun : 
  - Son identifiant
  - Sa ville
  - Sa latitude
  - Sa longitude
  - Son pays
  - Son code IATA (s'il existe)
  - Le pourcentage d'adresses IP accessibles depuis ce point

## Installation

Pour installer l'application et l'API, il faut :
- Cloner le répertoire Git avec `git clone https://github.com/Mathieeeu/isoc_osm.git`
- Importer les bibliothèques python necessaires avec `$ pip install -r requirements.txt`

## Equipe
Ce projet a été réalisé par :
- Charlotte C.
- Livio P.
- Louna C.
- Mathieu D.

=)
