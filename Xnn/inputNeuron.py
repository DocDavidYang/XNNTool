from Xnn.neuron import Neuron

class InputNeuron(object):

    def __init__(self, neuron_id = None):
        Neuron.__init__(self)
        self.__id = neuron_id
        self.__local.append(0)
        self.__output.append(0)

    def __accumulate(self, *argin):
        self.__local[0] = argin[0]

    def __activate(self):
        self.__output[0] = self.__local[0]

    def probagate(self, *argin):
        self.__accumulate(*argin)
        self.__activate()
        return self.__output[0]

    def neuronId():
        return self.__id

    def local(self):
        return self.__local

    def output(self):
        return self.__output

Neuron.register(InputNeuron)
