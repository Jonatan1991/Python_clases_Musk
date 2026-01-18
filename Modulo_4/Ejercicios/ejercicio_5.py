# Repite el ejercicio anterior esta vez creando una
# interfaz informal.


class Interfaz:
    def preprocess_data(self):
        pass
    def fit(self):
        pass
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

    def fit(self):
        print('Training at DecisionTree')

    def predict(self):
        print('Evaluating at DecisionTree')

svm = SVM()
svm.preprocess_data(data=None, y=None)
svm.fit()
svm.predict()

dt = DecisionTree()
dt.preprocess_data(data=None, y=None)
dt.fit()
dt.predict()