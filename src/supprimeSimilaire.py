#Emiliano BOUSSAC

import sys
import numpy as np
import re
import math
from collections import Counter
import cleaner
import textdistance
import shutil
import os
import progress_bar




def supressionPage(dico):
	fichiers = os.listdir('./pages_web/');
	taille = len(fichiers)
	compteur = 1
	for fichier in fichiers:
		try:
	    	#print(dico[fichier]); #KeyError
			#si dans le dico alors supprimé du dico les pages dans son set
			#set de nom fichier (string)
			setfichiers = dico[fichier] 
			#print("clé trouvé")
			for f in setfichiers:
				dico.pop(f); #supprime clé nom du fichier du dico
		except KeyError:
	    	#print("pas de clé trouvé donc suppression de la page")
			os.remove('./pages_web/' + fichier)
		progress_bar.print_progress_bar(compteur, taille, prefix = 'Vérifie si les fichiers sont dans le dico : ' + str(compteur) +  '/' + str(taille), suffix = '')
		compteur = compteur + 1



