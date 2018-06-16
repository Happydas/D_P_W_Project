fin = open("../Data/Country_Currency.txt")
fout = open("../Data/Country_Currency_Clean.txt", "w+")
delete_list = ['http://dbpedia.org/resource/']
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
print ('Completed')
