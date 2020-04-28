"""
@author: Emiliano BOUSSAC

"""
import textdistance

def motSimilaire(motCle,Dico):
	liste = []
	if(len(motCle)>2):
		for keys in Dico.keys():
			if textdistance.levenshtein(motCle,keys)<2 :
				liste.append(keys)
	else:
		liste.append(motCle)
	return liste




# a mettre au debut de la fonction search de index inversé
# request : liste de string ["le","chat","noir"]

def listeSimilaire2(request,index):
	request2=[]
	for word in request:
		request2.append(motSimilaire(word,index))
	return request2

def listeSimilaire(request,Dico):
	liste = []
	for motCle in request:
		if(len(motCle)>2):
			for keys in Dico.keys():
				if textdistance.levenshtein(motCle,keys)<2 :
					liste.append(keys)
		else:
			liste.append(motCle)
	return liste

