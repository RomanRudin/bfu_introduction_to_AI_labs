import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


diabetes = datasets.load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target
X = df[['bmi']].values
y = df['target'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=45)


sklearn_model = LinearRegression()
sklearn_model.fit(X_train, y_train)
y_pred_sklearn = sklearn_model.predict(X_test)
mse_sklearn = mean_squared_error(y_test, y_pred_sklearn)


class CustomLinearRegression:
    def __init__(self, learning_rate: float = 0.01, n_iter: float = 1000) -> None:
        self.learning_rate = learning_rate
        self.n_iter = n_iter
        self.w = None
        self.b = 0

    def fit(self, X: np.ndarray, y: np.ndarray) -> None:
        n_samples = X.shape[0]
        self.w = np.zeros(X.shape[1])

        for _ in range(self.n_iter):
            y_predictions = np.dot(X, self.w) + self.b
            dw = (2 / n_samples) * np.dot(X.T, (y_predictions - y))
            db = (2 / n_samples) * np.sum(y_predictions - y)
            self.w -= self.learning_rate * dw
            self.b -= self.learning_rate * db

    def predict(self, X: np.ndarray) -> np.ndarray:
        return np.dot(X, self.w) + self.b


custom_model = CustomLinearRegression()
custom_model.fit(X_train, y_train)
y_pred_custom = custom_model.predict(X_test)
mse_custom = mean_squared_error(y_test, y_pred_custom)


print()
print("Results:")
print(f"Sklearn MSE: {mse_sklearn:.2f}")
print(f"Coefficients sklearn: w={sklearn_model.coef_[0]:.2f}, b={sklearn_model.intercept_:.2f}")
print()
print(f"Custom MSE: {mse_custom:.2f}")
print(f"Coefficients custom: w={custom_model.w[0]:.2f}, b={custom_model.b:.2f}")

plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='black', label='Реальные значения')
plt.plot(X_test, y_pred_sklearn, color='red', linewidth=2, linestyle='dashed', label='Sklearn')
plt.plot(X_test, y_pred_custom, color='yellow', linestyle='dashed', label='Custom')
plt.xlabel('BMI')
plt.ylabel('Glucose level')
plt.title('Sklearn vs Custom')
plt.legend()
plt.grid(True)
plt.show()

results = pd.DataFrame({
    'Real date': y_test,
    'Predicted Sklearn': y_pred_sklearn,
    'Predicted Custom': y_pred_custom
})

print()
print("Predicted (first 20):")
print(results.head(20))