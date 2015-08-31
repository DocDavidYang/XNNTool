class dataset(object):

    def __init__(self, inputNum, outputNum):
        self.__inputNum = inputNum
        self.__input = []
        self.__minInput = [0] * inputNum
        self.__maxInput = [1] * inputNum
        self.__outputNum = outputNum
        self.__output = []
        self.__minOutput = [0] * outputNum
        self.__maxOutput = [1] * outputNum
        

    def inputTrainData(self, inputValue, outputValue):
        if len(inputValue) != inputNum or len(outputValue) != outputNum:
            raise Exception('Wrong number of input data or output data')
        self.__input.append(inputValue)
        for i in range(inputNum):
            if inputValue[i] < self.__minInput[i]:
                self.__minInput[i] = inputValue[i]
            elif inputValue[i] > self.__maxInput[i]:
                self.__maxInput[i] = inputValue[i]
            else:
                pass
        self.__output.append(outputValue)
        for i in range(outputNum):
            if outputValue[i] < self.__minOutput[i]:
                self.__minOutput[i] = outputValue[i]
            elif outputValue[i] > self.__maxOutput[i]:
                self.__maxOutput[i] = outputValue[i]
            else:
                pass

    def initialize(self):
        if not len(self.__input) || not len(self.__output):
            return
        for i in range(len(self.__input)):
            for j in range(inputNum):
                self.__input[i][j] -= self.__minInput[i]
                self.__input[i][j] /= self.__maxInput[i] - self.__minInput[i]
        for i in range(len(self.__output)):
            for j in range(outputNum):
                self.__output[i][j] -= self.__minOutput[i]
                self.__output[i][j] /= self.__maxOutput[i] - self.__minOutput[i]

    def getInput(self):
        return self.__input

    inputSet = property(getInput)

    def getOutput(self):

    outputSet = property(getOutput)

    def normalize(self, inputValue):
        if len(inputValue) != inputNum:
            raise Exception('Wrong number of input data')
        temp = []
        for i in range(inputNum):
            temp.append((inputValue[i] - self.__minInput[i])/(self.__maxInput[i] - self.__minInput[i]))
        return temp

    def unnormalize(self, outputValue):
        if len(outputValue) != outputNum:
            raise Exception('Wrong number of output data')
        temp = []
        for i in range(outputNum):
            temp.append(outputValue[i]*(self.__maxOutput[i] - self.__minOutput[i]) + self.__minOutput[i])
        return temp
