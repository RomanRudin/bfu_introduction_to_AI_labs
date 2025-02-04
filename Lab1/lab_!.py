import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Ex1
df = pd.read_csv(r'Lab1/student_scores.csv')

print(df.describe())

df.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours')
plt.ylabel('Score')
