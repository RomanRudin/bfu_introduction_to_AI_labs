import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.metrics import accuracy_score
from sklearn.linear_model import Perceptron as SkPerceptron
from sklearn.svm import SVC
from typing import Literal

class Perceptron:
    def __init__(self, random_weights=True, n_epochs=100, activation='step') -> None:
        self.random_weights = random_weights
        self.n_epochs = n_epochs
        self.activation = activation
        self.weights = None

    def _activate(self, x) -> Literal[1] | Literal[0] | Literal[-1]:
        if self.activation == 'step':
            return 1 if x >= 0 else 0
        elif self.activation == 'sign':
            return 1 if x >= 0 else -1
        else:
            raise ValueError("Неизвестная функция активации")

    def fit(self, X, y) -> None:
        n_samples, n_features = X.shape
        if self.random_weights:
            self.weights = np.random.rand(n_features + 1)  # +1 для смещения
        else:
            self.weights = np.zeros(n_features + 1)

        X = np.hstack((X, np.ones((n_samples, 1))))  # Добавляем смещение

        for _ in range(self.n_epochs):
            for i in range(n_samples):
                linear_output = np.dot(X[i], self.weights)
                prediction = self._activate(linear_output)
                error = y[i] - prediction
                self.weights += error * X[i]

    def predict(self, X) -> np.NDArray:
        X = np.hstack((X, np.ones((X.shape[0], 1))))
        linear_output = np.dot(X, self.weights)
        return np.array([self._activate(x) for x in linear_output])

# Генерация данных
data, labels = make_blobs(
    n_samples=500,
    centers=([1.1, 3], [4.5, 6.9]),
    cluster_std=1.3,
    random_state=0
)

# Визуализация данных
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
plt.title("Сгенерированные данные")
plt.show()

# Обучение перцептрона
X = data
y = labels
perceptron = Perceptron(random_weights=True, n_epochs=100)
perceptron.fit(X, y)

# Предсказание и оценка точности
y_pred = perceptron.predict(X)
accuracy = accuracy_score(y, y_pred)
print(f"Точность самописного перцептрона: {accuracy:.2f}")