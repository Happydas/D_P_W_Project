from random import shuffle
import random

fin = open("../Data/Currency_Country/Country_Currency_filtered.txt", 'r')
fout = open("../Data/Currency_Country/Currency_Train.txt", 'w+')
fout2 = open("../Data/Currency_Country/Currency_Test.txt", 'w+')
for line in fin:
    r = random.random()
    if r < 0.60:
        fout.write(line)
    else:
        fout2.write(line)
fin.close()
fout.close()
fout2.close()
