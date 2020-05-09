#Emiliano BOUSSAC

import sys
import numpy as np
import re
import math
from collections import Counter
import cleaner_test
import textdistance
import shutil
import os
import supprimeSimilaire as supSim
from pageSimilaireTEST import dico


fichiers = os.listdir('./pages_web_test/');
print("Nombre fichiers avant suppresssion : ");
print(len(fichiers));

supSim.supressionPage(dico);

fichiers = os.listdir('./pages_web_test/');
print("Nombre fichiers apres suppresssion : ");
print(len(fichiers));


