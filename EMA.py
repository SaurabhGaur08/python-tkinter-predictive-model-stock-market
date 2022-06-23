import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#Exponential Moving Average
def ema(window, stock, stock_column, ema_window):
    print("Exponential Moving Average ")
    
    newWindow = tk.Toplevel(window)

    plt.style.use('fivethirtyeight')
    
    stock['EMA_{}'.format(ema_window)] = stock[stock_column].ewm(span = ema_window, adjust = False).mean()
    
    figure = Figure(figsize=(7,6), dpi = 100)
    ax = figure.add_subplot(111)
    ax.plot(stock['EMA_{}'.format(ema_window)], label='EMA with {} window size'.format(ema_window))
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
    
    
    
        
