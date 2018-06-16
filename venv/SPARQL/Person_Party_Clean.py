import io
#Clean data
fin = open("../Data/Person_Party/Person_Party.txt", encoding="utf-8")
fout = open("../Data/Person_Party/Person_Party_Clean.txt", "w+", encoding="utf-8")
delete_list = ['http://dbpedia.org/resource/']
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
print ('Processing Finished')