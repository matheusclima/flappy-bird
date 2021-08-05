# Matriz de pesos
# Sigmoid(x) = 1/(1+exp(-x))

import numpy as np
from scipy.special import expit  # Sigmoid function


class NeuralNetwork:

    hidden_weights = None
    output_weights = None
    hidden_bias = None
    output_bias = None
    learning_rate = 0.1

    def __init__(self, n_input, n_hidden, n_output):
        self.hidden_weights = self.__random_matrix(n_hidden, n_input)
        self.output_weights = self.__random_matrix(n_output, n_hidden)

        self.hidden_bias = self.__random_matrix(n_hidden, 1)
        self.output_bias = self.__random_matrix(n_output, 1)

    def feedfoward(self, inputs):
        hidden_output = self.__hidden_output(inputs)

        return self.__output(hidden_output)

    def train(self, inputs, answers):
        hidden_output = self.__hidden_output(inputs)
        output = self.__output(hidden_output)
        error = np.array([answers]).T - output
        # Delta_Bias eh o gradiente
        delta_output_bias = self.gradient(output, error)
        # Delta_Weight eh o gradiente vezes o output da camada
        delta_weight_ho = np.dot(delta_output_bias, hidden_output.T)
        # Atualizar os pesos
        self.output_bias += delta_output_bias
        self.output_weights += delta_weight_ho

        # Backprogragation
        hidden_errors = np.dot(self.output_weights.T, error)

        delta_hidden_bias = self.gradient(hidden_output, hidden_errors)
        delta_weight_ih = np.dot(delta_hidden_bias, np.array([inputs]))
        self.hidden_bias += delta_hidden_bias
        self.hidden_weights += delta_weight_ih

    def __random_matrix(self, rows, columns):
        return 2 * (np.random.rand(rows, columns) - 0.5)

    def gradient(self, output, error):
        f = np.vectorize(self.__sigmoid_derivative)
        return self.learning_rate * np.multiply(f(output), error)

    def __hidden_output(self, inputs):
        hidden_output = np.dot(self.hidden_weights, np.array([inputs]).T) + self.hidden_bias
        # Activation function
        hidden_output = expit(hidden_output)
        return hidden_output

    def __output(self, hidden_output):
        output = np.dot(self.output_weights, hidden_output) + self.output_bias
        # Activation function
        output = expit(output)
        return output

    def __sigmoid_derivative(self, e):
        return np.multiply(e, (1 - e))
