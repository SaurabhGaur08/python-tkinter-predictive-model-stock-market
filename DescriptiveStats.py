import tkinter as tk
import customtkinter


class DescriptiveStats(object):
    def __init__(self, parent):
        self.descStat = tk.Toplevel(parent)
        self.descStat.title("Descriptive Analytics")

        #greet = tk.Label(self.descStat, text = "DESCRIPTIVE STATS MENU", bg="Blue", fg ="White", font=("Arial",10, 'bold'))
        greet = customtkinter.CTkLabel(master=self.descStat,text="DESCRIPTIVE STATS MENU", text_font=('Calibri',14), width=350, bg_color="#2794CF", text_color="White")
        greet.grid(row=0,column=0, columnspan=3)

        blank = tk.Label(master=self.descStat, text = "")
        blank.grid(row=1,column=0)
        print("Inside Descriptive")
        
        descriptiveMetric = [
        "count",
        "mean",
        "std",
        "min",
        "25%",
        "50%",
        "75%",
        "max"
        ] 
    
    
        stock_column = [
        "Open",
        "High",
        "Close",
        "Adj Close",
        "Total_Traded",
        "Daily_Return",
        "Cumulative_Return"
        ]
        
    
         # Create the descriptive frame with an Entry widget and label in it
        descriptive_frame = tk.Frame(master = self.descStat)
        
        # Dropdown about the descriptive metric
        self.descriptiveMetric_variable = tk.StringVar(descriptive_frame)
        self.descriptiveMetric_variable.set(descriptiveMetric[0])
        
        descriptiveMetric_opt = tk.OptionMenu(descriptive_frame, self.descriptiveMetric_variable, *descriptiveMetric)
        descriptiveMetric_opt.config(width=10, font=('Calibri', 12))
                
        lbl_descriptiveMetric = customtkinter.CTkLabel(master=descriptive_frame, text_font=('Calibri',11), width=270, text = "Choose your desciptive metric")
        
        # Dropdown about the stock column       
        self.stock_column_variable = tk.StringVar(descriptive_frame)
        self.stock_column_variable.set(stock_column[0])
        
        stock_column_opt = tk.OptionMenu(descriptive_frame, self.stock_column_variable, *stock_column)
        stock_column_opt.config(width=10, font=('Calibri', 12))
        
        lbl_stock_column = customtkinter.CTkLabel(master=descriptive_frame, text_font=('Calibri',11), width=270, text = "Choose your stock column")
        
        # Create the Find Button to call descriptive_statistics function to calculate the descriptive stats 
        btn_find = customtkinter.CTkButton(master = descriptive_frame, width=8, height=9, text_font=('Calibri',11), text = "Find", command = self.descriptive_statistics)
        
        btn_quitDesc = customtkinter.CTkButton(master = descriptive_frame, width=8, height=9, text_font=('Calibri',11), hover_color='pink' , fg_color="red",  text = "Quit",  command = self.quitDesc)
        
        # Create the Label that show the stock you chose
        self.descriptive_result = tk.Label(master = descriptive_frame, text = "")
    
    
        # Set-up the layout of the whole screen using grid
        
        descriptive_frame.grid(row=3, column = 0, padx = 10)
        lbl_descriptiveMetric.grid(row=0, column=0, pady = 5, padx=10)
        descriptiveMetric_opt.grid(row=0, column = 1, padx = 10)
    
        lbl_stock_column.grid(row=1, column=0, pady = 5, padx=10)
        stock_column_opt.grid(row=1, column = 1, padx = 10)
        
        btn_find.grid(row=1, column=2, pady = 5, padx=10)
        self.descriptive_result.grid(row=2, column=1, pady = 5, padx=10)
    
        btn_quitDesc.grid(row = 2, column=0, pady = 5, padx=10)

    
    def descriptive_statistics(self):
        
        # Calculating the selected descriptive stats of the cloumn selected ( eg. stock[mean,Close])
        result = self.passedData.loc[self.descriptiveMetric_variable.get(), self.stock_column_variable.get()]
        result = str(round(result, 2))
        print("The", self.descriptiveMetric_variable.get(), " of the", self.stock_column_variable.get(), "is:", result)
        
        self.descriptive_result["text"] = f"{result}"
        # Co-efficient of variation
        # print("Co-efficient of variation is:", descdata.loc["std", "Adj Close"]/descdata.loc["mean", "Adj Close"])
         
    def open_window(self, descdata, stock):

        #storing passed values to use in DeacriptiveStats class
        self.passedData = descdata
        self.passedStock = stock
     
    #function to close the Descriptive Stats window when we click on quit
    def quitDesc(self):
        self.descStat.destroy()

