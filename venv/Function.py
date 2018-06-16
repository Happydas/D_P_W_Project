
import warnings
warnings.filterwarnings(action="ignore", category=UserWarning, module='gensim')
import gensim, re
class Word2VecDBpedia():
    def saveWord(self, lines):
        f = open("filteredWords.txt", 'w')
        for line in lines:
            f.write(line + '\n')

    def loadFiles(self):

        model = gensim.models.KeyedVectors.load_word2vec_format(
            'D:/dl4j-files/GoogleNews-vectors-negative300.bin/GoogleNews-vectors-negative300.bin', binary=True)

        f = open("output1.txt", 'r')
        lines = f.read()
        linesNew = []
        for line in lines.split('\n'):
            line = re.sub(' +', ' ', line)
            for word in line.split(" "):
                if word not in model.vocab:
                    break
            linesNew.append(line)
        self.saveWord(linesNew)



w = Word2VecDBpedia()
w.loadFiles()
