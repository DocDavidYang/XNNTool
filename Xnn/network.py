from abc import *

class NetWork:
    
    __metaclass__ = ABCMeta

    def __init__(self):
        self.__id = None
        self.__neuron = {}
        self.__neuron_num = 0
        self.__synapse = {}
        self.__synapse_num = 0
        self.__connection = {}
        self.__inputNeuron = set()
        self.__outputNeuron = set()

    @abstractmethod
    def createNeuron(self, **argin):
        pass

    @abstractmethod
    def insertNeuron(self, neuron):
        pass

    @abstractmethod
    def createSynapse(self, **argin):
        pass

    @abstractmethod
    def insertSynapse(self, synapse):
        pass

    @abstractmethod
    def initialize(self):
        pass

    @abstractproperty
    def networkId(self):
        pass

    @abstractproperty
    def output(self):
        pass

    @abstractmethod
    def probagate(self, *argin):
        pass

    @abstractmethod
    def epochBatch(self, inputSet, outputSet):
        pass

    @abstractmethod
    def epochOnLine(self, inputValue, outputValue):
        pass

    @abstractmethod
    def train(self, inputSet, outputSet, trainType):
        pass
