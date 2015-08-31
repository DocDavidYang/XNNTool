from abc import *

class Neuron:

    __metaclass__ = ABCMeta

    def __init__(self):
        self.__id = None
        self.__local = []
        self.__output = []

    @abstractmethod
    def __accumulate(self, *argin):
        pass

    @abstractmethod
    def __activate(self):
        pass

    @abstractmethod
    def probagate(self, *argin):
        pass

    @abstractproperty
    def neuronId():
        pass
    
    @abstractproperty
    def local(self):
        pass

    @abstractproperty
    def output(self):
        pass
