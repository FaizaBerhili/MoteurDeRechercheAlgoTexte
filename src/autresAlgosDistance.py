# Emiliano BOUSSAC
#
#pip install textdistance
#bibliotheques contenant plusieurs algos de calcul de distance entre string
#https://pypi.org/project/textdistance/

import textdistance

#fonction identique pour tous les algos
#.distance(str1,str2)
#.similarity(str1,str2)
#.normalized_distance(str1,str2)
#.normalized_similarity(str1,str2)
#


texte1 = "un deux trois quatre"
texte2 = "un deux cinq quatre"


print("compare distance/similarite entre les sequences : ")
print(texte1)
print(texte2)


print()

print("DamerauLevenshtein")


print (textdistance.damerau_levenshtein.distance(texte1,texte2))
print( textdistance.damerau_levenshtein.similarity(texte1,texte2))

print()
print("JaroWinkler")


print( textdistance.jaro_winkler.distance(texte1,texte2))
print (textdistance.jaro_winkler.similarity(texte1,texte2))

print()

print("StrCmp95")


print( textdistance.strcmp95.distance(texte1,texte2))
print( textdistance.strcmp95.similarity(texte1,texte2))

print()

print("NeedlemanWunsch")


print( textdistance.needleman_wunsch.distance(texte1,texte2))
print( textdistance.needleman_wunsch.similarity(texte1,texte2))

print()

print("Gotoh")


print( textdistance.gotoh.distance(texte1,texte2))
print (textdistance.gotoh.similarity(texte1,texte2))

print()
print("SmithWaterman")


print( textdistance.smith_waterman.distance(texte1,texte2))
print (textdistance.smith_waterman.similarity(texte1,texte2))





