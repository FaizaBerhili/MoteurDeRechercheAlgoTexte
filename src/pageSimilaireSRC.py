#Emiliano BOUSSAC

import sys
import numpy as np
import re
import math
from collections import Counter
import cleaner
import pageSimilaire as pS

documents = cleaner.loadURL("./pages_web");
documents_cleaner = cleaner.convert_url(documents);

dico = pS.dicoSimilaire(documents_cleaner);

#print(dico)

#for lien1,liens2 in dico.items():	
	#print("la page \"" , lien1 , "\"");
	#print("est similaire aux pages : ");
	#print(liens2);
	#print();
	#sys.stdout.flush()






