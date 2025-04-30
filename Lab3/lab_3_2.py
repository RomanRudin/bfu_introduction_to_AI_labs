# Использование перцептрона из Scikit-Learn
sk_perceptron = SkPerceptron(max_iter=100, random_state=0)
sk_perceptron.fit(X, y)
y_pred_sk = sk_perceptron.predict(X)
accuracy_sk = accuracy_score(y, y_pred_sk)
print(f"Точность Scikit-Learn Perceptron: {accuracy_sk:.2f}")

# Сравнение с SVM на данных Iris
from sklearn.datasets import load_iris
iris = load_iris()
X_iris = iris.data[-100:]  # Последние 100 записей (классы 1 и 2)
y_iris = iris.target[-100]

# Обучение SVM
svm = SVC(kernel='linear')
svm.fit(X_iris, y_iris)
y_pred_svm = svm.predict(X_iris)
accuracy_svm = accuracy_score(y_iris, y_pred_svm)
print(f"Точность SVM на Iris: {accuracy_svm:.2f}")

# Обучение Scikit-Learn Perceptron на Iris
sk_perceptron_iris = SkPerceptron(max_iter=100, random_state=0)
sk_perceptron_iris.fit(X_iris, y_iris)
y_pred_sk_iris = sk_perceptron_iris.predict(X_iris)
accuracy_sk_iris = accuracy_score(y_iris, y_pred_sk_iris)
print(f"Точность Scikit-Learn Perceptron на Iris: {accuracy_sk_iris:.2f}")