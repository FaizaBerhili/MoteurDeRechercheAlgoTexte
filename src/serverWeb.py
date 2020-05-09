#Bibilothèques nécessaires
from flask import Flask, render_template, request, jsonify
import inverted_index as ii
import cleaner
from bs4 import BeautifulSoup
import time
from time import strftime
from time import gmtime

# Initialize the Flask application
app = Flask(__name__, template_folder='.')
# Debut du decompte du temps
start_time = time.time()
#On charge les documents
print("Nettoyage des fichiers en cours...\n")
documents = cleaner.loadURL("./pages_web")
#On transforme les documents en un dictionnaire {'file_name':'file_content'}
documents_cleaner = cleaner.convert_url(documents)
print("Nettoyage des fichiers terminé.\n")
#On crée un index inversé
stop_words = []
print("Création de l'index inversé en cours...\n")
index_inverse = ii.inverted_index(stop_words)
#On remplit l'index inversé avec les documents fournis
index_inverse.build(documents_cleaner)
print("Création de l'index inversé terminé.\n")
# Affichage du temps d execution
print("\nTemps d execution des fonctions avant le lancement du serveur : %s\n" % strftime('%Hh %Mm %Ss', gmtime((time.time() - start_time))))

#Route principale : la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index')
def route_index():
    return render_template('index.html')		

#Route quand on fait une recherche, on envoie a la page de recherche la liste des fichiers en fonction de la requete ainsi que la requete pour l'afficher
@app.route('/search', methods=['GET'])
def search():
    return render_template("search.html", requete =request.args.get('recherche', default=""), file_list = index_inverse.search(request.args.get('recherche',default="").split()))

if __name__ == '__main__':
    app.run(
        host="localhost",
        port=int("8090")
        #,debug=True
    )
