import tkinter as tk
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

# Polynomial regression
#Inspired from https://sumit-khedkar.medium.com/Stock Market Prediction Using Python: Article 2 ( ( Smart curves ) )
def polynomial_regression(window, stock, prediction_date, poly_degree):
    
    print("Polynomial regression ")
    
    newWindow = tk.Toplevel(window)
    
    stock_local = stock.copy()

    prediction_date = pd.to_datetime(prediction_date)

    last_training_day = stock_local.index[-1]
    print(last_training_day)
    delta = prediction_date - last_training_day
    print(delta.days)
        
     # function to calculate compound annual growth rate
    def CAGR(first, last, periods):
         return ((last/first)**(1/periods)-1) * 100
    
    # # Converting dates into number of days as dates cannot be passed directly 
    # # to any regression model
    stock_local.index = (stock_local.index - pd.to_datetime('1970-01-01')).days
    
    # Reshape x (dates) in order to be 2 dimensional (rows, 1 column)
    #  x = dates
    x = np.asarray(stock_local.index)
    # y = prices
    y = np.asarray(stock_local['Adj Close'])
    
    
    # Model initialization
    # by default the degree of the equation is 1.
    # Hence the mathematical model equation is y = mx + c, 
    # which is an equation of a line.
    regression_model = LinearRegression()
    
    # Choose the order of your polynomial. Here the degree is set to n.
    # hence the mathematical model equation is 
    # y = c0 + c1.x**1 + c2.x**2+....+ cn.x**n
    poly = PolynomialFeatures(poly_degree)
    
    # Convert dimension x in the higher degree polynomial expression
    X_transform = poly.fit_transform(x.reshape(-1, 1))
    
    # Fit the data (train the model)
    regression_model.fit(X_transform, y.reshape(-1, 1))
    
    # Prediction for historical dates. Let's call it learned values.
    y_learned = regression_model.predict(X_transform)
    
    # Score R^2
    R2 = r2_score(y.reshape(-1, 1), y_learned)
    R2 = str(round(R2, 2))
    
    # Score RMSE
    RMSE = (mean_squared_error(y.reshape(-1, 1), y_learned, squared = False))/1000
    RMSE = str(round(RMSE, 2))
    
    # Now, add future dates to the date index and pass that index to 
    # the regression model for future prediction.
    # As we have converted date index into a range index, hence, here we 
    # just need to add 3650 days ( roughly 10 yrs)
    # to the previous index. x[-1] gives the last value of the series.
    newindex = np.asarray(pd.RangeIndex(start=x[-1], stop=x[-1] + delta.days))
    
    # Convert the extended dimension x in the higher degree polynomial expression
    X_extended_transform = poly.fit_transform(newindex.reshape(-1, 1))
    
    # Prediction for future dates. Let's call it predicted values.
    y_predict = regression_model.predict(X_extended_transform)
    predicted_value = float(str(y_predict[-1])[1:-1]) 
    predicted_value = str(round(predicted_value, 2))
    
    # Convert the days index back to dates index for plotting the graph
    x = pd.to_datetime(stock_local.index, origin='1970-01-01', unit='D')
    future_x = pd.to_datetime(newindex, origin='1970-01-01', unit='D')
    
    cagr = CAGR(y[-1], y_predict[-1], delta.days/365.25)
    cagr = round(float(cagr),2)
    
    #Setting figure size
    
    figure = Figure(figsize=(7,6), dpi = 100)
    ax = figure.add_subplot(111)
    ax.plot(x, stock['Adj Close'], label = 'Adj Close Price History')
    ax.plot(x, y_learned, color='r', label = 'Polynomial Regression Model')
    ax.plot(future_x, y_predict, color='g', label = 'Future Predictions with Polynomial Regression Model')
    figure.autofmt_xdate()
    figure.tight_layout() 
      
    canvas = FigureCanvasTkAgg(figure, master = newWindow)
    newWindow.title("Stock Market Predictions")
    ax.set_ylabel('Price')
    ax.set_xlabel('Date')
    plt.suptitle('Stock Market Predictions -- Polynomial Regression with degree of {}'.format(poly_degree), fontsize=16)
    plt.rcParams["font.size"] =7
    plt.subplots_adjust(bottom=0.15)
    canvas.get_tk_widget().grid(row = 0, column = 0, padx = 10)
    canvas.draw()
    
    return predicted_value, R2, RMSE, cagr

