#Emiliano BOUSSAC




import calculDistance as cd


str1 = 'un deux deux quatre'
str2 = 'un deux trois quatre'


print("distance Hamming entre : " +str1+ " et " +str2)
d= cd.hamming_distance(str1,str2)
print(d)




t = cd.levenshtein(str1,str2)

print("distance de Levenshtein entre: "+ str1 + " et " + str2 )
print(t)




print("similarite cosinus entre : \"" + str1 + "\" et \"" + str2+"\"")


print (cd.get_result(str1,str2) )




