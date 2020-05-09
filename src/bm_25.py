"""
@author: Julian CHAMBRIER

"""

import tf_idf
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

