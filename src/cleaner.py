"""
@author: Julian CHAMBRIER

"""

#Importation des bibliotheques utiles
from os import listdir
from os.path import isfile, join
import codecs
import re
import string
import unidecode
from bs4 import BeautifulSoup
import html

# Fonction permettant d'extraire dans une Liste les fichiers d'un repertoire
def loadURL(repertoire):
    URL = [f for f in listdir(repertoire) if isfile(join(repertoire, f))]
    return URL

# Fonction permettant d'avoir les documents sous forme de dictionnaire {'file_name':'file_content'}
# Ici le file_content est normalise et nettoye
def convert_url(urls):
    res = dict()
    for url in urls:
        res[url] = cleaner_link(url)
    return res

# Fonction permettant de nettoyer le contenue d'une page
def cleaner_link(link):
    print("Netoyage de",link)
    try:
        #Lecture du fichier
        f = codecs.open("./pages_web/"+link, "r",encoding="UTF-8")
        content = f.read()

        #On supprime les balises script et style ainsi que leurs contenus
        soup = BeautifulSoup(content,"html.parser")
        for p in soup.find_all("script"):
            p.replace_with(" ")
        content = str(soup)

        soup = BeautifulSoup(content,"html.parser")
        for p in soup.find_all("style"):
            p.replace_with(" ")
        content = str(soup)

        #On supprimes les balises et leurs attributs (différenciation selon inline/block)
        content = re.sub(r'<[/]?span[^>]*>', '', content)
        content = re.sub(r'<[/]?em[^>]*>', '', content)
        content = re.sub(r'<[/]?strong[^>]*>', '', content)
        content = re.sub(r'<[/]?mark[^>]*>', '', content)
        content = re.sub(r'<[/]?a[^>]*>', '', content)
        content = re.sub(r'<[/]?cite[^>]*>', '', content)
        content = re.sub(r'<[/]?abbr[^>]*>', '', content)
        content = re.sub(r'<[/]?acronym[^>]*>', '', content)
        content = re.sub(r'<[/]?small[^>]*>', '', content)
        content = re.sub(r'<[^>]*>', ' ', content)

        #On enleve les accents et enleve les encodages 
        content = unidecode.unidecode(content)

        #On enleve les éléments de la forme &... qui code des caractères qui n'ont pas été décodé en ascii
        content = re.sub(r"&[^;]*;",' ', content)

        #On remplace des signes de ponctuation par un espace et on met le texte en un paragraphe
        content = " ".join("".join([" " if ch in string.punctuation else ch for ch in content]).split()) 
        content = content.replace("’"," ")
        content = content.replace("–", " ")

        #Mettre le texte en minuscule
        content = content.lower()

        #print(content)

        #On ferme le fichier
        f.close() 
        return content
    except ValueError:
        #print("Erreur dans le fichier")
        return ""
