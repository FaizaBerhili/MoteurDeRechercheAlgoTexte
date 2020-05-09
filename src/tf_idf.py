"""
@author Julian CHAMBRIER

"""

#Importation des bibliothèques utiles
from os import listdir
from os.path import isfile, join
import time
import codecs
import re
import string
import unidecode
import math
import sys
import functools
import numpy

def TF_frequence_brute(term , document_content):
    """
    Fonction Term Frequency avec la fréquence brute (nombre d'occurence du term / taille du texte)

    @params:
        term - Required : Le terme dont on veut calculer le score (Str)
        document_content  - Required : Le document sur lequel on calcul le score (Str)
    """
    document_split = document_content.split()
    try: 
        return document_split.count(term)/len(document_split)
    except:
        #Division par 0
        return 0

def TF_binaire(term , document_content):
    """
    Fonction Term Frequency binaire(nombre d'occurence dans le texte)

    @params:
        term - Required : Le terme dont on veut calculer le score (Str)
        document_content  - Required : Le document sur lequel on calcul le score (Str)
    """
    return document_content.split().count(term)

def TF_normalisation_log(term , document_content):
    """
    Fonction Term Frequecy avec la normalisation logarithmique (1 + log((nombre d'occurence du term / taille du texte)))

    @params:
        term - Required : Le terme dont on veut calculer le score (Str)
        document_content  - Required : Le document sur lequel on calcul le score (Str)
    """
    return 1 + math.log10(TF_frequence_brute(term,document_content))

def TF_normalisation_0_5_max(term,document_content):
    """
    Fonction Term Frequency avec normalisation 0.5 par le max

    @params:
        term - Required : Le terme dont on veut calculer le score (Str)
        document_content  - Required : Le document sur lequel on calcul le score (Str)
    """
    document_split = document_content.split()
    frequency_list = [TF_frequence_brute(word,document_content) for word in document_split]
    try:
        return 0.5 + 0.5 * ( TF_frequence_brute(term,document_content) / max(frequency_list))
    except:
        #division par 0
        return 0.5

def IDF(term , documents_contents):
    """
    Fonction Inverse Document Frequency 

    @params:
        term - Required : Le terme dont on veut calculer le score (Str)
        documents_contents  - Required : Les documents sur lesquels on veut calculer le score (List of Str)
    """
    doc_contain_term = 0
    for document_content in documents_contents:
        document_split = document_content.split()
        if(document_split.count(term) > 0):
            doc_contain_term += 1
    try: 
        return math.log10( len(documents_contents) / doc_contain_term )
    except:
        #Division par 0
        return 0
"""
#Autre manière de calculer l'IDF
def IDF_2(term , documents_contents):
    doc_contain_term = 0
    for document_content in documents_contents:
        document_split = document_content.split()
        if(document_split.count(term) > 0):
            doc_contain_term += 1
    freq = doc_contain_term / len(documents_contents)
    try:
        return math.log10( 1 / freq )
    except:
        #Division par 0
        return sys.maxsize
"""

def TF_IDF(TF_function,term, document_content, documents_contents):
    """
    Fonction calculant le TF_IDF
    Pour des raisons de praticité et vu le nombre de fonctions TF différentes, il est plus simple que TF_IDF prenne en argument une fonction TF.
    Ainsi l'utilisateur va pouvoir choisir la fonction qu'il souhaite utiliser 

    @params:
        TF_function - Required : La fonction de calcul de TF à utiliser (fonction)
        term - Required : Le terme dont on veut calculer le score (Str)
        document_content  - Required : Le document sur lesquels on veut calculer le score d'où est extrait le term (List of Str)
        documents_contents  - Required : Les documents sur lesquels on veut calculer le score (List of Str)
    """
    return TF_function(term, document_content) * IDF(term,documents_contents)
