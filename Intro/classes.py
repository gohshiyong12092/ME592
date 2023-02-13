
class Model (object):
    #class initialization and attributes
    def __init__(self, params, model_type, name= 'Neutral Network'):
        self.name = name 
        self.params = params
        self.model_type = model_type
    #interal functions denoted by  ___._
    def __str__(self):
        return 'Readablel string : This is a ' + self.model_type + ' ' + self.name + ' with ' + str(self.params) + ' params'
    def __repr__(self):
        return self.model_type + ' ' + self.name + ' with ' + str(self.params) + ' params'
    #method
    def printParams(self, multipler):
        print(self.params*multipler)

ml = Model(5, 'Supervised', 'LinearRegression')
print(ml)
print(ml.name)
ml.printParams(10)