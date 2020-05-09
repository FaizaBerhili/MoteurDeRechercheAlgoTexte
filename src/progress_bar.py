"""
@author CHAMBRIER Julian

"""
import os
def print_progress_bar (it, taille, prefix = '', suffix = '', logo = '█', printEnd = "\r"):
    """
    Affiche une bar de progression
    @params:
        it  - Required  : interation de boucle (Int)
        taille - Required  : taille totale de l'itération (Int)
        prefix - Optional  : Ce que l'on veut écrire avant la barre de progression (Str)
        suffix - Optional  : Ce que l'on veut écrire après la barre de progression(Str)
        logo   - Optional  : Logo de progression (Str)
        printEnd - Optional  : Caractere de fin de progress bar (Str)
    """
    #Affichage du pourcentage sans chiffre après la virgule
    percent = ("{0:.0f}").format(100 * (it / float(taille)))
    #Calcule de la taille du texte pour rester sur une ligne du terminal
    tailletext = len(prefix) + len(suffix) + 12
    #La taille de la progress bar s'ajuste en fonction de la grandeur du terminal
    #Si on agrandi ou rétrécit le terminal la progress bar s'ajustera
    taillelogo = int((os.get_terminal_size().columns - tailletext) * it // taille)
    #Affichage progress bar
    progress_bar = logo * taillelogo + '-' * ((os.get_terminal_size().columns - tailletext) - taillelogo)
    print('\r%s |%s| %s%% %s' % (prefix, progress_bar, percent, suffix), end = printEnd)
    # On affiche une nouvelle ligne quand le chargement est terminé 
    if it == taille: 
        print()