"""
@author: Julian CHAMBRIER

"""

#Importation des bibliothèques utiles
import inverted_index_test as ii
import cleaner

#Main
if __name__ == '__main__':
    #On charge les documents
    documents = cleaner.loadURL("./pages_web_test")
    #On transforme les documents en un dictionnaire {'file_name':'file_content'}
    documents_cleaner = cleaner.convert_url(documents)
    #On crée un index inversé
    stop_words = []
    index_inverse = ii.inverted_index(stop_words)
    #On remplit l'index inversé avec les documents fournis
    index_inverse.build(documents_cleaner)
    #On affiche l'index inversé
    index_inverse.display()
 