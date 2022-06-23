import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def sma(window, stock, stock_column, sma_window):
    
    
    print("Standard Moving Average ")
    print(sma_window)
    newWindow = tk.Toplevel(window)
        
    plt.style.use('fivethirtyeight')


    
   # stock['SMA_50'] = stock[stock_column].rolling(50).mean()
    stock['SMA_{}'.format(sma_window)] = stock[stock_column].rolling(sma_window).mean()
    #print(stock['SMA_{}'.format(sma_window)])
    
    figure = Figure(figsize=(7,6), dpi = 100)
    ax = figure.add_subplot(111)
    ax.plot(stock['SMA_{}'.format(sma_window)], label='SMA with {} window size'.format(sma_window))
    figure.autofmt_xdate()
    
      
    canvas = FigureCanvasTkAgg(figure, master = newWindow)
    newWindow.title("SMA")
    ax.set_ylabel('Price')
    ax.set_xlabel('Date')
    plt.rcParams["font.size"] =7
    plt.subplots_adjust(bottom=0.15)
    canvas.get_tk_widget().grid(row = 0, column = 0, padx = 10)
    canvas.draw()
        
