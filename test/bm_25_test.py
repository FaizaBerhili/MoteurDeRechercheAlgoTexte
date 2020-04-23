"""
@author: Julian CHAMBRIER

"""

import tf_idf_test
import math
import numpy

#Fonction IDF utilisé dans le bm-25
def IDF_bm_25(term,  documents_contents):
    doc_contain_term = 0
    for document_content in documents_contents:
        document_split = document_content.split()
        if(document_split.count(term) > 0):
            doc_contain_term += 1
    return math.log10( (len(documents_contents) - doc_contain_term + 0.5)  / (doc_contain_term + 0.5) )
    
#Fonction calculant le bm-25 d'un mot
#En pratique k appartient [1.2,2], b = 0.75
def bm_25(TF_function, term , document_content, documents_contents,k,b):
    avg_length = numpy.mean([len(document) for document in documents_contents])
    TF_value = TF_function(term,document_content)
    return IDF_bm_25(term, documents_contents) * (( TF_value * (k + 1)) / (TF_value + k * (1 - b + b * (len(document_content) / avg_length) )))

if __name__ == '__main__':
    #Tests des TF/IDF/TF-IDF
    #Les tests sont les mêmes que ceux de Wikipédia

    document1 = "Son nom est célébré par le bocage qui frémit, et par le ruisseau qui murmure, les vents l emportent jusqu à l arc céleste, l arc de grâce et de consolation que sa main tendit dans les nuages."
    document2 = "À peine distinguait on deux buts à l extrémité de la carrière: des chênes ombrageaient l un, autour de l autre des palmiers se dessinaient dans l éclat du soir."
    document3 = "Ah! le beau temps de mes travaux poétiques! les beaux jours que j'ai passés près de toi ! Les premiers, inépuisables de joie, de paix et de liberté; les derniers, empreints d une mélancolie qui eut bien aussi ses charmes."
    print("BM-25 avec TF_frequency_brute : " + str(bm_25(tf_idf_test.TF_frequence_brute,'qui',document1,[document1,document2,document3],1.7,0.75)))