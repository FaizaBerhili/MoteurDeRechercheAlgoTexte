"""
@author: Julian CHAMBRIER

"""

#Importation des bibliothèques utiles
from os import listdir
from os.path import isfile, join
import time
import codecs
import re
import tf_idf_test
import unidecode
import string
from bs4 import BeautifulSoup
import motSimilaire
import progress_bar_test
import cleaner_test
from time import strftime
from time import gmtime

#Class de l'index inversé
class inverted_index:

    def __init__(self, stop_words = []):
        """
        Constructeur de l'index inversé
        @params:
            stop_words  - Optionnal : Mot qu'on ne souhaite pas indexé car jugé trop peu utile (List of Str)
            Les stop words sont la pour ne pas indexer des mots sans importance dans une recherche car souvent trop nombreux dans les fichiers et 
            de ce fait peuvent faire varier les scores (par exemple : le/la/les/un ...)
        """
        self.index = dict()
        self.stop_words = stop_words

    def display(self):
        """
        Affiche un index inversé
        
        """
        for word, files in self.index.items():
            print(word , files)
        print("\n", len(self.index.items()), "mot(s) indexe(s)")

    def build(self, documents):
        """
        Construction de l'index inversé
        Cette fonction va permettre d'ajouter dans l'index inversé le mot et son fichier.
        @params:
            documents - Required  : Les documents sur lesquels ont veux contruire l'index inversé (Dict)
        """
        compteur = 1
        taille = len(documents)
        for file_name, file_content in documents.items():
            self.add(file_name,file_content);
            progress_bar_test.print_progress_bar(compteur, taille, prefix = 'Indexation des fichiers : ' + str(compteur) +  '/' + str(taille), suffix = '')
            compteur = compteur + 1
        print("\nTri des fichiers (trie décroissant des scores des fichiers en fonction du mot indexe) en cours...")
        self.sort(documents)
       	print("\nTri des fichiers terminé");

    def add(self, file_name, file_content):
        """
        Ajouter des mots et des fichiers dans l'index inversé
        Pour chaque mot du contenu du fichier, on va l'ajouté à l'index inversé avec sson fichier associé
        Si le mot est déjà dans l'index, on va simplement ajouté à l'ensemble de fichier du mot le nouveau fichier
        @params:
            file_name - Required  : Le nom du fichier sur lequel on travaille (Str)
            documents - Required  : Le contenu du fichier sur lequel on travaille (Str)

        """
        # On formalise le contenu du fichier afin de le normalisé et d'enlevé les stop words le cas échéant
        content_clean = self.format_file_content(file_content,self.stop_words)
        for word in content_clean:
            #Si le mot est n'est pas présent dans le dictionnaire, on associe un ensemble vide
            #Sinon on retourne l'ensemble de fichiers correspondant au mot
            files = self.index.setdefault(word,set())
            #On ajoute le fichier à cet ensemble
            files.add(file_name)

    def search(self, request1):
        """
        Recherche une requete dans l'index inversé
        La requete est entrée directement via le navigateur par son utilisateur
        Cette méthode va permettre de renvoyer l'url du fichier et le titre du fichier (s'il existe) 
        sous la forme d'une liste afin de pouvoir proposer un meilleur affichage et une redirection  à l'utilisateur de notre navigateur
        @params:
            request1 - Required  : La requete du l'utilisateur du navigateur (List of Str)
        @return:
            Les 10 fichiers qui maximise les scores pour la requête sous la forme d'une liste de tuple (url du fichier, titre du fichier)
        @rtype:
            List of tuples (file_url,file_title)

        """
        list_file_score = []
        request_normalise = []
        start_time = time.time()
        #On traite les mots de la requete pour enlever la ponctuation, la casse et les accents
        for word in request1:
            #On traite les mots de la requete pour se formaliser au format des mots de notre index
            #Pas de majuscule, pas d'accent...
            word = unidecode.unidecode(word)
            word = word.lower()
            word = " ".join("".join(["" if ch in string.punctuation else ch for ch in word]).split()) 
            word = word.replace("’","")
            word = word.replace("–", "")
            request_normalise.append(word)
        #On ajoute à la liste de requete les mots qui sont proche et dans le dico ex : algorithmic et algorithmie
        request=motSimilaire.listeSimilaire(request_normalise,self.index)
        # Pour chaque mots de la requete on cherche les fichiers où sont présent ces mots
        for word in request:
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
        #On recupère le titre de la page grâce à la balise title s'il existe
        for file,_ in list_file_sorted[0:10]:
            title = self.get_URL_title(file)
            title = title.replace('<title>', '')
            title = title.replace('</title>', '')
            file = self.transform_link(file)
            if title == "":
                title = file
            list_file_sorted_res.append((file,title))
        #print(list_file_sorted[0:10])
        print("\nRésultats pour la requete", request , ":", list_file_sorted_res[0:10])
        print("\nTemps de la recherche : %s\n" % strftime('%Hh %Mm %Ss', gmtime((time.time() - start_time))))
        return list_file_sorted_res[0:10]

    def sort(self, documents_cleaner):
        """
        Tri des l'ensemble de chaque mot de l'index par rapport à un score
        Chaque ensemble deviendra une liste triée en fonction des scores
        @params:
            documents_cleaner - Required  : Les documents à trier (Dict)
        """
        list_files_content = []
        compteur = 1
        taille = len(documents_cleaner.items())
        # On recupere tous les contenus de tous les fichiers
        for file,content in documents_cleaner.items():
            list_files_content.append(content)
            #Progress bar         
            progress_bar_test.print_progress_bar(compteur, taille, prefix = 'Récupération des fichiers : ' + str(compteur) +  '/' + str(taille), suffix = '')
            compteur = compteur + 1
        compteur = 1
        taille = len(self.index.items())
        #Pour chaque mot de chaque fichier on calcule le score associé
        for word,files in self.index.items():
            dict_word = dict()
            for file in files:
                score_word_file = tf_idf_test.TF_frequence_brute(word,documents_cleaner[file])
                #score_word_file = tf_idf_test.TF_IDF(tf_idf_test.TF_frequence_brute,word,documents_cleaner[file], list_files_content)
                dict_word[file] = score_word_file
            #On tri par rapport au score
            list_word =  sorted(dict_word.items(), key=lambda t: t[1], reverse = True)
            # L'index est devient word [('file_name' : score) , ...]
            # On a ainsi un index où les fichiers sont triés par ordre décroissant en fonction du mot et des autres fichiers 
            self.index[word] = list_word
            #Progress bar
            progress_bar_test.print_progress_bar(compteur, taille, prefix = 'Tri des fichiers (par score de mot) : ' + str(compteur) +  '/' + str(taille), suffix = '')
            compteur = compteur + 1
            #print(self.index[word])
     
    def format_file_content(self,file_content, stop_words):
        """
        Formate le contenu du document 
        @params:
            file_content - Required  : Le contenu du fichier à formater (Str)
            stop_words - Required  : Les mots qu'on ne veut pas indexer (list of Str)
        @return: 
            Les mots normalisés
        @rtype:
            List of Str

        """
        #On partitionne le fichier
        words = file_content.split()
        words = self.clean_words(words, stop_words)
        #words = self.normalize_words(words)
        return words

    def clean_words(self,words, stop_words):
        """
        Fonction permettant de ne pas indexer les stop words 

        @params:
            words - Required  : Les mots extraits du contenu d'un fichier (list Str)
            stop_words - Required  : Les mots qu'on ne veut pas indexer (list of Str)
        @return:
            Les mots où les stop words ont été retirés
        @rtype:
            List of Str

        """
        cleaned_words = []
        #Pour chaque mot s'il n'appartient pas au stop words, on le garde
        for word in words:
            if word not in stop_words:
                cleaned_words.append(word)
        return cleaned_words

    def normalize_words(self,words):
        """
        Fonction permettant de coller avec la normalisation qu'on s'est donné
        (Cette fonction n'est plus utilisé car les mots sont mis directement en minuscule dans lors du nettoyage )

        @params:
            words - Required  : Les mots à normaliser (list Str)
        @return:
            Les mots en minuscule
        @rtype:
            list of Str
        """
        normalized_words = []
        for word in words:
            lower_word = word.lower()
            normalized_words.append(lower_word)
        return normalized_words

    def transform_link(self,link):
        """
        Fonction permettant de transformer le lien
        Remplace les _ du lien par des /. Les _ on surement remplacés les / pour éviter les erreurs d'accès au fichier

        @params:
            link - Required  : Le lien a transformé (Str)
        @return:
            Le lien transformé
        @rtype:
            Str
        """
        link = link.replace("_", "/")
        return link

    def get_URL_title(self, link):
        """
        Fonction permettant de récupérer le lien d'une page
        Le titre de la page se trouve dans une balise title

        @params:
            link - Required  : Le lien de la page (Str)
        @return:
            Le titre de la page
        @rtype:
            Str
        @raise:
            ValueError: Déclenche une exception s'il y a une erreur d'ouverture du fichier
        """
        try:
            #Lecture du fichier
            f = codecs.open("./pages_web_test/"+link, "r",encoding="UTF-8")
            content = f.read()
            #On parse notre fichier pour le coller au html
            soup = BeautifulSoup(content,"html.parser")
            #Si il y a une balise title
            if soup.find("title"):
                title = soup.find("title")
                #On renvoie le contenu
                return str(title)
            else:                
                return str("")            
        except ValueError:
            #print("Erreur dans le fichier")
            return ""

#Main de test
if __name__ == '__main__':
    #On charge les documents
    documents = cleaner_test.loadURL("./pages_web_test")
    #On transforme les documents en un dictionnaire {'file_name':'file_content'}
    #On nettoie aussi les fichiers
    documents_cleaner = cleaner_test.convert_url(documents[0:3])
    #On crée un index inversé
    stop_words = []
    index_inverse = inverted_index(stop_words)

    #On remplit l'index inversé avec les documents fournis
    #Cette etape fait le trie des fichiers par rapport au score du mot indexe pour ces fichiers
    index_inverse.build(documents_cleaner)

    #On affiche l'index inversé
    index_inverse.display()

    #On effectue une recherche
    #Les mots de la requete qui sont dans aucun fichier son simplement ignoré
    #Les mots proches sont ajoutés à la requete
    index_inverse.search(["Algorithmie","Julien","David."])





