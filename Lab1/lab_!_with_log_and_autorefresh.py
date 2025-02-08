import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
from math import log

#? Subplots
fig, ((plot3, plot5), (plot6, plot6_log)) = plt.subplots(2, 2) 
# info.axis('off')

# plot3 = plt.subplot(2, 2, 1) 
# plot5 = plt.subplot(2, 2, 2)
# plot6 = plt.subplot(2, 2, 3)
# info = plt.subplot(2, 2, 4)

plot3.set_title('Initial points') 
plot5.set_title('Linear regression') 
plot6.set_title('MSE with squares') 
plot6_log.set_title('MSE with squares and logarythmic scale') 


def plot_initial_data(x: list, y: list, chosen_columns_variant: tuple[str, str]) -> None:
    plot3.scatter(x, y, color='blue')
    # print(f"Chosen columns variant: {chosen_columns_variant}")
    plot3.set_title(str(chosen_columns_variant))
    plot3.set_xlabel(chosen_columns_variant[0])
    plot3.set_ylabel(chosen_columns_variant[1])
    # plot3.set_aspect('equal', adjustable='box')


#? Ex4
def calculate_regression_parameters(x: list, y: list) -> tuple[float, float]:
    n = len(x)
    w1 = (1/n * sum([xi * sum(y) for xi in x]) - sum([y[i] * x[i] for i in range(n)])) / \
        (1/n * sum([xi * sum(x) for xi in x]) - sum([xi**2 for xi in x]))
    w0 = sum([y[i]- w1 * x[i] for i in range(n)]) / n
    return w0, w1


#? Ex5
def plot_regression(x: list, y: list, w0: int, w1: int, chosen_columns_variant: tuple[str, str]) -> None:
    plot5.scatter(x, y, color='blue')
    plot5.set_xlabel(chosen_columns_variant[0])
    plot5.set_ylabel(chosen_columns_variant[1])
    
    plot5.axline(xy1=(0, w0), slope=w1, color='red')

    
#? Ex6
def plot_regression_with_squares(x: list, y: list, w0: int, w1: int, chosen_columns_variant: tuple[str, str]) -> None:
    plot6.scatter(x, y, color='blue')
    plot6.set_xlabel(chosen_columns_variant[0])
    plot6.set_ylabel(chosen_columns_variant[1])
    y_pred = [w0 + w1 * xi for xi in x]
    
    #? Regression
    plot6.axline(xy1=(0, w0), slope=w1, color='red')

    #? Size of the figure
    bbox = plot6.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    #? Difference between scales inculding difference between sizes of axes
    difference_between_scales = (plot6.get_xlim()[1] - plot6.get_xlim()[0]) / (plot6.get_ylim()[1] - plot6.get_ylim()[0]) / (bbox.width / bbox.height)
    print(f"difference between axes scales: {difference_between_scales}")
    
    for patch in plot6.patches:
        patch.remove()
    for i in range(len(x)):
        if (y[i] < y_pred[i]):
            patch = patches.Rectangle((x[i], y[i]), -abs(y_pred[i] - y[i]) * difference_between_scales, abs(y_pred[i] - y[i]), color='green', alpha=0.4)
        else:
            patch = patches.Rectangle((x[i], y_pred[i]), abs(y_pred[i] - y[i]) * difference_between_scales, abs(y_pred[i] - y[i]), color='green', alpha=0.4)
        plot6.add_patch(patch)


def plot_regression_with_squares_logarythmic(x: list, y: list, w0: int, w1: int, chosen_columns_variant: tuple[str, str]) -> None:
    def __plot_regression_with_squares_logarythmic(x, y, w0, w1) -> None:
        #? Unable to use .axline() for logarythmic scale, so trying another thing here:
        x_new = np.linspace(min(0, min(x) * 1.2), max(0, max(x) * 1.2), 1000)
        plot6_log.plot(x_new, w0 + w1 * x_new, color='red')
        #? Draw and fill error squares
        for i in range(len(x)):
            if (y[i] < y_pred[i]):
                patch = patches.Rectangle((x[i], y[i]), -abs(y_pred[i] - y[i]) * difference_between_scales, abs(y_pred[i] - y[i]), color='green', alpha=0.4)
            else:
                patch = patches.Rectangle((x[i], y_pred[i]), abs(y_pred[i] - y[i]) * difference_between_scales, abs(y_pred[i] - y[i]), color='green', alpha=0.4)
            plot6_log.add_patch(patch)

    plot6_log.scatter(x, y, color='blue')
    plot6_log.set_xlabel(chosen_columns_variant[0])
    plot6_log.set_ylabel(chosen_columns_variant[1])
    y_pred = [w0 + w1 * xi for xi in x]

    for patch in plot6_log.patches:
        patch.remove()

    #? Size of the figure
    bbox = plot6.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    #? Difference between scales inculding difference between sizes of axes
    difference_between_scales = (plot6.get_xlim()[1] - plot6.get_xlim()[0]) / (plot6.get_ylim()[1] - plot6.get_ylim()[0]) / (bbox.width / bbox.height)

    if difference_between_scales < 1:
        plot6_log.set_yscale('log')
    else:
        plot6_log.set_xscale('log')

    __plot_regression_with_squares_logarythmic(x, y, w0, w1)


def on_resize(x: list, y: list, w0: int, w1: int) -> None:
    plt.ion()
    plot_initial_data(x, y, columns_variants[chosen_variant - 1])
    plot_regression(x, y, w0, w1, columns_variants[chosen_variant - 1])
    plot_regression_with_squares(x, y, w0, w1, columns_variants[chosen_variant - 1])
    plot_regression_with_squares_logarythmic(x, y, w0, w1, columns_variants[chosen_variant - 1])
    fig.canvas.draw()
    plt.ioff()



if __name__ == "__main__":
    #? Ex1
    df = pd.read_csv(r'Lab1/student_scores.csv')
    #? df = pd.read_csv(input("Please, enter the path from current working directory to tour file:"))


    #? Ex2
    print(df.describe())


    #? Ex3
    print("How you want your graph to look like? Write down the срщыут variant number:")
    columns_variants = [
        (df.columns[0], df.columns[1]),
        (df.columns[1], df.columns[0])
        ]
    for index, line in enumerate(columns_variants):
        print(f"{index + 1}. " + ' : '.join(line))
    chosen_variant = int(input())


    match chosen_variant:
        case 1:
            x, y = df[df.columns[0]], df[df.columns[1]]
        case 2:
            x, y = df[df.columns[1]], df[df.columns[0]]
        case _:
            Exception("There is no such variant")

    plot_initial_data(x, y, columns_variants[chosen_variant - 1])
    #? Ex4
    w0, w1 = calculate_regression_parameters(x, y)
    #? Ex5
    plot_regression(x, y, w0, w1, columns_variants[chosen_variant - 1])
    #? Ex6
    plot_regression_with_squares(x, y, w0, w1, columns_variants[chosen_variant - 1])
    #plot6_log.axis("off")
    plot_regression_with_squares_logarythmic(x, y, w0, w1, columns_variants[chosen_variant - 1])

    fig.canvas.mpl_connect('resize_event', lambda func: on_resize(x, y, w0, w1))


    #? General
    plt.tight_layout() 
    plt.show()