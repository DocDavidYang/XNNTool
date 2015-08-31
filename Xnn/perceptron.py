from math import exp

from Xnn.neuron import Neuron

class Perceptron(object):

    def __init__(self, neuron_id = None, activate_mode = 'Logistic', state_num = 1):
        Neuron.__init__(self)
        self.__id = neuron_id
        self.__mode = activate_mode
        self.__num = state_num
        for i in range(self.__num):
            self.__local.append(0)
            self.__output.append(0)

    def __accumulate(self, *argin):
        for i in range(self.__num - 1):
            self.__local[i] = self.__local[i+1]
        self.__local[-1] = sum(argin)

    def __activate(self):
        if not len(self.__local):
            return
        output = 0.0
        
        if self.activate_mode == 'Logistic':
            output = 1.0 / (1.0 + exp(-self.__local[-1]))

        for i in range(self.__num - 1):
            self.__output[i] = self.__output[i+1]
        self.__output[-1] = output

    def probagate(self, *argin):
        self.__accumulate(*argin)
        self.__activate()
        return self.__output[-1]

    def neuronId():
        return self.__id

    def local(self):
        return self.__local

    def output(self):
        return self.__output

Neuron.register(Perceptron)
