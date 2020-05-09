#Emiliano BOUSSAC

import numpy as np
import re
import math
from collections import Counter
import textdistance
import progress_bar_test


#prend en entrée le dico créer par le cleaner avec comme clé le lien de la page et comme valeur
# son contenu qui est formaliser
#crée un dico ou les clé sont les liens des pages
#et les valeurs sont un set des liens des pages avec lesquelles ils sont similaires

def dicoSimilaire(dicoDocuments):
	print("Creation du dico des pages similaires");
	dicoSim = dict()
	compteur = 1
	taille = len(dicoDocuments.items());
	print("Traitement pages similaires\n")
	for lien1,texte1 in dicoDocuments.items():
		for lien2,texte2 in dicoDocuments.items():
			if(lien1 != lien2):
				d = textdistance.hamming.similarity(texte1,texte2)
				s = dicoSim.setdefault(lien1,set())				
				if(d>300): # si leur similarité est supérieur à 300 on ajoute la page comme valeur dans le set
					s.add(lien2)
		progress_bar_test.print_progress_bar(compteur, taille, prefix = 'Vérifie si les fichiers sont dans le dico : ' + str(compteur) +  '/' + str(taille), suffix = '')
		compteur = compteur + 1
	return (dicoSim)
	





