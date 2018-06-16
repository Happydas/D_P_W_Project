from random import shuffle
import random

fin = open("../Data/Company_Headquarter/Company_headquarter_filtered.txt", 'r')
fout = open("../Data/Company_Headquarter/Company_headquarter_Train.txt", 'w+')
fout2 = open("../Data/Company_Headquarter/Company_headquarter_Test.txt", 'w+')
for line in fin:
    r = random.random()
    if r < 0.40:
        fout.write(line)
    else:
        fout2.write(line)
fin.close()
fout.close()
fout2.close()
