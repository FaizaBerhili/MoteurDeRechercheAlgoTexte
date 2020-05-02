#Bibilothèques nécessaires
from flask import Flask, render_template, request, jsonify
import inverted_index_test as ii
import cleaner_test
from bs4 import BeautifulSoup

# Initialize the Flask application
app = Flask(__name__, template_folder='.')
#On charge les documents
documents = cleaner_test.loadURL("./pages_web_test")
#On transforme les documents en un dictionnaire {'file_name':'file_content'}
documents_cleaner = cleaner_test.convert_url(documents)
#On crée un index inversé
stop_words = []
index_inverse = ii.inverted_index(stop_words)
#On remplit l'index inversé avec les documents fournis
index_inverse.build(documents_cleaner)

#Route principale : la page d'accueil
@app.route('/')
def index():
    return render_template('index_test.html')	
@app.route('/index')
def route_index():
    return render_template('index_test.html')	

#Route quand on fait une recherche, on envoie a la page de recherche la liste des fichiers en fonction de la requete ainsi que la requete pour l'afficher
@app.route('/search', methods=['GET'])
def search():
    return render_template("search_test.html", requete =request.args.get('recherche', default=""), file_list = index_inverse.search(request.args.get('recherche',default="").split()))

if __name__ == '__main__':
    app.run(
        host="localhost",
        port=int("8090")
        #,debug=True
    )
