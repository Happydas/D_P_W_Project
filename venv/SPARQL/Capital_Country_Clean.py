

fin = open("../Data/Capital_Country/Capital.txt")
fout = open("../Data/Capital_Country/Capital1.txt", "w+")
delete_list = ['http://dbpedia.org/resource/']
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
print ('Completed')





f = open( "../Data/Capital_Country/Capital1.txt", "r" )
text = f.read()
f.close()
newText = ""
for each in text:
    if each == "-":
        each = "_" #Or replace it with whatever you like.
    newText += each
f = open( "../Data/Capital_Country/Capital_Clean.txt", "w" )
f.write( newText )
f.close()
