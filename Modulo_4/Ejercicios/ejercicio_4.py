"""
Dadas las siguientes clases con el output de sus
respectivos métodos, crea una interfaz formal
que las implemente.

svm = SVM()
svm.preprocess_data(data=None, y=None)
svm.fit()
svm.predict()
dt = DecisionTree()
dt.preprocess_data(data=None, y=None)
dt.fit(O)
dt.predict()

output:
Preprocessing data at SVM
Training at SVM
Evaluating at SVM
Preprocessing data at DecisionTree
Training at DecisionTree
Evaluating at DecisionTree

Preprocessing data at SVM
Training at SVM
Evaluating at SVM
Preprocessing data at DecisionTree
Training at DecisionTree
Evaluating at DecisionTree

"""

from abc import abstractmethod
from abc import ABCMeta

class Interfaz(metaclass=ABCMeta):

    @abstractmethod
    def preprocess_data(self, data, y):
        pass

    @abstractmethod
    def fit(self):
        pass

    @abstractmethod
    def predict(self):
        pass

class SVM(Interfaz):

    def preprocess_data(self, data, y):
        self.data = data
        self.y = y

        print('Preprocessing data at SVM')

    def fit(self):
        print('Training at SVM')

    def predict(self):
        print('Evaluating at SVM')

class DecisionTree(Interfaz):

    def preprocess_data(self, data, y):
        self.data = data
        self.y = y
        print('Preprocessing data at DecisionTree')

    def fit(self, data):
        print('Training at DecisionTree')

    def predict(self):
        print('Evaluating at DecisionTree')

svm = SVM()
svm.preprocess_data(data=None, y=None)
svm.fit()
svm.predict()
dt = DecisionTree()
dt.preprocess_data(data=None, y=None)
dt.fit(0)
dt.predict()