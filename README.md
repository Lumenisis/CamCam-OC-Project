# Administrateur Infrastructure et Cloud

# Participez à la vie de la communauté Open Source

## 1 - Présentation du projet :

Pour ce projet, j'ai créé un script en Python permettant de sauvegarder la configuration complète d'un site web réalisé avec WordPress.
La sauvegarde est tranférée par FTP depuis un serveur Linux local vers un serveur Linux distant.

## 2 - Pour commencer :

J'ai travaillé avec deux machines virtuelles, créées avec des images Ubuntu 21.04 Desktop (version Desktop parce que j'ai utilisé un IDE pour coder).
J'ai utilisé l'accès par pont pour les connexions réseau, permettant ainsi à mes machines de communiquer entre elles et d'avoir internet.
La configuration réseau sur chaque machine a été faite avec netplan.

## 3 - Pré-requis :

Pour mettre en place mon infrastructure virtuelle, voici les outils que j'ai utilisés :

- Un serveur web LAMP installé sur le serveur local
    - Linux (Ubuntu 21.04)
    - Apache (configuration dans /etc/apache2)
    - MySQL (nom de la base de données "wordpress")
    - PHP (permettant d'utiliser la base de donnée MySQL)
- Un service WordPress installé sur le serveur local (Configuration dans /var/www/wordpress)
- Un IDE PyCharm installé sur le serveur local pour coder
- Un service ProFTPd installé sur le serveur distant permettant de transférer les éléments sauvegardés

## 4 - L'IDE PyCharm et ses fonctionnalités :

J'ai utilisé cet environnement de développement pour Python parce qu'il s'agit d'un éditeur intelligent, très pratique pour les développeurs débutants.
Il comporte des outils de débogage et de test, utilisables simplement depuis l'interface graphique.
Il permet l'accès à une base de donnée, par exemple MySQL, et c'est une fonctionnalité très utile pour la réalisation d'un projet comme celui-ci.

## 5 - Présentation du code source :

Dans un premier temps, nous avons la liste des modules importés dans l'IDE. Ensuite, nous avons les variables, c'est à ce niveau que nous pouvons gérer
l'adressage IP des serveurs, le répertoire source et le répertoire de destination qui contiennent les fichiers sauvegardés, le nom de la base de données...
Concernant les fonctions, nous testons à chaque fois pour MySQL, WordPress et Apache s'il existe un répertoire de sauvegarde, s'il n'y en a pas nous en
créons un, nous sauvegardons la configuration et le tout est compressé au format .tar.gz. Puis tout le contenu du répertoire /backup du serveur local est
envoyé par FTP dans le répertoire /backup du serveur distant (il y a un test dans la fonction qui permet de ne pas copier plusieurs fois la même chose).
Pour finir, toutes les fonctions sont exécutées.

## 6 - Lancement du programme :

Avec PyCharm, nous pouvons déjà vérifier qu'il n'y a pas d'erreur de syntaxe ou d'indentation dans notre code en haut à droite de l'interface. Normalement
tout est bon, et il suffit d'exécuter le code avec la petite flèche verte. Si tout se passe bien, les répertoires choisis sont sauvegardés et envoyés
sur le serveur distant. Dans le cas contraire, il faut vérifier au niveau des variables que la configuration système ou réseau est bonne.

## Auteur :

    - Camille GASCHET
    - Étudiant chez OpenClassrooms
    - Parcours "Administrateur Infrastructure et Cloud"

## Licence :

Ce projet est sous licence ``GPL-3.0`` - voir le fichier [LICENSE.md](LICENSE.md) pour plus d'informations
