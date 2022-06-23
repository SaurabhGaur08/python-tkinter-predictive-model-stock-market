import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#Line Plot Graph
def linePlot(window, stock, stock_column):

    newWindow = tk.Toplevel(window)

    figure = Figure(figsize=(7,6), dpi = 100)
    ax = figure.add_subplot(111)
    ax.plot(stock[stock_column])
    figure.autofmt_xdate()
    figure.tight_layout()    
      
    canvas = FigureCanvasTkAgg(figure, master = newWindow)
    newWindow.title("Line plot of {}".format(stock_column))
    ax.set_ylabel('{}'.format(stock_column))
    ax.set_xlabel('Date')
    plt.rcParams["font.size"] =7
    plt.subplots_adjust(bottom=0.15)


    canvas.get_tk_widget().grid(row = 0, column = 0, padx = 10)
    canvas.draw()
      
