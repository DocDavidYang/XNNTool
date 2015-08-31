from random import uniform

from Xnn.synapse import Synapse

class DirectSynapse(object):

    def __init__(self, synapse_id = None, src = None, des = None, state_num = 2):
        Synapse.__init__(self)
        self.__id = synapse_id
        self.__src = src
        self.__des = des
        self.__num = state_num
        for i in range(self.__num):
            self.__weight.append(0)

    def getSrc(self):
        return self.__src

    def setSrc(self, src):
        self.__src = src

    def getDes(self):
        return self.__des

    def setDes(self, des):
        self.__des = des

    def link(self, src = None, des = None):
        self.setSrc(src)
        self.setDes(des)

    def synapseId(self):
        return self.__id

    def getWeight(self):
        return self.__weight

    def setWeight(self, weight):
        for i in range(self.__num - 1):
            self.__weight[i] = self.__weight[i+1]
        self.__weight[-1] = weight

    def randomWeight(self, beg, end):
        self.__weight[-1] = uniform(beg, end)
    
    def probagate(self, argin):
        return self.__weight[-1] * argin

Synapse.register(DirectSynapse)
