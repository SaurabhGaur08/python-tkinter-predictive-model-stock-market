import tkinter as tk
from sklearn.metrics import mean_squared_error
import pandas as pd
from matplotlib import pyplot as plt
from fbprophet import Prophet
from sklearn.metrics import r2_score
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

#Prophet Prediction Algorithm
#Inspired from https://sumit-khedkar.medium.com/Stock Market Prediction Using Python: Article 3 ( The Prophet )

def prophet(window, stock, prediction_date):

    newWindow = tk.Toplevel(window)
    
    
    # function to calculate compound annual growth rate
    def CAGR(first, last, periods):
        return ((last/first)**(1/periods)-1) * 100

    # preparing data. Prophet only understands y and ds columns. Hence we need to rename
    # our data frame columns
    
    # Prophet algorithm
    
    print(stock)
    stock_local = stock.copy()
    
    prediction_date = pd.to_datetime(prediction_date)

    last_training_day = stock_local.index[-1]
    print(last_training_day)
    delta = prediction_date - last_training_day
    print(delta.days)
    stock_local = stock_local.reset_index()
    stock_local.drop(['Open', 'High', 'Low', 'Close', 'Volume'], axis = 1, inplace = True) 

   
    stock_local.rename(columns={'Adj Close': 'y', 'Date': 'ds'}, inplace=True)
    
    # Model initialization. Create an object of class Prophet.
    model = Prophet()
    
    # Fit the data(train the model)
    model.fit(stock_local)
    
    # Create a data frame of the future dates until the prediction_date
    future = model.make_future_dataframe(periods = delta.days)
    
    # Prediction for future dates.
    forecast = model.predict(future)
    
    # forecast has number of various columns. In this exercise we are considering only two of them.
    # ds is a date column and yhat is the median predicated value.
    forecast_valid = forecast[['ds','yhat']][:]
    forecast_valid.rename(columns = {'yhat': 'y'}, inplace = True)
    
    predicted_value = str(forecast_valid.iloc[-1]['y'])
    
    
    
    # create a date index for input data frame.
    stock_local['Date'] = pd.to_datetime(stock_local.ds)
    stock_local.index = stock_local['Date']
    
    # Create a date index for forecast data frame.
    forecast_valid['Date'] = pd.to_datetime(forecast_valid.ds)
    forecast_valid.index = forecast_valid['Date']
    
    
    #Plotting the graph
    figure = Figure(figsize=(7,6), dpi = 100)
    ax = figure.add_subplot(111)
    ax.plot(stock_local['y'], label = 'Adj Close Price History')
    ax.plot(forecast_valid[['y']], label = 'Prophet Model', color='r')
    ax.plot(forecast_valid[['y']].tail(delta.days), label = 'Future Predictions using Prophet Algorithm', color='g')
    figure.autofmt_xdate()
    
      
    canvas = FigureCanvasTkAgg(figure, master = newWindow)
    newWindow.title("Stock Market Predictions")
    ax.set_ylabel('Price')
    ax.set_xlabel('Date')
    plt.rcParams["font.size"] =7
    plt.suptitle('"Stock Market Predictions -- Prophet Alogorithm')
    plt.subplots_adjust(bottom=0.15)
    canvas.get_tk_widget().grid(row = 0, column = 0, padx = 10)
    canvas.draw()
    
    
    return predicted_value
    