"""
@author: Emiliano BOUSSAC

"""
import textdistance

def motSimilaire(motCle,Dico):
	liste = []
	for keys in Dico.keys():
		if textdistance.levenshtein(motCle,keys)<2 :
			liste.append(keys)
	return liste
