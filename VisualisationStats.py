import tkinter as tk
import customtkinter
from LinePlot import linePlot
from CandleStick import candlestick
from SMA import sma
from CMA import cma
from EMA import ema
from WMA import wma
from MACD import macd
from KDE import kde
from RISK import risk


class VisualisationStats(object):
    def __init__(self, parent):
        self.visualStat = tk.Toplevel(parent)
        self.visualStat.title("Visualisation")
        
        greet = customtkinter.CTkLabel(master=self.visualStat,text="VISUALIZATION MENU", text_font=('Calibri',14), width=350, bg_color="#2794CF", text_color="White")
        greet.grid(row=0,column=0, columnspan=3)
        
        blank = tk.Label(master=self.visualStat, text = "")
        blank.grid(row=1,column=0)



        visualizations_frame = tk.Frame(master = self.visualStat)
        visualizations_frame.grid(row=2, column = 0, padx = 10)
        
        stock_column = [
        "Open",
        "High",
        "Close",
        "Adj Close",
        "Total_Traded",
        "Daily_Return",
        "Cumulative_Return"
        ]
        
        self.plotOption = [
        "Line Plot",
        "Candle Stick"]
        
        self.MovingAvgOption = [
            "Standard Moving Average",
            "Cumulative Moving Average",
            "Exponential Moving Average",
            "Weighted Moving Average",
            "Moving Average Convergence/Divergence"
            ]

        
        lbl_candle_Stick = customtkinter.CTkLabel(master= visualizations_frame, text_font=('Calibri',13), width=300,text = "- Candle Stick Chart of the Stock")
        lbl_candle_Stick.grid(row=0, column=0)
        
        btn_candle_Stick = customtkinter.CTkButton(master = visualizations_frame, width=8, height=9, text_font=('Calibri',11), text = "Show", command = self.cStick)
        btn_candle_Stick.grid(row=0, column=2)
        
        
        
        blank2 = tk.Label(master=visualizations_frame, text = "")
        blank2.grid(row=1,column=0)
        blank3 = tk.Label(master=visualizations_frame, text = "")
        blank3.grid(row=2,column=0)

        #Creating the KDE option
        
        lbl_kde = customtkinter.CTkLabel(master= visualizations_frame, text_font=('Calibri',13), width=250, text = "- Kernel density estimation (KDE)")
        lbl_kde.grid(row=3, column=0)
        
        btn_kde = customtkinter.CTkButton(master = visualizations_frame, width=8, height=9, text_font=('Calibri',11), text = "Show",command = self.kde)
        btn_kde.grid(row=3, column=2)
        
        blank4 = tk.Label(master=visualizations_frame, text = "")
        blank4.grid(row=4,column=0)
        blank5 = tk.Label(master=visualizations_frame, text = "")
        blank5.grid(row=5,column=0)            
        
        lbl_declaration = customtkinter.CTkLabel(master= visualizations_frame, text_font=('Calibri',11), width=350, text = "For the below Plots, Specify Stock Column")
        lbl_declaration.grid(row=6, column=0)
        
        blank6 = tk.Label(master=visualizations_frame, text = "")
        blank6.grid(row=7,column=0)
        
        
        lbl_stock_column = customtkinter.CTkLabel(master= visualizations_frame, text_font=('Calibri',11), width=180, text = "Choose your stock column")
        lbl_stock_column.grid(row=8, column=0)
        
        
        # Dropdown about the stock column
        self.stock_column_variable = tk.StringVar(visualizations_frame)
        self.stock_column_variable.set(stock_column[0])
        self.stock_column_opt = tk.OptionMenu(visualizations_frame, self.stock_column_variable, *stock_column)
        self.stock_column_opt.config(width=10, font=('Calibri', 11))
        self.stock_column_opt.grid(row=8, column = 1, padx = 10)
        
        #button to submit the selected column
        stock_column = customtkinter.CTkButton(master = visualizations_frame, width=8, height=9, text_font=('Calibri',11), text = "Submit Column name",command = self.submitColumn)
        stock_column.grid(row=8, column=2)
        
        self.stock_Column_result = tk.Label(master = visualizations_frame, text = "")
        self.stock_Column_result.grid(row=9, column=1)
        
        blank7 = tk.Label(master=visualizations_frame, text = "")
        blank7.grid(row=10,column=0)
        blank8 = tk.Label(master=visualizations_frame, text = "")
        blank8.grid(row=11,column=0)
        

        lbl_line_plot = customtkinter.CTkLabel(master= visualizations_frame, text_font=('Calibri',13), width=250, text = "- Line Plot of the Stock")
        lbl_line_plot.grid(row=12, column=0)
        
        
        btn_line_plot = customtkinter.CTkButton(master = visualizations_frame, width=8, height=9, text_font=('Calibri',11), text = "Show", command = self.lPlot)
        btn_line_plot.grid(row=12, column=2)
        
        blank9 = tk.Label(master=visualizations_frame, text = "")
        blank9.grid(row=13,column=0)
        blank10 = tk.Label(master=visualizations_frame, text = "")
        blank10.grid(row=14,column=0)    
        
        
        lbl_MovingAverage = customtkinter.CTkLabel(master= visualizations_frame, text_font=('Calibri',13), width=250, text = "- Moving Average Graphs")
        lbl_MovingAverage.grid(row=15, column=0)
        
        # lbl_stock_column = tk.Label(master = visualizations_frame, text = "Choose your Visualisation from below options:")
        # lbl_stock_column.grid(row=2, column=0)
        
        
        #Dropdown to choose plot options
        # self.plotOption_variable = tk.StringVar(visualizations_frame)
        # self.plotOption_variable.set("select") # default value
        # lbl_visual_option1 = tk.Label(master = visualizations_frame, text = "1. Choose the type of graph to plot")
        # lbl_visual_option1.grid(row=3, column=0)
        # lbl_plotOption = tk.OptionMenu(visualizations_frame, self.plotOption_variable, *self.plotOption)
        # lbl_plotOption.grid(row=3, column=1)
        # bt_plotOption = tk.Button(master = visualizations_frame, text = "Show",command = self.submitOption)
        # bt_plotOption.grid(row=3, column=2)
        
        #Creating text box to enter moving average window              
        
        lbl_ma_Window = customtkinter.CTkLabel(master= visualizations_frame, text_font=('Calibri',11), width=350, text = "Enter Moving Average window (Days):")
        lbl_ma_Window.grid(row=16, column=0)
        
    
        self.ma_Window_variable = customtkinter.CTkEntry(master=visualizations_frame, width=70, height=20, fg_color="#A9ADAF")
        self.ma_Window_variable.grid(row=16, column=1)
        btn_ma_Window = customtkinter.CTkButton(master = visualizations_frame, width=8, height=9, text_font=('Calibri',11), text = "Enter ",command = self.submitSmaWindow)
        btn_ma_Window.grid(row=16, column=2)
        self.ma_Window_result = tk.Label(master = visualizations_frame, text = "")
        self.ma_Window_result.grid(row=17, column=1)
       
        
        lbl_visual_option = customtkinter.CTkLabel(master= visualizations_frame, text_font=('Calibri',11), width=250, text = "Choose the type of Moving Average:")
        lbl_visual_option.grid(row=18, column=0)
        #Creating dropdown to choose Moving Average options
        self.maOption_variable = tk.StringVar(visualizations_frame)
        self.maOption_variable.set("select") # default value
        
        lbl_maOption = tk.OptionMenu(visualizations_frame, self.maOption_variable, *self.MovingAvgOption)
        lbl_maOption.grid(row=18, column=1)
        bt_maOption = customtkinter.CTkButton(master = visualizations_frame, width=8, height=9, text_font=('Calibri',11), text = "Show",command = self.submitMAOption)
        bt_maOption.grid(row=18, column=2)
       
        
        blank11 = tk.Label(master=visualizations_frame, text = "")
        blank11.grid(row=19,column=0)
        blank12 = tk.Label(master=visualizations_frame, text = "")
        blank12.grid(row=20,column=0)    
    
       
        
        #creating the Stock Risk option
        lbl_risk = customtkinter.CTkLabel(master= visualizations_frame, text_font=('Calibri',13), width=100, text = "- Stock Risk")
        lbl_risk.grid(row=21, column=0)
        
        btn_risk = customtkinter.CTkButton(master = visualizations_frame, width=8, height=9, text_font=('Calibri',11), text = "Show",command = self.risk)
        btn_risk.grid(row=21, column=2)
       
        
        blank13 = tk.Label(master=visualizations_frame, text = "")
        blank13.grid(row=22,column=0)  
        
        #Creating button to quit the Visualisation menu
        btn_quitVisual = customtkinter.CTkButton(text = "Quit", master=visualizations_frame, width=9, height=9, hover_color='pink' , fg_color="red",  text_font=('Calibri',11), command=self.quitDesc)
        btn_quitVisual.grid(row = 23, column=0, columnspan=3)
        
        blank14 = tk.Label(master=visualizations_frame, text = "")
        blank14.grid(row=24,column=0)  
        
    #Function to capture the column selected
    def submitColumn(self):
        
        self.columnName = self.stock_column_variable.get()
        self.stock_Column_result["text"] = f"{self.columnName}"
    
    #Function to capture the plotOption selected
    def submitOption(self):
        
        self.plotOptionSelect = self.plotOption_variable.get()
        self.stock_Column_result["text"] = f"{self.plotOptionSelect}"  
        
        #logic to show the Line plot or CandleStick graph
        if self.plotOptionSelect == self.plotOption[0]:
            self.line_plot()
        
    # def cStick(self):
    #         self.candlestick()
    
    #Function to capture the Moving Average option selected
    def submitMAOption(self):
        
        self.maOptionSelect = self.maOption_variable.get()
        
        #logic to call the respective moving average function selected 
        if self.maOptionSelect == self.MovingAvgOption[0]:
            self.sma()
        elif self.maOptionSelect == self.MovingAvgOption[1]:
            self.cma()
        elif self.maOptionSelect == self.MovingAvgOption[2]:
            self.ema()
        elif self.maOptionSelect == self.MovingAvgOption[3]:
            self.wma()
        else:
            self.macd()
        
    #Function to capture the Moving average window entered
    def submitSmaWindow(self):
        
        self.maWindow = self.ma_Window_variable.get()
        print(type(self.maWindow))
        if self.maWindow.isdigit(): 
            self.ma_Window_result["text"] = f"{self.maWindow}"
            self.ma_Window_result.configure(fg ="black")
            self.maWindow = int(self.maWindow)
        else:
            self.ma_Window_result["text"] = "Only integer numbers are allowed, please try again"
            self.ma_Window_result.configure(fg ="red")

    
    def lPlot(self):
        #Funciton call to line Plot graph
        linePlot(self.visualStat, self.passedStock, self.columnName)      
    
    
    def cStick(self):
        #Funciton call to candle stick graph
        candlestick(self.visualStat, self.passedStock)

    def sma(self):
        #Funciton call to Simple Moving Average graph
        sma(self.visualStat, self.passedStock, self.columnName, self.maWindow)
        
    def cma(self):
        #Funciton call to Cummulative Moving Average graph
        cma(self.visualStat, self.passedStock, self.columnName, self.maWindow)
    
    def ema(self):
        #Funciton call to Exponential Moving Average graph
        ema(self.visualStat, self.passedStock, self.columnName, self.maWindow)
   
    def wma(self):
        #Funciton call to Weighted Moving Average graph
        wma(self.visualStat, self.passedStock, self.columnName, self.maWindow)
   
    def macd(self):
        #Funciton call to Moving Average Convergence/Divergence graph
        macd(self.visualStat, self.passedStock, self.columnName)
   
    def kde(self):
        #Funciton call to Kernel density estimation graph
        kde(self.visualStat, self.passedStock)
        
    def risk(self):
        #Funciton call to risk graph
        risk(self.visualStat, self.passedStock, self.columnName)
   
    
    
   
    def openVisual(self, stock):
        
        #storing passed values to use in VisualisationStats class
        self.passedStock = stock
        
    #function to close the Visualisation Stats window when we click on quit
    def quitDesc(self):
        
        self.visualStat.destroy()
