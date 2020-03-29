#Ammar ALSADIK

#coding:utf-8

#Importation des bibliotheques necessaires
import http.server
 
#Definition du port d'écoute
port = 8889

#Definition d'un adresse auquelle on se connecte
serverAddress = ("localhost", port)

#Demarrer le serveur
server = http.server.HTTPServer

#Mettre en place un gestionnaire pour la gestion des requetes http fonctionnant avec CGI
handler = http.server.CGIHTTPRequestHandler

#Indiquer ou chercher les scripts a executer, ici à la racine du repertoire
handler.cgi_directories = ["/"]

#On execute le serveur 
httpd = server(serverAddress,handler)

#Message de verification
print("Serveur actif sur le port :", port)

#On dessert le serveur pour qu'il toune en boucle, jusqu'a l'interruption manuelle 
httpd.serve_forever()
