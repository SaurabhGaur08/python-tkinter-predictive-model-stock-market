import numpy as np
import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#Exponential Moving Average
def wma(window, stock, stock_column, wma_window):
    
    newWindow = tk.Toplevel(window)

    plt.style.use('fivethirtyeight')
        
    weights = np.arange(1, wma_window + 1) 
    print(weights)
    
    stock['WMA_{}'.format(wma_window)] = stock[stock_column].rolling(wma_window).apply(lambda prices: np.dot(prices, weights)/weights.sum(), raw=True)
    
    figure = Figure(figsize=(7,6), dpi = 100)
    ax = figure.add_subplot(111)
    ax.plot(stock['WMA_{}'.format(wma_window)], label='WMA with {} window size'.format(wma_window))
    figure.autofmt_xdate()
    figure.tight_layout() 
    
    canvas = FigureCanvasTkAgg(figure, master = newWindow)
    newWindow.title("EMA")
    ax.set_ylabel('Price')
    ax.set_xlabel('Date')
    plt.rcParams["font.size"] =7
    plt.subplots_adjust(bottom=0.15)

    canvas.get_tk_widget().grid(row = 5, column = 3, padx = 10)
    canvas.draw()
    
