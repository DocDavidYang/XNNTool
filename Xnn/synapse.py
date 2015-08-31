from abc import *

class Synapse:
    
    __metaclass__ = ABCMeta

    def __init__(self):
        self.__id = None
        self.__src = None
        self.__des = None
        self.__weight = []

    @abstractmethod
    def getSrc(self):
        pass

    @abstractmethod
    def setSrc(self, src):
        pass

    src = abstractproperty(getSrc, setSrc)

    @abstractmethod
    def getDes(self):
        pass

    @abstractmethod
    def setDes(self, des):
        pass

    des = abstractproperty(getDes, setDes)

    @abstractmethod
    def link(self, src = None, des = None):
        pass

    @abstractproperty
    def synapseId(self):
        pass

    @abstractmethod
    def getWeight(self):
        pass

    @abstractmethod
    def setWeight(self, weight):
        pass

    weight = abstractproperty(getWeight, setWeight)

    @abstractmethod
    def randomWeight(self, beg, end):
        pass

    @abstractmethod
    def probagate(self, argin):
        pass
