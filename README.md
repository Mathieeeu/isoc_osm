# ISOC - Etude de la structure de l'Internet mondial


Dans le cadre ce projet, nous avons fait une API ainsi qu'une application principalement avec les langages python et HTML.
Le but était de réaliser une étude de la structure de l'internet mondial, en analysant les diffèrents points d'accès au réseau dans le monde ainsi que les tables de routage de chacun des points. 

Nous avons utilisé les bibliothèques Tkinter et CustomTkinter pour réaliser une interface en python.
Et OSMNX et folium pour créer une visualisation des points d'accès réseau sur une carte ainsi que tout l'aspect géographique (calculs de distance)


## Fonctionnement

### Application

L'application est composée d'une partie front end et d'une partie back end. 
Lors du lancement du programme, une fenêtre s'ouvre afin de dialoguer avec l'utilisateur. Ce dernier peut alors rentrer le nom d'une ville (celle dont il veut les points d'accès internet), un rayon de recherche maximum pour les différents points. Il est aussi possible de selectionner les pays dans lesquels les points de d'acces seront recherchés. 
Une fois les informations saisies, une nouvelle fenêtre, contenant les résultats, s'ouvre. Celle-ci contient tous les points IXP trouvés, le pourcentage de couverture réseau, le pourcentage de connexion des routeurs ainsi que le nombre de points triés par distance. Un bouton permet également d'ouvrir un navigateur web pour visionner une carte contenant les points d'accès répondant aux critères remplis précedemment. Lorsque que l'on clique sur un point, nous pouvons savoir son nom ainsi que sa distance à la ville rentrée à l'étape d'avant.
### API







## Installation

pour le l'installation il faut telecharger les fichier présent sur le git et ouvrir le fichier FentreISOC afin de lancée l'apllication 
en se qui conserne l'API il faut 
