class CivilEngineer:

    def __init__(self):
        inputs = []

        mixDesignTypes[0] = ['M5', 1, 5, 10]
        mixDesignTypes[1] = ['M7.5', 1, 4, 8]
        mixDesignTypes[2] = ['M10', 1, 3, 6]
        mixDesignTypes[3] = ['M15', 1, 2, 4]
        mixDesignTypes[4] = ['M20', 1, 1.5, 3]
        mixDesignTypes[5] = ['M25', 1, 1, 2]
        mixDesignTypes[6] = ['M30', 1, 1, 1.5]

        structElement[0] = {'element':'screed', 'mix': {'M10':3, 'M7.5':2, 'M5':1}}
		structElement[1] = {'element':'beam', 'mix':{'M20':3, 'M15':2, 'M10':1}}
		structElement[2] = {'element':'slab', 'mix':{'M25':3, 'M20':2, 'M15':1}}
		structElement[3] = {'element':'column', 'mix':{'M30':3, 'M25':2, 'M20':1}}

    def getInputs(self):
        userInputs = input()

        foreach x in userInputs.split(" "):
            inputs.append(int(x))

    
    def calDesignRatio(self, kg, element):
        if element == 'screed':

    
    def calMaterialWeight(self, mixType, kg):

            




    
