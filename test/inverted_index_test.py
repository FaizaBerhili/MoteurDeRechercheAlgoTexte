"""
@author: Julian CHAMBRIER

"""

#Importation des bibliothèques utiles
from os import listdir
from os.path import isfile, join
import time
import codecs
import re

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
            self.add(file_name,file_content)

    #Fonction d'ajout du contenu d'un fichier spliter dans l'index inversé
    def add(self, file_name, file_content):
        for word in self.format_file_content(file_content,self.stop_words):
            files = self.index.setdefault(word,set())
            files.add(file_name)

    #Fonction de recherche
    def search(self, request):
        #A compléter pour la prochaine tache
        return None

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

