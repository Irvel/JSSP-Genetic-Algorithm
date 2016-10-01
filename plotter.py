import plotly.graph_objs as go
import plotly.plotly as py
from plotly.tools import FigureFactory as FF
import matplotlib.pyplot as plt


def plot(x_data, y_data):
    # x_data = iteration_numbers
    # y_data = makespans
    # colorscale = ['#7A4579', '#D56073', 'rgb(236,158,105)', (1, 1, 0.2), (0.98,0.98,0.98)]
    # fig = FF.create_2D_density(
    #     x_data, y_data, colorscale=colorscale,
    #     hist_color='rgb(255, 237, 222)', point_size=3
    # )

    # py.plot(fig, filename='histogram_subplots')

    # trace = go.Scattergl(
    #     x = x_data,
    #     y = y_data,
    #     mode = 'lines',
    #     marker = dict(
    #         color = 'rgb(152, 0, 0)',
    #         line = dict(
    #             width = 1,
    #             color = 'rgb(0,0,0)')
    #     )
    # )
    # data = [trace]
    # py.plot(data, filename='goodthick')
    plt.plot(x_data, y_data, 'ro')
    plt.title("Initial population: " + str(100) + " Iteration Numbers: " + str(len(x_data)))
    plt.ylabel("Makespan")
    plt.xlabel("Generation")
    plt.show()