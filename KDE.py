import tkinter as tk
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Kernel density estimation (KDE) of the daily return
def kde(window, stock):
            
    newWindow = tk.Toplevel(window)  
    plt.style.use('fivethirtyeight')
    
    
    sns.set_style('whitegrid')
    figure = Figure(figsize=(7,6), dpi = 100)
    ax = figure.add_subplot(111)
    sns.kdeplot(np.array(stock['Daily_Return']), bw=0.5, ax=ax)
    
    figure.autofmt_xdate()
    figure.tight_layout() 
    
    canvas = FigureCanvasTkAgg(figure, master = newWindow)
    newWindow.title("KDE of the Daily return")
    ax.set_ylabel('Density')
    plt.rcParams["font.size"] =7
    plt.subplots_adjust(bottom=0.15)
    canvas.get_tk_widget().grid(row = 0, column = 0, padx = 10)
    canvas.draw()