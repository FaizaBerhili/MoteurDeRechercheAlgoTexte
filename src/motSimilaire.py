"""
@author: Emiliano BOUSSAC

"""
import textdistance
import progress_bar

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
	taille = len(request)
	compteur = 1
	for motCle in request:
		#Progress bar
		progress_bar.print_progress_bar(compteur, taille, prefix = 'Mot de la recherche traité : ' + str(compteur) +  '/' + str(taille), suffix = '')
		compteur = compteur + 1
		if(len(motCle)>2):
			for keys in Dico.keys():
				if textdistance.levenshtein(motCle,keys)<2 :
					liste.append(keys)
		else:
			liste.append(motCle)
	return liste

