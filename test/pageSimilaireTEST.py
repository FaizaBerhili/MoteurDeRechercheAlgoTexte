#Emiliano BOUSSAC

import numpy as np
import re
import math
from collections import Counter
import cleaner_test
import pageSimilaire as pS

documents = cleaner_test.loadURL("./pages_web_test")
documents_cleaner = cleaner_test.convert_url(documents)

dico = pS.dicoSimilaire(documents_cleaner)


for lien1,liens2 in dico.items():	
	print("la page \"" + lien1 + "\"")
	print("est similaire aux pages : ")
	print(liens2)
	print()






