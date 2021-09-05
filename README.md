# CamCam-OC-Project

# Administrateur Infrastructure et Cloud

# Participez à la vie de la communauté Open Source

## Présentation du projet :

Pour ce projet, j'ai créé un script avec le langage Python permettant de sauvegarder la configuration complète d'un site web réalisé avec WordPress.
La sauvegarde est tranférée par FTP depuis notre serveur Linux local vers notre serveur Linux distant.

## Pour commencer :

J'ai travaillé avec deux machines virtuelles, créées avec des images Ubuntu 21.04 Desktop car j'ai utilisé un IDE pour coder.
J'ai utilisé l'accès par pont pour les connexions réseau, permettant ainsi à mes machines de communiquer entre elles et d'avoir internet.
La configuration réseau sur chaque machine a été faite avec netplan.

## Pré-requis :

Pour mettre en place mon infrastructure virtuelle, voici les outils que j'ai utilisés :

- Le serveur web LAMP installé sur le serveur local
    - Linux (Ubuntu 21.04)
    - Apache (configuration dans /etc/apache2)
    - MySQL (nom de la base de données "wordpress")
    - PHP (permettant d'utiliser la base de donnée MySQL)
- Le service WordPress installé sur le serveur local (Configuration dans /var/www/wordpress)
-  L'IDE PyCharm installé sur le serveur local pour coder
- Le service ProFTPd installé sur le serveur distant permettant de transférer les éléments sauvegardés

## L'IDE PyCharm et ses fonctionnalités :

J'ai utilisé cet environnement de développement pour Python parce qu'il s'agit d'un éditeur intelligent, très pratique pour les développeurs débutants.
Il comporte des outils de débogage et de test, utilisables simplement depuis l'interface graphique.
Il permet l'accès à une base de donnée MySQL par exemple, fonctionnalité très utile pour la réalisation de ce projet.

## Présentation du code source :



## Lancement du programme :



## Auteur :

Camille GASCHET
Étudiant chez OpenClassrooms
Parcours "Administrateur Infrastructure et Cloud"

## Licence :

Ce projet est sous licence ``GPL-3.0`` - voir le fichier [LICENSE.md](LICENSE.md) pour plus d'informations
