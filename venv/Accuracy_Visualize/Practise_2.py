def before():
    newFile = open('../Data/Person_Party/Person_Before_Filtered1.txt', 'r+', encoding="utf-8")
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
    return newFile

f = open('../Data/Person_Party/Person_Before_filtered_2.txt', 'w', encoding="utf-8")
newFile = before()
for line in newFile:
    sen = line.strip()
    if sen[-1:] == '_':
        sen = sen[:-1]
        line = line.replace(line, "")
        # print(sen)
        f.write(sen + "\n")
    else:
        f.write(sen + "\n")




