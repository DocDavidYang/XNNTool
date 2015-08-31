from Xnn.netWork import NetWork
from Xnn.inputNeuron import InputNeuron
from Xnn.perceptron import Perceptron

class MLP(object):

    def __init__(self, netWork_id = None, *argin):
        NetWork.__init__(self)
        self.__id = netWork_id
        self.initialize(argin)

    def createNeuron(self, **argin):
        if argin['type'] == 'InputNeuron':
            return InputNeuron(argin['id'])
        if argin['type'] == 'Perceptron':
            return Perceptron(argin['id'], argin['mode'], argin['stateNum'])
        raise Exception('neuron type is not existed')

    def insertNeuron(self, neuron, neuronType = 'hidden'):
        if neuron.neuronId in self.__neuron:
            raise Exception('neuron is already existed')
        self.__neuron[neuron.neuronId] = neuron
        self.__neuron_num += 1
        if neuronType == 'input':
            self.__inputNeuron.add(neuron.neuronId)
        elif neuronType == 'output':
            self.__outputNeuron.add(neuron.neuronId)
        else:
            pass

    def createSynapse(self, **argin):
        if argin['type'] == 'DirectSynapse':
            return DirectSynapse(argin['id'], argin['src'], argin['des'], argin['stateNum'])
        raise Exception('synapse type is not existed')

    def insertSynapse(self, synapse):
        if synapse.synapseId in self.__synapse:
            raise Exception('synapse is already existed')
        if synapse.src not in self.__neuron and synapse.des not in self.__neuron:
            raise Exception('neurons assigned are not existed')
        self.__synapse[synapse.synapseId] = synapse
        self.__synapse_num += 1
        if synapse.src in self.__connection:
            self.__connection[src][des] = synapse.synapseId
        else:
            self.__connection[src] = {des: synapse.synapseId}
        if synapse.des in self.__connection:
            self.__connection[des][src] = -synapse.synapseId
        else:
            self.__connection[des] = {src: -synapse.synapseId}

    def initialize(self, argin):
        if len(argin) < 2:
            raise Exception('network must has an output layer')
        self.__layer = argin
        for i in range(argin[0]):
            param = {'type': 'InputNeuron', 'id': self.__neuron_num + 1}
            inputLayerNode = self.createNeuron(**param)
            self.insertNeuron(inputLayerNode, 'input')
        for layer in range(1, len(argin)):
            for i in range(argin[layer]):
                param = {'type': 'Perceptron', 'id': self.__neuron_num + 1, 'mode': 'Logistic', 'stateNum': 1}
                featureLayerNode = self.createNeuron(**param)
                if layer = len(argin) - 1:
                    self.insertNeuron(featureLayerNode, 'output')
                else:
                    self.insertNeuron(featureLayerNode, 'hidden')
                for pre_id in range(sum(argin[0:layer - 1]) + 1, sum(argin[0:layer]) + 1):
                    param = {'type': 'DirectSynapse', 'id': self.__synapse_num + 1, 'src': pre_id, 'des': self.__neuron_num, 'stateNum': 2}
                    layerLink = createSynapse(**param)
                    layerLink.randomWeight(-1, 1)
                    self.insertSynapse(layerLink)

    def networkId(self):
        return self.__id

    def output(self):
        return self.__neuron[-len(self.__outputNeuron):]

    def probagate(self, *argin):
        if len(argin) != self.__layer[0]:
            raise Exception('number of parameter is not equal with number of input neuron')
        for i in range(self.__layer[0]):
            self.__neuron[i+1].probagate(argin[i])
        for layer in range(1, len(self.__layer)):
            for i in range(sum(self.__layer[0:layer]) + 1, sum(self.__layer[0:layer + 1]) + 1):
                temp = []
                for j in range(sum(argin[0:layer - 1]) + 1, sum(argin[0:layer]) + 1):
                    l = self.__connection[j][i]
                    temp.append(self.__synapse(l).probagate(self.__neuron[j].output()))
                self.__neuron[i].probagate(*temp)

    def __backprobagate(self, error, learningRate):
        delta_cur = []
        delta_pre = []
        for i in range(len(error)):
            delta_cur.append(error[i] * self.__neuron[-len(self.__outputNeuron) + i] * (1 - self.__neuron[-len(self.__outputNeuron) + i]))
        for layer, layerNum in enumerate(self.__layer[-2::-1]):
            layer = len(self.__layer) - layer - 2
            for i in range(layerNum):
                i = sum(self.__layer[0:layer]) + i + 1
                delta_pre.append(0)
                for jn in range(self.__layer[layer + 1]):
                    j = sum(self.__layer[0:layer + 1]) + jn + 1
                    delta_pre[-1] += delta_cur[jn] * self.__synapse[ self.__connection[i][j] ].weight
                    self.__synapse[ self.__connection[i][j] ].weight += learningRate * delta_cur[jn] * self.__neuron[i].output
                delta_pre[-1] *= self.__neuron[i].output * (1 - self.__neuron[i].output)
            delta_cur = delta_pre
            delta_pre = []

    def epochBatch(self, inputSet, outputSet, learningRate):
        pass

    def epochOnLine(self, inputValue, outputValue, learningRate):
        if (len(inputValue) != len(self.__inputNeuron) or len(outputValue) != len(self.__outputNeuron)):
            raise Exception('number of trainning data is not fit to network')
        self.probagate(*inputValue)
        error = []
        for i in range(len(outputValue)):
            error.append(outputValue[i] - self.__neuron[-len(self.__outputNeuron) + i])
        self.__backprobagate(error, learningRate)
        return sum([0.5 * e * e for e in error])

    def train(self, inputSet, outputSet, trainType = 'OnLine', learningRate = 0.1, maxIteration = 200, errorLimit = 0):
        for epoch in range(maxIteration):
            error = 0
            if trainType = 'OnLine':
                for i in range(len(inputSet)):
                    error += epochOnLine(inputSet[i], outputSet[i], learningRate)
                error /= len(inputSet)

            if error <= errorLimit:
                return

NetWork.register(MLP)
