import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from sklearn.datasets import load_iris, make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target
# print(iris.target_names)
# print(iris.target)
print(df.head())
print(df.info())



#? Ex1
colors = {0: 'red', 1: 'green', 2: 'blue'}
fig, ((plot_sepal), (plot_petal)) = plt.subplots(1, 2) 
plot_sepal.set_title('Sepal Length to Sepal Width')

def plot_length_to_width(plot, name: str) -> None:
    plot.set_title(f'{name.capitalize()} Length to {name.capitalize()} Width')
    for target in np.unique(iris.target):
        plot.scatter(
            df[df['target'] == target][f'{name} length (cm)'],
            df[df['target'] == target][f'{name} width (cm)'],
            c=colors[target],
            label=iris.target_names[target]
        )
    plot.set_xlabel(f'{name.capitalize()} Length (cm)')
    plot.set_ylabel(f'{name.capitalize()} Width (cm)')
    plot.legend()

plot_length_to_width(plot_sepal, 'sepal')
plot_length_to_width(plot_petal, 'petal')
plt.show()



#? Ex2
seaborn.pairplot(df, hue='target', palette='viridis')
plt.suptitle('Pairplot of Iris Dataset', y=1.02)
plt.show()



#? Ex3
df1 = df[df['target'].isin([0, 1])]
df2 = df[df['target'].isin([1, 2])]



#? Ex4, Ex5, Ex6, Ex7
# Data separation
X1 = df1.drop('target', axis=1)                     # Ex4
y1 = df1['target']
X1_train, X1_test, y1_train, y1_test = train_test_split(X1, y1, test_size=0.2, random_state=42)

# Model training
clf1 = LogisticRegression(random_state=0)           # Ex4
clf1.fit(X1_train, y1_train)                        # Ex5

# Prediction and evaluation
y1_pred = clf1.predict(X1_test)                     # Ex6
accuracy1 = clf1.score(X1_test, y1_test)            # Ex7
print(f'Accuracy for first dataset: {accuracy1:.2f}')


# Data separation
X2 = df2.drop('target', axis=1)                     # Ex4
y2 = df2['target']
X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y2, test_size=0.2, random_state=42)

# Model training
clf2 = LogisticRegression(random_state=0)           # Ex4
clf2.fit(X2_train, y2_train)                        # Ex5

# Prediction and evaluation
y2_pred = clf2.predict(X2_test)                     # Ex6
accuracy2 = clf2.score(X2_test, y2_test)            # Ex7
print(f'Accuracy for second dataset: {accuracy2:.2f}')



#? Ex9
X, y = make_classification(
    n_samples=1000,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    random_state=1,
    n_clusters_per_class=1
)

plt.figure(figsize=(10, 6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Generated Dataset')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf_gener = LogisticRegression(random_state=0)
clf_gener.fit(X_train, y_train)
accuracy_gener = clf_gener.score(X_test, y_test)
print(f'Accuracy for generated data: {accuracy_gener:.2f}')