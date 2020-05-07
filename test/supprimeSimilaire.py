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




def supressionPage(dico):
	fichiers = os.listdir('./pages_web_test/');
	n = len(fichiers);
	compteur = 0 ;
	for fichier in fichiers:
		compteur = compteur + 1;
		print(str(compteur) , " / " , str(n));
		print("verifie si fichier" , fichier ," est dans dico");
		sys.stdout.flush()
		try:
			#print(dico[fichier]) #KeyError
			#si dans le dico alors supprimé du dico les pages dans son set
			setfichiers = dico[fichier]; #set de nom fichier (string)
			#print("clé trouvé")
			for f in setfichiers:
				dico.pop(f); #supprime clé nom du fichier du dico
		except KeyError:
			#print("pas de clé trouvé donc suppression de la page")
			os.remove('./pages_web_test/' + fichier);



