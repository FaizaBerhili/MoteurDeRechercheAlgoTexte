"""
@author: Julian CHAMBRIER

"""

#Importation des bibliothèques utiles
from os import listdir
from os.path import isfile, join
import codecs
import re
import string
import unidecode


# Fonction permettant d'extraire dans une Liste les fichiers d'un repertoire
def loadURL(repertoire):
    URL = [f for f in listdir(repertoire) if isfile(join(repertoire, f))]
    return URL

# Fonction permettant d'avoir les documents sous forme de dictionnaire {'file_name':'file_content'}
# Ici le file_content est normalisé et nettoyé
def convert_url(urls):
    res = dict()
    for url in urls:
        res[url] = cleaner_link(url)
    return res

# Fonction permettant de nettoyer le contenue d'une page
def cleaner_link(link):
    try:
        #Lecture du fichier
        f = codecs.open("./pages_web_test/"+link, "r",encoding="UTF-8")
        content = f.read()
        #On supprime les balises script et style ainsi que leurs contenus
        content =  re.sub('<script[^<]+?>[^<]+?</script>', ' ',content)
        content =  re.sub('<style[^<]+?>[^<]+?</style>', ' ',content)
        #On supprimes les balises
        content = re.sub('<[^<]+?>', ' ', content)
        #On supprime les espaces inutiles
        content = " ".join(content.split())
        #On remplace l'apostrophe et le trait d'union par un espace
        content = re.sub('\'', ' ', content)
        content = re.sub('-', ' ', content)
        #On supprime la ponctuation        
        translator = str.maketrans('', '', string.punctuation)
        content = content.translate(translator)
        #On enlève les accents
        content = unidecode.unidecode(content)
        #On ferme le fichier
        f.close() 
        return content
    except ValueError:
        #print("Erreur dans le fichier")
        return ""
