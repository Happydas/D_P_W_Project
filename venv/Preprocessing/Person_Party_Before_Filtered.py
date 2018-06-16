def before():
    newFile = open('../Data/Person_Party/Person_Party_Before_Filtered.txt', 'r+', encoding="utf-8")
    return newFile
newFile = before()
Directions = False
with open('../Data/Person_Party/Person_Party_Clean.txt', encoding="utf-8") as f:
    for c in f.read():
        if Directions is False and c == '(':
            Directions = True
        elif Directions is True and c == ')':
            Directions = False
            continue

        if not Directions:
            newFile.write(c)

        if Directions:
            pass

f = open('../Data/Person_Party/Person_Party_Before_filtered_2.txt', 'w', encoding="utf-8")
fin = before()
for line in fin:
    sen = line.strip()
    if sen[-1:] == '_':
        sen = sen[:-1]
        line = line.replace(line, "")
        f.write(sen + "\n")
    else:
        f.write(sen + "\n")


