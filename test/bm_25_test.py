"""
@author: Julian CHAMBRIER

"""

import tf_idf_test
import math
import numpy

def IDF_bm_25(term,  documents_contents):
    """
    Fonction IDF utilisé dans le bm-25

    @params:
        term - Required : Le terme dont on veut calculer le score (Str)
        documents_contents  - Required : Les documents sur lesquels on calcul le score (list of Str)
    """
    doc_contain_term = 0
    for document_content in documents_contents:
        document_split = document_content.split()
        if(document_split.count(term) > 0):
            doc_contain_term += 1
    return math.log10( (len(documents_contents) - doc_contain_term + 0.5)  / (doc_contain_term + 0.5) )
    
def bm_25(TF_function, term , document_content, documents_contents,k,b):
    """
    Fonction calculant le bm-25 d'un mot
    En pratique k appartient [1.2,2], b = 0.75

    @params:
        TF_function - Required : La fonction de calcul de TF à utiliser (fonction)
        term - Required : Le terme dont on veut calculer le score (Str)
        document_content  - Required : Le document sur lesquels on calcul le score par rapprt au term d'où est extrait le term (Str)
        documents_contents  - Required : Les documents sur lesquels on calcul le score (list of Str)
        k - Required : (Float)
        b - Required : (Float)
    """
    avg_length = numpy.mean([len(document) for document in documents_contents])
    TF_value = TF_function(term,document_content)
    return IDF_bm_25(term, documents_contents) * (( TF_value * (k + 1)) / (TF_value + k * (1 - b + b * (len(document_content) / avg_length) )))

#Main de test
if __name__ == '__main__':
    #Test du calcul du bm-25
    document1 = "Son nom est célébré par le bocage qui frémit, et par le ruisseau qui murmure, les vents l emportent jusqu à l arc céleste, l arc de grâce et de consolation que sa main tendit dans les nuages."
    document2 = "À peine distinguait on deux buts à l extrémité de la carrière: des chênes ombrageaient l un, autour de l autre des palmiers se dessinaient dans l éclat du soir."
    document3 = "Ah! le beau temps de mes travaux poétiques! les beaux jours que j'ai passés près de toi ! Les premiers, inépuisables de joie, de paix et de liberté; les derniers, empreints d une mélancolie qui eut bien aussi ses charmes."
    print("BM-25 avec TF_frequency_brute : " + str(bm_25(tf_idf_test.TF_frequence_brute,'qui',document1,[document1,document2,document3],1.7,0.75)))
