# Deployez un modèle dans le cloud

Une start-up souhaite dans un premier temps se faire connaître en mettant à disposition du grand public
une application mobile qui permettrait aux utilisateurs de prendre en photo un fruit et d'obtenir des informations sur ce fruit.

Pour la start-up, cette application permettrait de sensibiliser le grand public à la biodiversité des fruits et
de mettre en place une première version du moteur de classification des images de fruits.

De plus, le développement de l’application mobile permettra de construire une première version de l'architecture Big Data nécessaire.

# Les données
Le [jeu de donnée](https://www.kaggle.com/moltean/fruits) constitué des images de fruits et des labels associés,
qui pourra servir de point de départ pour construire une partie de la chaîne de traitement des données.

# Mission
Développer dans un environnement Big Data une première chaîne de traitement des données qui comprendra le preprocessing et une étape de réduction de dimension.

# Contraintes

le volume de données va augmenter très rapidement après la livraison de ce projet.
Développerez des scripts en Pyspark et utiliserez par exemple le cloud AWS pour profiter d’une architecture Big Data (EC2, S3, IAM), 
basée sur un serveur EC2 Linux.
La mise en œuvre d’une architecture Big Data sous (par exemple) AWS peut nécessiter une configuration serveur plus puissante que
celle proposée gratuitement (EC2 = t2.micro, 1 Go RAM, 8 Go disque serveur).

# Livrables
* Un notebook sur le cloud contenant les scripts en Pyspark exécutables (le preprocessing et une étape de réduction de dimension).
* Un support de présentation 
