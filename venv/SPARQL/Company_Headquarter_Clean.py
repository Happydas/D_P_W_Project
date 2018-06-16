fin = open("../Data/Company_Headquarter/Company_headquarter.txt", "r", encoding="utf-8")
fout = open("../Data/Company_Headquarter/Company_headquarter_Clean.txt", "w+", encoding="utf-8")
delete_list = ['http://dbpedia.org/resource/']
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
print ('Completed')
