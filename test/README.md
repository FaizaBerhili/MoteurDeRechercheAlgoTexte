# Projet Moteur de Recherche (Algorithme des Textes)  

## Exécution  

Pour exécuter le projet  

1. Veuillez installer préalablement les bibliothèques nécessaires grâce aux commandes suivantes :    

pip install rank_bm25  
pip install unidecode  
pip install bs4  
pip install textdistance  
pip install flask  
pip install numpy  
  
**OU**  
  
pip3 install rank_bm25  
pip3 install unidecode  
pip3 install bs4  
pip3 install textdistance  
pip3 install flask  
pip3 install numpy  


2. Puis :   

- Démarrer un Terminal   
- Aller dans le repertoire /src qui contient les fichiers (cd le_chemin_avant_test/test/) 
- Lancer (une fois pour toute) la commande : python supprimeSimilaireTEST.py (ou python3 supprimeSimilaireTEST.py) pour supprimer les pages trop similaires
- Lancer la commande : python serverWeb_test.py (ou python3 serverWeb_test.py)
- Le server se lance avec le message : "Running on http://localhost:8090/" (si vous êtes en local)  
(Le lancement du serveur peut être long dû à la création de l'index inversé de milliers de fichier)  
- Ouvrer votre navigateur et entrer http://localhost:8090 ou localhost:8090  
- Le navigateur JuAmEm se lance  
	- (Si vous avez le message "La connexion a échoué", regarder si votre serveur Web est bien lancé dans le terminal)  
- Vous pouvez effectuer des recherches sur le navigateur   
	- Si une recherche VIDE est effectué, le navigateur ne lance aucune recherche  
	- Si une recherche NON VIDE est effectué, le navigateur lance une recherche et renvoie ses résultats dans une seconde page  
	- Si vous effectuer une requete avec des fautes d'orthographes, vous aurez un résutat
	- 10 résultats peuvent être affiché au maximum. Si la recherche n'a pas de résultat, le message "Aucun résultat." s'affichera  

Remarque : Des affichages sont disponibles sur le terminal où est lancé le serveur afin d'avoir des informations sur les étapes en cours.
