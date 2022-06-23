import tkinter as tk
import yfinance as yf
import tkcalendar as tkcal
import customtkinter
from datetime import datetime

class DataEntry(object):
    def __init__(self, parent):
        self.dataEntry = tk.Toplevel(parent)
        self.dataEntry.title("Data Entry")
        
        stock_frame = tk.Frame(master = self.dataEntry)
        stock_frame.grid(row=0, column = 0, padx = 10)
        self.stock_entry = customtkinter.CTkEntry(master=stock_frame, width=70, height=20, fg_color="#A9ADAF")
        #self.stock_entry = tk.Entry(stock_frame, width = 10)
        self.stock_entry.grid(row=0, column=0)
        
        # Create the Submit Button of stock name
        btn_submit_stock = customtkinter.CTkButton(master = stock_frame, width=8, height=9, text_font=('Calibri',11), text = "Submit stock name", command = self.submit_stock)
        # Create the Label that show the stock you choose    
        self.stock_name_result = customtkinter.CTkLabel(master= stock_frame, text_font=('Calibri',11), width=100, text = "")
        btn_submit_stock.grid(row=1, column=0, padx = 10, pady = 10)
        self.stock_name_result.grid(row=2, column=0, pady = 5, padx=10)
                
        cal_frame = tk.Frame(master = self.dataEntry)
        cal_frame.grid(row=0, column=1, pady = 5, padx=10)
        
        self.start_cal = tkcal.Calendar(master = cal_frame, setme = 'day', date_pattern = "y-mm-dd", foreground="black")
        self.end_cal = tkcal.Calendar(master = cal_frame, setme = 'day', date_pattern = "y-mm-dd", foreground="black")
    
        # Layout of the inside of cal_frame using grid
        self.start_cal.grid(row=0, column=0, padx = 20)
        self.end_cal.grid(row=0, column=1, padx = 20)
        
        
        # Create the Submit Button of start_cal
        btn_start_cal = customtkinter.CTkButton(master = cal_frame, width=8, height=9, text_font=('Calibri',11), text = "Submit start date", command = self.select_start_date)
        btn_start_cal.grid(row=1, column = 0, padx = 10, pady = 10)
        
        # Create the Submit Button of end_cal
        btn_end_cal = customtkinter.CTkButton(master = cal_frame, width=8, height=9, text_font=('Calibri',11), text = "Submit end date", command = self.select_end_date)
        btn_end_cal.grid(row=1, column = 1, padx = 10, pady = 10)
        
        # Create the Label that show the stock you choose    
        self.start_time_result = customtkinter.CTkLabel(master= cal_frame, text_font=('Calibri',11), width=100, text = "")
        self.start_time_result.grid(row=2, column=0, pady = 5, padx=10)
        
        self.end_time_result = customtkinter.CTkLabel(master= cal_frame, text_font=('Calibri',11), width=100, text = "")
        self.end_time_result.grid(row=2, column=1, pady = 5, padx=10)
        
        # Create the Input Data name frame with an Entry widget and label in it
        input_data_frame = tk.Frame(master = self.dataEntry )
        input_data_frame.grid(row=2, column=0)
        
        # Create the Label that show the result of stock you chose
        self.message_result = customtkinter.CTkLabel(master= input_data_frame, text_font=('Calibri',11), width=360, text = "")
        self.message_result.grid(row=1, column=0, pady = 5, padx=10)

        # Create the Submit Button of input data
        btn_submit_input_data = customtkinter.CTkButton(master = input_data_frame, width=8, height=9, text_font=('Calibri',12), text = "Submit input data", command = self.submit)
        btn_submit_input_data.grid(row=0, column=0, padx = 10, pady = 10)
        
    
   
    def submit_stock(self):
        self.stockName = self.stock_entry.get()

        self.stock_name_result.set_text(self.stockName)
#        print(self.stock_name_result["text"])
    def select_start_date(self):
        self.date = self.start_cal.get_date()
        self.start_time_result.set_text(self.date)
        #self.start_time_result["text"] = f"{self.date}"
        #print(self.start_time_result["text"])
    def select_end_date(self):
        self.date = self.end_cal.get_date()
        self.end_time_result.set_text(self.date)

    
   
    def submit(self):
        
        self.stockCode = self.stock_entry.get()
        self.startDate = self.start_cal.get_date()
        self.endDate = self.end_cal.get_date()
        self.stock = yf.download(self.stockCode, self.startDate, self.endDate)
     
        if self.stock.empty:
            if len(self.stockCode) > 5 or len(self.stockCode) < 3:
                result = "Stock code should have 3 - 5 letters, please try again"
            elif self.endDate > str(datetime.today()):
                result = "For the time period you selected, there is no available data, please try again"
            elif self.startDate > self.endDate:
                 result = "Start date cannot be after end date, please try again"           
            else:
                result = "The stock data does not exist"
            self.message_result.set_text(result)
            self.message_result.configure(text_color ="red")
        else:
            result = "Success"
            self.message_result.set_text(result)
            self.message_result.configure(text_color="green")
            self.preprocess()
            self.dataEntry.destroy()
            #print("result is: ", result, "and stock is: ", self.stock)
        print("result is: ", result)
         
        #if (self.message_result.set_text(result) == "Success"):
        #     self.succ_msg = "Success"
        #     #self.message_result["text"] = self.succ_msg
        #     self.message_result.set_text(self.succ_msg)
        #     self.message_result.configure(fg_color="green")
        #     #return result
            
    def preprocess(self):
        
        # Calculating some extra values that a user might be interested in - Preprocessing       
        # Total Traded attribut as a column
        self.stock["Total_Traded"] = self.stock["Open"] * self.stock["Volume"]
        
        # Daily percentage change for Adj Close
        self.stock["Daily_Return"] = (self.stock['Adj Close']/self.stock['Adj Close'].shift(1)) - 1
        
        
        # Cumulative percentage change for Adj Close
        self.stock["Cumulative_Return"] = (1 + self.stock["Daily_Return"]).cumprod()
    


    def returnValue(self):
         #self.dataEntry.deiconify()
         self.dataEntry.wait_window()
         value = [self.stockCode, self.startDate, self.endDate]
         return value, self.stock
    
#deiconify(): Displays the window, after using either the iconify or the withdraw methods.
#wait_window(): method ideally waits for an event to happen and executes the event of the main window
        
     