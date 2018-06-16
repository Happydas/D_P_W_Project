from random import shuffle
import random

f = open("../Data/Person_Party/Person_Party_filtered.txt", 'r', encoding="utf-8")
train = open("../Data/Person_Party/Person_Party_Train.txt", 'w+' , encoding="utf-8")
test = open("../Data/Person_Party/Person_Party_Test.txt", 'w+' , encoding="utf-8")
for line in f:
    r = random.random()
    if r < 0.30:
        train.write(line)
    else:
        test.write(line)
f.close()
train.close()
test.close()
