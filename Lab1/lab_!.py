import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd

# General/
fig, ((plot3, plot5), (plot6, info)) = plt.subplots(2, 2) 
info.axis('off')

# plot3 = plt.subplot(2, 2, 1) 
# plot5 = plt.subplot(2, 2, 2)
# plot6 = plt.subplot(2, 2, 3)
# info = plt.subplot(2, 2, 4)


plot3.set_title('Initial points') 
plot5.set_title('Linear regression') 
plot6.set_title('SSE with squares') 


# Ex1
df = pd.read_csv(r'Lab1/student_scores.csv')
# df = pd.read_csv(input("Please, enter the path from current working directory to tour file:"))


# Ex2
print(df.describe())


# Ex3
print("How you want your graph to look like? Write down the срщыут variant number:")
columns_variants = [
    (df.columns[0], df.columns[1]),
    (df.columns[1], df.columns[0])
    ]
for index, line in enumerate(columns_variants):
    print(f"{index + 1}. " + ' : '.join(line))
chosen_variant = int(input())

def plotting(x: list, y: list, chosen_columns_variant: tuple[str, str]) -> None:
    plot3.scatter(x, y)
    print(chosen_columns_variant)
    plot3.set_title(str(chosen_columns_variant))
    plot3.set_xlabel(chosen_columns_variant[0])
    plot3.set_ylabel(chosen_columns_variant[1])
    # plot3.set_aspect('equal', adjustable='box')


    # Ex4
    n = len(x)
    w1 = (1/n * sum([xi * sum(y) for xi in x]) - sum([y[i] * x[i] for i in range(n)])) / \
        (1/n * sum([xi * sum(x) for xi in x]) - sum([xi**2 for xi in x]))
    w0 = sum([y[i]- w1 * x[i] for i in range(n)]) / n


    # Ex5
    plot5.scatter(x, y)
    plot5.set_xlabel(chosen_columns_variant[0])
    plot5.set_ylabel(chosen_columns_variant[1])
    
    plot5.axline(xy1=(0, w0), slope=w1, color='red')

    
    # Ex6
    plot6.scatter(x, y)
    plot6.set_xlabel(chosen_columns_variant[0])
    plot6.set_ylabel(chosen_columns_variant[1])
    

    # draw and fill error squares
    plot6.axline(xy1=(0, w0), slope=w1, color='red')
    difference_between_scales = (plot6.get_xlim()[1] - plot6.get_xlim()[0]) / (plot6.get_ylim()[1] - plot6.get_ylim()[0])
    print(difference_between_scales)
    for i in range(n):
        if (y[i] < w0 + w1 * x[i]):
            patch = patches.Rectangle((x[i], y[i]), -abs(w0 + w1 * x[i] - y[i]) * difference_between_scales, abs(w0 + w1 * x[i] - y[i]), color='green', alpha=0.2)
        else:
            patch = patches.Rectangle((x[i], w0 + w1 * x[i]), abs(w0 + w1 * x[i] - y[i]) * difference_between_scales, abs(w0 + w1 * x[i] - y[i]), color='green', alpha=0.2)
        plot6.add_patch(patch)






match chosen_variant:
    case 1:
        plotting(df[df.columns[0]], df[df.columns[1]], columns_variants[0])
    case 2:
        plotting(df[df.columns[1]], df[df.columns[0]], columns_variants[1])
    case _:
        Exception("There is no such variant")


# General
plt.tight_layout() 
plt.show()