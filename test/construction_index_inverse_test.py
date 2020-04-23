"""
@author: Julian CHAMBRIER

"""
# Cette page est une page de test, le serveur Web se chargera de créer et de remplir l'index
#Importation des bibliothèques utiles
import inverted_index_test as ii
import cleaner_test
import textdistance
# Les fonctions suivantes seront à intégrer dans le server Web 
# En effet, le server Web crée l'index et le construit
# La recherche sera récupérer dirrectement à partir des entrées de l'utilisateur

# Les fonctions suivantes seront à intégrer dans le server Web 
# En effet, le server Web crée l'index et le construit
# La recherche sera récupérer dirrectement à partir des entrées de l'utilisateur

#Main
if __name__ == '__main__':
    #On charge les documents
    documents = cleaner_test.loadURL("./pages_web_test")
    #On transforme les documents en un dictionnaire {'file_name':'file_content'}
    documents_cleaner = cleaner_test.convert_url(documents)
    #On crée un index inversé
    stop_words = []
    index_inverse = ii.inverted_index(stop_words)
    #On remplit l'index inversé avec les documents fournis
    index_inverse.build(documents_cleaner)
    #On affiche l'index inversé
    index_inverse.display()
    #Effectuer une recherche
    #print(index_inverse.search(["Université","Paris","13"]))
    print()

    print(type(index_inverse.index))

    print("fonction search")
    print()
    resultats = index_inverse.search(["Université","Paris","13"])
    print(resultats)
    print(len(resultats))



    motCle = "methode"   
    motsSimilaire = []
    for keys in index_inverse.index.keys(): 	
    	if textdistance.levenshtein(motCle,keys)<2 :
    		motsSimilaire.append(keys)

    print()
    print("mot similaire a " + motCle)
    print(motsSimilaire)



 
