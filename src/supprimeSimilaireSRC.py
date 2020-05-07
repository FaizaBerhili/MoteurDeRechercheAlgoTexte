#Emiliano BOUSSAC

import sys
import numpy as np
import re
import math
from collections import Counter
import cleaner
import textdistance
import shutil
import os
import supprimeSimilaire as supSim
from pageSimilaireSRC import dico


fichiers = os.listdir('./pages_web/');
print("nombre fichiers avant suppresssion");
print(len(fichiers));



supSim.supressionPage(dico);

fichiers = os.listdir('./pages_web/');
print("nombre fichiers apres suppresssion");
print(len(fichiers));


