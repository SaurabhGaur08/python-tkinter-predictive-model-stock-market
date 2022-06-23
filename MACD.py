import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#Moving Average Convergence/Divergence
def macd(window, stock, column):
    
    newWindow = tk.Toplevel(window)  
    plt.style.use('fivethirtyeight')
    
    exp1 = stock[column].ewm(span = 12, adjust = False).mean()
    exp2 = stock[column].ewm(span = 26, adjust = False).mean()
    macd = exp1 - exp2
        
    figure = Figure(figsize=(7,6), dpi = 100)
    ax = figure.add_subplot(111)
    ax.plot(macd, label = 'MACD')
    figure.autofmt_xdate()
    figure.tight_layout()     
    
    canvas = FigureCanvasTkAgg(figure, master = newWindow)
    newWindow.title("MACD")
    ax.set_ylabel('Price')
    ax.set_xlabel('Date')
    plt.rcParams["font.size"] =7
    plt.subplots_adjust(bottom=0.15)
    canvas.get_tk_widget().grid(row = 0, column = 0, padx = 10)
    canvas.draw()
