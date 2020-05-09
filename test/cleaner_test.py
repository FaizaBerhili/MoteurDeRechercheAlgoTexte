"""
@author: Julian CHAMBRIER

"""

#Importation des bibliotheques utiles
import os
from os import listdir
from os.path import isfile, join
import codecs
import re
import string
import unidecode
from bs4 import BeautifulSoup
import html
import sys
import progress_bar_test
import cleaner_test

def loadURL(repertoire):
    """
    Fonction permettant d'extraire une liste de fichier d'un repertoire
    @params:
        repertoire  - Required : Repertoire depuis lequel on veut extraire les fichiers
    """
    URL = [f for f in listdir(repertoire) if isfile(join(repertoire, f))]
    return URL

def convert_url(urls):
    """
    Fonction permettant d'avoir les documents sous forme de dictionnaire {'file_name':'file_content'}
    Ici le file_content est normalisé et nettoyé
    On affiche en plus la progression des fichiers nettoyés
    @params:
        urls  - Required : Les urls des fichiers
    """
    res = dict()
    compteur = 1
    taille = len(urls)
    for url in urls:
        #On associer à l'url son contenu nettoyé
        res[url] = cleaner_link(url); 
        progress_bar_test.print_progress_bar(compteur, taille, prefix = 'Nettoyage des fichier : ' + str(compteur) +  '/' + str(taille), suffix = '')
        compteur = compteur + 1
    return res

def cleaner_link(link):
    """
    Fonction permettant de nettoyer le contenue d'une page
    On va enlever tous les contenus inutiles balises, style, ponctuations ...
    @params:
        link  - Required : Fichier qu'on veut nettoyer
    """
    try:
        #Lecture du fichier
        f = codecs.open("./pages_web_test/"+link, "r",encoding="UTF-8")
        content = f.read()

        #On supprime les balises styles et script avec leurs contenus
        content = re.sub(r'<script[^>]*>.(?s)*</script>', ' ', content)
        content = re.sub(r'<style[^>]*>.(?s)*</style>', ' ', content)   

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

        #On enlève les éléments de la forme &... qui code des caractères qui n'ont pas été décodé en ascii
        # S'il on été décodé en ASCII c'est que leur code ASCII est dans la table ASCII
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

#Main de test
if __name__ == '__main__':
    #On charge les documents
    documents = cleaner_test.loadURL("./pages_web_test")
    #On transforme les documents en un dictionnaire {'file_name':'file_content'}
    documents_cleaner = cleaner_test.convert_url(documents[0:3])
    print()
    print(documents_cleaner)
