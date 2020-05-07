"""
@author: Julian CHAMBRIER

"""

#Importation des bibliothèques utiles
from os import listdir
from os.path import isfile, join
import time
import codecs
import re
import tf_idf
import unidecode
import string
from bs4 import BeautifulSoup
import motSimilaire

#Class de l'index inversé
class inverted_index:
    #Constructeur 
    def __init__(self, stop_words):
        self.index = dict()
        self.stop_words = stop_words

    #Fonction d'affichage
    def display(self):
        for word, files in self.index.items():
            print(word , files)
        print("\n", len(self.index.items()), "mot(s) indexe(s)")

    #Fonction de construction de l'index inversé
    def build(self, documents):
        for file_name, file_content in documents.items():
            self.add(file_name,file_content);
            print("Fichier", file_name ,"traité pour l'indexation")
        print("\nTri des fichiers (trie décroissant des scores des fichiers en fonction du mot indexe) en cours...")
        self.sort(documents)
        print("\nTri des fichiers terminé");

    #Fonction d'ajout du contenu d'un fichier spliter dans l'index inversé
    def add(self, file_name, file_content):
        content_clean = self.format_file_content(file_content,self.stop_words)
        for word in content_clean:
            files = self.index.setdefault(word,set())
            files.add(file_name)

    #Fonction de recherche
    def search(self, request):
        list_file_score = []
        #Prend les mots similaires qui sont déjà dans le dico par exemple : paris et pris sont proches
        request=motSimilaire.listeSimilaire(request1,self.index)
        # Pour chaque mots de la requete on cherche les fichiers où sont présent ces mots
        for word in request:
            #On traite les mots de la requete pour quelle colle au mieux à l'index
            word = unidecode.unidecode(word)
            word = word.lower()
            word = " ".join("".join(["" if ch in string.punctuation else ch for ch in word]).split()) 
            word = word.replace("’","")
            word = word.replace("–", "")
            #Si le mot est dans l'index
            if word in self.index:
                #On ajoute le couple (fichier, score) à la liste
                for couple in self.index[word]:
                    list_file_score.append(couple)
        # On cree une liste de tuples (couple fichier : 0) où 0 est le score qu'on additionnera ensuite
        list_file = [ (tupl[0],0) for tupl in list_file_score]
        # On creer un dictionnaire de {'fichier':'score'} en modiant transformant la liste en un set piur enlever les doublons
        dict_file = dict(list(set(list_file)))
        # On additionne le score pour un meme fichier
        for file,score in list_file_score:
            dict_file[file] += score
        # On trie le dictionnaire et on transforme en liste
        list_file_sorted =  sorted(dict_file.items(), key=lambda t: t[1], reverse = True)
        list_file_sorted_res = []
        #On cree une liste sans le score (on enleve le tuple file, score pour garder que le score), cette liste est trié en fonction de list_file_sorted
        for file,_ in list_file_sorted:
            title = self.get_URL_title(file)
            title = title.replace('<title>', '')
            title = title.replace('</title>', '')
            file = self.transform_link(file)
            if title == "":
                title = file
            list_file_sorted_res.append((file,title))
        #print(list_file_sorted[0:10])
        #print("\nRésultats pour la requete", request , ":", list_file_sorted_res[0:10])
        return list_file_sorted_res[0:10]

    #Fonction de tri
    def sort(self, documents_cleaner):
        list_files_content = []
        # On recupere tous les contenus de tous les fichiers
        for file,content in documents_cleaner.items():
            list_files_content.append(content)

        for word,files in self.index.items():
            dict_word = dict()
            for file in files:
                score_word_file = tf_idf.TF_IDF(tf_idf.TF_frequence_brute,word,documents_cleaner[file], list_files_content)
                dict_word[file] = score_word_file
            list_word =  sorted(dict_word.items(), key=lambda t: t[1], reverse = True)
            # L'index est devient word [('file_name' : score) , ...]
            # On a ainsi un index où les fichiers sont triés par ordre décroissant en fonction du mot et des autres fichiers 
            self.index[word] = list_word
            #print(self.index[word])

    #Fonction permettant de formater les documents 
    def format_file_content(self,file_content, stop_words):
        words = file_content.split()
        words = self.clean_words(words, stop_words)
        words = self.normalize_words(words)
        return words

    #Fonction permettant de ne pas indexer les stop words
    def clean_words(self,words, stop_words):
        cleaned_words = []
        for word in words:
            if word not in stop_words:
                cleaned_words.append(word)
        return cleaned_words

    #Fonction permettant de normaliser les mots. C'est à dire de les mettre en minuscule
    def normalize_words(self,words):
        normalized_words = []
        for word in words:
            lower_word = word.lower()
            normalized_words.append(lower_word)
        return normalized_words

    #Remplace les _ du lien par des /. Les _ on surement remplacés les / pour éviter les erreurs d'accès au fichier
    def transform_link(self,link):
        link = link.replace("_", "/")
        return link
    #On recupère le titre de la page s'il existe
    def get_URL_title(self, link):
        try:
            #Lecture du fichier
            f = codecs.open("./pages_web/"+link, "r",encoding="UTF-8")
            content = f.read()
            soup = BeautifulSoup(content,"html.parser")
            if soup.find("title"):
                title = soup.find("title")
                return str(title)
            else:                
                return str("")            
        except ValueError:
            #print("Erreur dans le fichier")
            return ""

