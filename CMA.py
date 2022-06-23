import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#Cummulative Moving Average
def cma(window, stock, stock_column, cma_window):
    
    newWindow = tk.Toplevel(window)
    plt.style.use('fivethirtyeight')
    
    stock['CMA_{}'.format(cma_window)] = stock[stock_column].expanding(cma_window).mean()
    
    figure = Figure(figsize=(7,6), dpi = 100)
    ax = figure.add_subplot(111)
    ax.plot(stock['CMA_{}'.format(cma_window)], label='CMA with {} window size'.format(cma_window))
    figure.autofmt_xdate()
    figure.tight_layout() 
    
    canvas = FigureCanvasTkAgg(figure, master = newWindow)
    newWindow.title("CMA")
    ax.set_ylabel('Price')
    ax.set_xlabel('Date')
    plt.rcParams["font.size"] =7
    plt.subplots_adjust(bottom=0.15)
    
    canvas.get_tk_widget().grid(row = 5, column = 3, padx = 10)
    canvas.draw()
    
    
    
        
