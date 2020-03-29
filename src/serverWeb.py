#Ammar ALSADIK

#coding:utf-8

#Importation des binliothèques nécessaires
import http.server
 
#Définition du port d'écoute
port = 8889

#Définition d'un adresse auquelle on se connecte
serverAddress = ("localhost", port)

#Démarrer le serveur
server = http.server.HTTPServer

#Mettre en place un gestionnaire pour la gestion des requêtes http fonctionnant avec CGI
handler = http.server.CGIHTTPRequestHandler

#Indiquer où chercher les scripts à éxécuter, ici à la racine du repertoire
handler.cgi_directories = ["/"]

#On exécute le serveur 
httpd = server(serverAddress,handler)

#Message de vérification
print("Serveur actif sur le port :", port)

#On dessert le serveur pour qu'il toune en boucle, juqu'à l'interruption manuelle 
httpd.serve_forever()