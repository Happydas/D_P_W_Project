from random import shuffle
import random

fin = open("../Data/Capital_Country/Capital_filtered.txt", 'r')
fout = open("../Data/Capital_Country/Capital_Train.txt", 'w+')
fout2 = open("../Data/Capital_Country/Capital_Test.txt", 'w+')
for line in fin:
    r = random.random()
    if r < 0.50:
        fout.write(line)
    else:
        fout2.write(line + "\n")
fin.close()
fout.close()
fout2.close()
