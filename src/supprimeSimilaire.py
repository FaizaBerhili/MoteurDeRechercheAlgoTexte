#Emiliano BOUSSAC

import numpy as np
import re
import math
from collections import Counter
import cleaner_test
import textdistance
import shutil
import os




def supressionPage(dico):
	fichiers = os.listdir('./pages_web_test/')
	#print("nombre de fichiers dans le répertoire : ")
	#print(len(fichiers))
	for fichier in fichiers:
		#print("verifier si dans dico")
		try:
			#print(dico[fichier]) #KeyError
			#si dans le dico alors supprimé du dico les pages dans son set
			setfichiers = dico[fichier] #set de nom fichier (string)
			for f in setfichiers:
				dico.pop(f) #supprime clé nom du fichier du dico
		except KeyError:
			#print("pas de clé trouvé donc suppression de la page")
			os.remove('./pages_web_test/' + fichier)



