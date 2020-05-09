#Emiliano BOUSSAC

import sys
import numpy as np
import re
import math
from collections import Counter
import cleaner_test
import textdistance
import shutil
import os
import progress_bar_test




def supressionPage(dico):
    fichiers = os.listdir('./pages_web_test/')
    taille = len(fichiers)
    compteur = 1
    for fichier in fichiers:
	    try:
	        #print(dico[fichier]); #KeyError
		    #si dans le dico alors supprimé du dico les pages dans son set
		    setfichiers = dico[fichier] #set de nom fichier (string)
		    #print("clé trouvé")
		    for f in setfichiers:
		        dico.pop(f) #supprime clé nom du fichier du dico
	    except KeyError:
	     	#print("pas de clé trouvé donc suppression de la page")
	     	os.remove('./pages_web_test/' + fichier)
	    progress_bar_test.print_progress_bar(compteur, taille, prefix = 'Vérifie si les fichiers sont dans le dico : ' + str(compteur) +  '/' + str(taille), suffix = '')
	    compteur = compteur + 1



