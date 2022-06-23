import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import mplfinance as mpf

#Candle Stick Graph
def candlestick(window, stock):
    
    newWindow = tk.Toplevel(window)

    plt.style.use('fivethirtyeight')   

    figure = Figure(figsize=(7,6), dpi = 100)
    ax = figure.add_subplot(111)
    mpf.plot(stock, type='candle', style='charles', figsize=(17,7), ax=ax)
    figure.autofmt_xdate()
    figure.tight_layout() 

    canvas = FigureCanvasTkAgg(figure, master = newWindow)
    newWindow.title("Candle Stick")
    plt.subplots_adjust(bottom=0.15)
    canvas.get_tk_widget().grid(row = 0, column = 0, padx = 10)
    canvas.draw()
    
