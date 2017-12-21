import string
import numpy
import math
class MarkovChain:
        dic={}
        inv_map={}
        matrix=[[0]]
        def addCorpus(self, corpus):
                corpus=corpus.lower()
                last=corpus.split(" ")[0]
                self.dic[last]=0
                for word in corpus.split(" ")[1:]:
                        if (word in self.dic):
                                self.matrix[self.dic[last]][self.dic[word]]+=1
                        else:
                                self.dic[word]=len(self.dic)
                                self.matrix.append([0 for k in self.matrix])
                                for val in self.matrix:
                                        val.append(0)
                                self.matrix[self.dic[last]][self.dic[word]]+=1
                        last=word
                self.inv_map = {v: k for k, v in self.dic.iteritems()}
        def genWord(self, seed):
                tot = sum(self.matrix[self.dic[seed]])
                if tot>0:
                        p=[val/(1.0*sum(self.matrix[self.dic[seed]])) for val in self.matrix[self.dic[seed]]]
                else:
                        p=[1/len(self.matrix) for val in self.matrix]
                try:
                        return numpy.random.choice(numpy.arange(0, len(self.matrix)),p=p)
                except:
                        p[-1]+=abs(1-sum(p))
                        return numpy.random.choice(numpy.arange(0, len(self.matrix)),p=p)
        def genParagraph(self, seed,length):                       
                last=seed
                out=seed+" "
                for val in range(length):
                        last= self.inv_map[int(self.genWord(last))]
                        out+=last+" "
                return out


