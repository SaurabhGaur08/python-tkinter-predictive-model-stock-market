import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def risk(window, stock, column):
    
    print("Stock Risk ")
    newWindow = tk.Toplevel(window)  
    # Scatter plot among stock risk and return

    # calculation of the percentage change between the current and the previous stock price
    retscomp = stock[column].pct_change()
    print(retscomp)
    
    x = retscomp.mean()
    y = retscomp.std()

    
    figure = Figure(figsize=(7,6), dpi = 100)
    ax = figure.add_subplot(111)
#   ax.scatter(retscomp.mean(), retscomp.std())
    ax.scatter(x, y)
    ax.annotate(
    "stock", 
    xy = (x, y), xytext = (20, -20),
    textcoords = 'offset points', ha = 'right', va = 'bottom',
    bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
    arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3, rad=0'))
    figure.autofmt_xdate()
    
      
    canvas = FigureCanvasTkAgg(figure, master = newWindow)
    newWindow.title("RISK")
    ax.set_ylabel('Risk')
    ax.set_xlabel('Expected returns')
    plt.rcParams["font.size"] =7
    plt.subplots_adjust(bottom=0.15)
    canvas.get_tk_widget().grid(row = 0, column = 0, padx = 10)
    canvas.draw()
