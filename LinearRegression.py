import tkinter as tk
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def linear_regression(window, stock, prediction_date):
        
    #Inspired from https://sumit-khedkar.medium.com/Stock Market Prediction Using Python: Article 1 ( The straight line )
    print("Linear regression ")
    newWindow = tk.Toplevel(window)
    
    # Linear Regression Model

    stock_local = stock.copy()
    prediction_date = pd.to_datetime(prediction_date)
    print(prediction_date)
    
    last_training_day = stock_local.index[-1]
    print(last_training_day)
    delta = prediction_date - last_training_day
    print(delta.days)
    
    
    # converting dates into number of days as dates cannot be passed directly to any regression model
    stock_local.index = (stock_local.index - pd.to_datetime('1970-01-01')).days
    
    # Reshape x (dates) in order to be 2 dimensional (rows, 1 column)
    #  x = dates
    x = np.asarray(stock_local.index)
    # y = prices
    y = np.asarray(stock_local['Adj Close'])


    # Fit the data -- train the linear regression model
    linear_regression = LinearRegression().fit(x.reshape(-1, 1), y.reshape(-1, 1))
    
    # Prediction for the historical dates
    y_learned = linear_regression.predict(x.reshape(-1, 1)) 
    
    # Score R^2
    R2 = r2_score(y.reshape(-1, 1), y_learned)
    R2 = str(round(R2, 2))
    
    # Score RMSE
    RMSE = (mean_squared_error(y.reshape(-1, 1), y_learned, squared = False))/1000
    RMSE = str(round(RMSE, 2))  
    
    # Now, add future dates to the date index and pass that index to the regression model for future prediction.
    # As we have converted date index into a range index, hence, here we just need to add 365 days -- 1 year
    # to the previous index. x[-1] gives the last value of the series.
    newindex = np.asarray(pd.RangeIndex(start=x[-1], stop=x[-1] + delta.days))
    
    # Prediction for the future dates
    y_predict = linear_regression.predict(newindex.reshape(-1, 1))
    #predicted_value = str(y_predict[-1])[1:-1]    
    predicted_value = float(str(y_predict[-1])[1:-1]) 
    predicted_value = str(round(predicted_value, 2))
    
    # convert the days index back to dates index for plotting the graph
    x_plot = pd.to_datetime(stock_local.index, origin='1970-01-01', unit='D')
    future_x = pd.to_datetime(newindex, origin='1970-01-01', unit='D')


    #Plotting the graph    
    plt.style.use('fivethirtyeight')
     
    figure = Figure(figsize=(7,6), dpi = 100)
    ax = figure.add_subplot(111)
    ax.plot(x_plot, stock['Adj Close'], label = 'Adjusted Close Price History')
    ax.plot(x_plot, y_learned, color='r', label = 'Linear Regression Model')
    ax.plot(future_x, y_predict, color='g', label = 'Future predictions with Linear Regression Model')
    figure.autofmt_xdate()
    figure.tight_layout() 
      
    canvas = FigureCanvasTkAgg(figure, master = newWindow)
    newWindow.title("Stock Market Predictions")
    ax.set_ylabel('Price')
    ax.set_xlabel('Date')
    plt.rcParams["font.size"] =7
    plt.subplots_adjust(bottom=0.15)
    canvas.get_tk_widget().grid(row = 0, column = 0, padx = 10)
    canvas.draw()

    return predicted_value, R2, RMSE
    