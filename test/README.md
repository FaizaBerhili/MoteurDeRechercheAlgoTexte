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
- Lancer la commande : python serverWeb_test.py  
- Le server se lance avec le message : "Running on http://localhost:8090/" (si vous êtes en local)  
(Le lancement du serveur peut être long dû à la création de l'index inversé de millier de fichier)  
- Ouvrer votre navigateur et entrer http://localhost:8090 ou localhost:8090  
- Le navigateur JuAmEm se lance  
	- (Si vous avez le message "La connexion a échoué", regarder si votre serveur Web est bien lancé dans le terminal)  
- Vous pouvez effectuer des recherches sur le navigateur   
	- Si une recherche VIDE est effectué, le navigateur ne lance aucune recherche  
	- Si une recherche NON VIDE est effectué, le navigateur lance une recherche et renvoie ses résultats dans une seconde page  
	- 10 résultats peuvent être affiché au maximum. Si la recherche n'a pas de résultat, le message "Aucun résultat." s'affichera  
