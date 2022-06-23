import tkinter as tk
import customtkinter
import tkcalendar as tkcal
import pandas as pd
import numpy as np
from LinearRegression import linear_regression
from PolyRegression import polynomial_regression
from ProphetAlgo import prophet
from datetime import datetime

class PredictiveStats(object):
    def __init__(self, parent):
        self.predictStat = tk.Toplevel(parent)
        self.predictStat.title("Predictive Analytics")

        
        greet = customtkinter.CTkLabel(master=self.predictStat,text="PREDICTIVE STATS MENU", text_font=('Calibri',14), width=350, bg_color="#2794CF", text_color="White")
        greet.grid(row=0,column=0, columnspan=3)
        
        blank = tk.Label(master=self.predictStat, text = "")
        blank.grid(row=1,column=0)

         # Create the Predictive frame with an Entry widget and label in it
        self.predictive_frame = tk.Frame(master = self.predictStat)
        self.predictive_frame.grid(row=1, column = 0, padx = 10)
            
        #Creating calendar to select the prediction date
        lbl_Menu = customtkinter.CTkLabel(master= self.predictive_frame, text_font=('Calibri',11), width=250, text = "Choose prediction Date:")
        lbl_Menu.grid(row=2, column = 0)
        
        self.calDate = tkcal.Calendar(master = self.predictive_frame, setme = 'day', date_pattern = "y-mm-dd", foreground="black")
        self.calDate.grid(row=3,column=0)
        btn_calDate = customtkinter.CTkButton(master = self.predictive_frame, width=8, height=9, text_font=('Calibri',11), text = "Submit", command =self.select_date)
        btn_calDate.grid(row=4, column = 0, padx = 10, pady = 10)
        self.date_result = customtkinter.CTkLabel(master= self.predictive_frame, text_font=('Calibri',11), width=400, text = "")
        self.date_result.grid(row=5, column=0)
        
        #blank1 = tk.Label(master=self.predictive_frame, text = "")
        #blank1.grid(row=5,column=0)
        blank2 = tk.Label(master=self.predictive_frame, text = "")
        blank2.grid(row=6,column=0)

        
        #Creating options to choose the Predection models
        self.DateLabel = customtkinter.CTkLabel(master= self.predictive_frame, text_font=('Calibri',13), width=200, text = " Chose a prediction Model:")
        self.DateLabel.grid(row=7,column=0)
        
        blank3 = tk.Label(master=self.predictive_frame, text = "")
        blank3.grid(row=8,column=0)
        
       #Linear Regression Model Option
        lbl_Option1 = customtkinter.CTkLabel(master= self.predictive_frame, text_font=('Calibri',11), width=250, text = "Linear Regression Model")
        lbl_Option1.grid(row=9, column = 0)
               
        #button to call the linear_reg function
        btn_show = customtkinter.CTkButton(master = self.predictive_frame, width=8, height=9, text_font=('Calibri',11), text = "Show", command =self.linear_reg)
        btn_show.grid(row = 9, column=1, pady = 5, padx=10)
        
        blank4 = tk.Label(master=self.predictive_frame, text = "")
        blank4.grid(row=10,column=0)
        
        
        #fbProphet Prediction Model Option        
        lbl_Option3 = customtkinter.CTkLabel(master= self.predictive_frame, text_font=('Calibri',11), width=250, text = "Prophet Model")
        lbl_Option3.grid(row=11, column = 0)
        
        #button to call the prophet function
        btn_show = customtkinter.CTkButton(master = self.predictive_frame, width=8, height=9, text_font=('Calibri',11), text = "Show", command =self.prophet)
        btn_show.grid(row = 11, column=1, pady = 5, padx=10)
        
        blank5 = tk.Label(master=self.predictive_frame, text = "")
        blank5.grid(row=12,column=0)
        
        
        #Polynomial Regression Model Option
        #Creating text box to enter degree for polynomial regression model
        lbl_degree = customtkinter.CTkLabel(master= self.predictive_frame, text_font=('Calibri',11), width=350, text = "Enter Degree for the polynomial model ")
        lbl_degree.grid(row=13, column=0)
        self.degree_variable = customtkinter.CTkEntry(master=self.predictive_frame, width=70, height=20, fg_color="#A9ADAF")
        self.degree_variable.grid(row=13, column=1)
        btn_degree = customtkinter.CTkButton(master = self.predictive_frame, width=8, height=9, text_font=('Calibri',11), text = "Enter", command =self.submitDegree)
        btn_degree.grid(row=13, column=2)
        self.degree_result = tk.Label(master = self.predictive_frame, text = "")
        self.degree_result.grid(row=14, column=1)
       
        
        lbl_Option2 = customtkinter.CTkLabel(master= self.predictive_frame, text_font=('Calibri',11), width=250, text = "Polynomial Regression Model")
        lbl_Option2.grid(row=15, column = 0)
        
        #button to call the poly_reg function
        btn_show = customtkinter.CTkButton(master = self.predictive_frame, width=8, height=9, text_font=('Calibri',11), text = "Show", command =self.poly_reg)
        btn_show.grid(row = 15, column=1, pady = 5, padx=10)
        
        
        
        self.predicted_value_result= customtkinter.CTkLabel(master= self.predictive_frame, text_font=('Calibri',11), width=250, text = "")
        self.predicted_value_result.grid(row=11, column = 3)
        self.R2_result= customtkinter.CTkLabel(master= self.predictive_frame, text_font=('Calibri',11), width=250, text = "")
        self.R2_result.grid(row=12, column = 3)
        self.RMSE_result= customtkinter.CTkLabel(master= self.predictive_frame, text_font=('Calibri',11), width=250, text = "")
        self.RMSE_result.grid(row=13, column = 3)
        
        # lbl_Option4 = tk.Label(master = self.predictive_frame, text = "ARIMA Model")
        # lbl_Option4.grid(row=9, column = 0)
        
        # btn_show = tk.Button(master = self.predictive_frame, text = "Show", command = self.poly_reg)
        # btn_show.grid(row = 9, column=1, pady = 5, padx=10)
        
        blank6 = tk.Label(master=self.predictive_frame, text = "")
        blank6.grid(row=16,column=0) 
        
        #Button to call quit function
        btn_quitDesc = customtkinter.CTkButton(text = "Quit", master=self.predictive_frame, width=9, height=9, hover_color='pink' , fg_color="red",  text_font=('Calibri',11), command=self.quitDesc)
        btn_quitDesc.grid(row = 17, column=0, columnspan=3)

        # self.bg_image= ImageTk.PhotoImage(Image.open("C:/UCD_BA/Programming/PythonScripts/Diff.png"))
        # self.bg_label=tk.Label(image=self.bg_image)
        # self.bg_label.grid(row=10,column=0, columnspan=3)
    
    #function to capture the selected date
    def select_date(self):
        self.date = self.calDate.get_date()
        if self.date < str(datetime.today()):          
            self.date_result.set_text("Prediction date should be future date, please try again")
        else:
            self.date_result.set_text(self.date)
        #print(self.date)
        
        #code to calculate variables for regression models
        
        # prediction_date = pd.to_datetime(self.date)
  
        # last_training_day = self.passedStock.index[-1]
        # print(last_training_day)

        # self.delta = prediction_date - last_training_day
        # self.delta_value = self.delta.days
        
        # self.passedStock.index = (self.passedStock.index - pd.to_datetime('1970-01-01')).days

        # # Reshape x (dates) in order to be 2 dimensional (rows, 1 column)
        # #  x = dates
        # self.x = np.asarray(self.passedStock.index)
        # # y = prices
        # self.y = np.asarray(self.passedStock['Adj Close'])
        # #return self.delta.days, self.x, self.y

    #function to capture the entered degree for polynomial    
    def submitDegree(self):
        
        
        self.degree = self.degree_variable.get()
        if self.degree.isdigit(): 
            self.degree = int(self.degree_variable.get())
            self.degree_result["text"] = f"{self.degree}" 
            self.degree_result.configure(fg ="black")
        else:
            self.degree_result["text"] = "Only integer numbers are allowed, please try again"
            self.degree_result.configure(fg ="red")
        
    
    #function to call linear_regression function
    def linear_reg(self):
        
        #calling linear_regression function and storing the returned values
        self.predicted_value, self.R2, self.RMSE = linear_regression(self.predictStat, self.passedStock, self.date)
        
        #Printing the result values on the screen
        self.predicted_value_result.set_text("Predicted Value is: %s" % self.predicted_value)
        self.R2_result.set_text("R2 Value is: %s" % self.R2)
        self.RMSE_result.set_text("RMSE Value is: %s" % self.RMSE)
        
    #function to call polynomial_regression function
    def poly_reg(self):
        
        #calling polynomial_regression function and storing the returned values
        self.predicted_value, self.R2, self.RMSE, self.CAGR = polynomial_regression(self.predictStat, self.passedStock, self.date, self.degree)
        
        #Printing the result values on the screen
        self.predicted_value_result.set_text("Predicted Value is: %s" % self.predicted_value)
        self.R2_result.set_text("R2 Value is: %s" % self.R2)
        self.RMSE_result.set_text("RMSE Value is: %s" % self.RMSE)
        
    #function to call polynomial_regression function    
    def prophet(self):
        
        #calling prophet function and storing the returned values
        self.predicted_value = prophet(self.predictStat, self.passedStock, self.date)
        
        #Printing the result values on the screen
        self.predicted_value_result.set_text("Predicted Value is: %s" % self.predicted_value)
        self.R2_result.set_text("")
        self.RMSE_result.set_text("")
        
    
    def open_window(self, stock):
        
        #storing passed values to use in PredictiveStats class
        self.passedStock = stock
    #    self.linear_regression()
    
    #function to close the Predictive Stats window when we click on quit
    def quitDesc(self):
        self.predictStat.destroy()

###########################################################################        

