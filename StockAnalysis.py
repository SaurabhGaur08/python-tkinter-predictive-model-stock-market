import tkinter as tk
import pandas as pd
import yfinance as yf
from tkinter import *
from tkinter.ttk import Label
from PIL import ImageTk, Image
from DescriptiveStats import DescriptiveStats
from DataEntry import DataEntry
from VisualisationStats import VisualisationStats
from PredictiveStats import PredictiveStats
import warnings
import customtkinter

warnings.filterwarnings("ignore")

class StockAnalysis(tk.Frame):
    def __init__(self, master):
        
        tk.Frame.__init__(self, master)
        # Set window title
        master.title("Stock Analysis")
        greet = customtkinter.CTkLabel(master=master,text="Welcome to the Stock Analysis Application", text_font=('Calibri',14), width=350, bg_color="#2794CF", text_color="White")
        greet.grid(row=0,column=0, columnspan=3)
        line = tk.Label(master, text = "")
        line.grid(row=1,column=0)


        
        option1 =customtkinter.CTkLabel(master=master, text_font=('Calibri',11), width=270, text="Specify the Details of the stock")
        option1.grid(row=2,column=0)
        button = customtkinter.CTkButton(text = "Enter", master=master, width=9, height=9, text_font=('Calibri',11),command=self.showDetails )
        button.grid(row=2,column=1)
        
        
        blank = tk.Label(master, text = "")
        blank.grid(row=7,column=0)


        #Create Menu options
        question =customtkinter.CTkLabel(master,text="Choose the preferred analysis", text_font=('Calibri',11), width=270, )
        question.grid(row=8,column=0)

        
        
        option2 = customtkinter.CTkLabel(master,text="Descriptive Statistics", text_font=('Calibri',11), width=150 )
        option2.grid(row=9,column=0)
        master.rowconfigure(9, minsize=30)

        #call descStats function
        buttonShow = customtkinter.CTkButton(text = "Show", master=master, width=9, height=9, text_font=('Calibri',11),command=self.descStats )
        buttonShow.grid(row=9,column=1)
        
        
        option3 = customtkinter.CTkLabel(master,text="Descriptive Visualisations", text_font=('Calibri',11), width=160 )
        option3.grid(row=10,column=0)
        master.rowconfigure(10, minsize=30)
        #call descStats function
        buttonShow2 = customtkinter.CTkButton(text = "Show", master=master, width=9, height=9, text_font=('Calibri',11),command=self.visualStats )
        buttonShow2.grid(row=10,column=1)

        option4 = tk.Label(master, text = "Predictive Analysis")
        option4 = customtkinter.CTkLabel(master,text="Predictive Analysis", text_font=('Calibri',11), width=160 )
        option4.grid(row=11,column=0)
        master.rowconfigure(11, minsize=30)
        #call descStats function
        buttonShow4 = customtkinter.CTkButton(text = "Show", master=master, width=9, height=9, text_font=('Calibri',11),command=self.predictStats )
        buttonShow4.grid(row=11,column=1)


        qbutton = customtkinter.CTkButton(text = "Quit", master=master, width=9, height=9, hover_color='pink' , fg_color="red",  text_font=('Calibri',11), command=self.quit)
        qbutton.grid(row=12,column=0, columnspan=3)

        #add image to the window
        self.bg_image= ImageTk.PhotoImage(Image.open("BG_Image.png"))
        self.bg_label=tk.Label(image=self.bg_image)
        self.bg_label.grid(row=13,column=0, columnspan=3)
    

        #function to show the returned values after searching the stock
    def showDetails(self):
        
        
        InqDetails, self.stockData = DataEntry(self).returnValue()
        
        resultOutput4 = customtkinter.CTkLabel(text="****STOCK INQUIRY:SUCCESS****", text_font=('Calibri',11), width=260 )
        resultOutput4.grid(row=3,column=0, columnspan=2)
        resultOutput1 = tk.Label(text="\t\t Stock Code: %s" % InqDetails[0])
        resultOutput1 = customtkinter.CTkLabel(text="\t\t Stock Code: %s" % InqDetails[0], text_font=('Calibri',11), width=260 )
        resultOutput1.grid(row=4,column=0)
        #resultOutput2 = tk.Label(text="\t\t Start Date: %s" % InqDetails[1])
        resultOutput2 = customtkinter.CTkLabel(text="\t\t Start Date: %s" % InqDetails[1], text_font=('Calibri',11), width=260 )
        resultOutput2.grid(row=5,column=0)
        #resultOutput3 = tk.Label(text="\t\t End Date: %s" % InqDetails[2])
        resultOutput3 = customtkinter.CTkLabel(text="\t\t End Date: %s" % InqDetails[2], text_font=('Calibri',11), width=260 )
        resultOutput3.grid(row=6,column=0)
    
       
        #Function for Descriptive Statistics
    def descStats(self):
        
        
        #Calculating some extra values that a user might be interested in        
        # Total Traded attribut as a column
        self.stockData["Total_Traded"] = self.stockData["Open"] * self.stockData["Volume"]
        
        # Daily percentage change for Adj Close
        self.stockData["Daily_Return"] = (self.stockData['Adj Close']/self.stockData['Adj Close'].shift(1)) - 1
        
        
        # Cumulative percentage change for Adj Close
        self.stockData["Cumulative_Return"] = (1 + self.stockData["Daily_Return"]).cumprod()
        
        descriptiveData = self.stockData.describe()
        
        #Calling the open_window function of DescriptiveStats class
        DescriptiveStats(self).open_window(descriptiveData, self.stockData)
        
        #Function for Visualisation 
    def visualStats(self):
        
        #Calling the open_window function of VisualisationStats class
        VisualisationStats(self).openVisual(self.stockData)
    
        #Function for Predictive Statistics
    def predictStats(self):
        
        #Calling the open_window function of PredictiveStats class
        PredictiveStats(self).open_window(self.stockData)
        
        #function to close the window when we click on quit
    def quit(self):
        self.master.destroy()


        
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x500") # Force a specific geometry
    data = StockAnalysis(root)  
    root.mainloop()