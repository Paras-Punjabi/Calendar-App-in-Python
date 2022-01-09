from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Utils import Calendar

class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Calendar App")
        self.root.geometry("600x500")
        self.root.resizable(False,False)
        self.today = Calendar.getToday()

        self.year = self.today.year
        self.monthIndex = self.today.month
        self.day = self.today.day
        self.weekDay = self.today.weekday()
        self.dayName = Calendar.weekdays[self.today.weekday()]

        self.dateLabelsOnWindow = []

        self.frame = Frame(self.root,background="#ececec")
        self.move_to_date_frame = Frame(self.root)
        self.menu = Menu(self.root)

        self.setUpCalendar()
        self.root.mainloop()

    def selectDate(self,e):
        for items in self.dateLabelsOnWindow:

            if int(items.cget("text")) == self.today.day and self.year == self.today.year and self.monthIndex == self.today.month:
                items.config(background="#19668A",foreground="white")

            else:
                items.config(background="#D3D3D3",foreground="black")
            items.selected = False

        e.widget.config(background="#3f3f3f",foreground="white")
        e.widget.selected = True
    
    def nextMonth(self):
        self.monthIndex +=1
        self.dateLabelsOnWindow = []
        if self.monthIndex > 12:
            self.monthIndex = 1
            self.year+=1
        self.setUpCalendar()
            
    def previousMonth(self):
        self.monthIndex -=1
        self.dateLabelsOnWindow = []
        if self.monthIndex < 1:
            self.monthIndex = 12
            self.year-=1
        self.setUpCalendar()

    def getToday(self):
        self.monthIndex = self.today.month
        self.year = self.today.year
        self.setUpCalendar()

    def moveToDate(self,year,month):
        try:
            if month =="" or year == "":
                raise Exception()  

            self.year = int(year)
            self.monthIndex=Calendar.months.index(month.capitalize())+1
            self.setUpCalendar()

        except Exception as e:
            messagebox.showwarning(title="Warning",message="Fill all the entries carefully")

    def createMenuBar(self):
        self.menu = Menu(self.root)
        home = Menu(self.menu,tearoff=False)
        about = Menu(self.menu,tearoff=False)

        self.menu.add_cascade(label="Home",menu=home)
        self.menu.add_cascade(label="About",menu=about)

        home.add_cascade(label="Today",command=self.getToday)
        home.add_cascade(label="Move to Date",command=self.moveToDatePage)
        home.add_separator()
        home.add_cascade(label="Exit",command=self.root.destroy)

        about.add_cascade(label="About",command=lambda:messagebox.askokcancel(title="About",message="This is a calendar app made using python by Paras Punjabi"))

        self.root.config(menu=self.menu)
    
    def moveToDatePage(self):
        self.frame.pack_forget()

        month = StringVar()
        year = StringVar()

        year.set(self.year)
        month.set("January")
        Label(self.move_to_date_frame,text="Go To Date",font=("monospace",25,"bold")).grid(row=0,column=0,columnspan=2,pady=20)

        Label(self.move_to_date_frame,text="Month",font=("monospace",15,"bold")).grid(row=1,column=0,pady=10)
        combobox = ttk.Combobox(self.move_to_date_frame,textvariable=month,width=40,font=("monospace",15,"bold"))
        combobox["values"] = Calendar.months
        combobox.grid(row=1,column=1,pady=10)

        Label(self.move_to_date_frame,text="Year",font=("monospace",15,"bold")).grid(row=2,column=0,pady=10)
        Entry(self.move_to_date_frame,textvariable=year,font=("monospace",15,"bold"),width=40).grid(row=2,column=1,pady=10)

        Button(self.move_to_date_frame,text="Go to Date",font=("monospace",15,"bold"),command=lambda:self.moveToDate(year.get(),month.get())).grid(row=3,column=1,pady=10)
        Button(self.move_to_date_frame,text="Home",font=("monospace",15,"bold"),command=self.setUpCalendar).grid(row=4,column=1,pady=10)
        self.move_to_date_frame.pack()
        
    def setUpCalendar(self):
        self.move_to_date_frame.pack_forget()
        self.dateLabelsOnWindow = []
        self.frame.destroy()
        self.createMenuBar()

        self.frame = Frame(self.root,background="#ececec")
        heading = Label(self.frame,text=Calendar.months[self.monthIndex-1].upper() + " " + str(self.year),font=("monospace",20,"bold"),anchor="center")
        heading.grid(row=0,column=2,columnspan=5,padx=10,pady=10)

        Button(self.frame,text="\u25C4",font=("monospace",15,"bold"),command=self.previousMonth).grid(row=0,column=0,pady=10,padx=10)
        Button(self.frame,text="\u25BA",font=("monospace",15,"bold"),command=self.nextMonth).grid(row=0,column=8,pady=10,padx=10)

        # all days of calendar
        Label(self.frame,text=" ",font=("monospace",10,"bold")).grid(row=2,column=0,padx=10)
        for i in range(7):
            label =  Label(self.frame,text=Calendar.weekdays[i],font=("monospace",10,"bold"))
            label.grid(row=2,column=i+1,padx=10)

        Label(self.frame,text="",font=("monospace",10,"bold")).grid(row=2,column=8,padx=10)

        # all dates of calendar
        columnIndex = 1
        rowIndex = 3
        todaysCalendar = Calendar().getCalendarArray(self.year,self.monthIndex)
        
        for items in todaysCalendar:
            if columnIndex>7:
                columnIndex =1
                rowIndex +=1
            columnIndex = items["day"]+1

            label = Label(self.frame,text=str(f'0{items["date"]}') if items["date"] <= 9 else str(items["date"]) ,font=("monospace",13,"bold"),background="#D3D3D3",border="2")
            label.grid(row=rowIndex,column=items["day"]+1,padx=10,pady=5,ipadx=10,ipady=10)
            label.selected = False

            if items["date"] == self.today.day and items["day"] == self.today.weekday() and self.today.year == self.year and self.today.month == self.monthIndex:
                label.config(background="#19668A",foreground="white")

            self.dateLabelsOnWindow.append(label)
            label.bind("<Button-1>",lambda e:self.selectDate(e))
            columnIndex+=1
        
        self.frame.pack(ipadx=10,ipady=10,side="top")

if __name__ == '__main__':
    App()

    '''
    To convert into exe:-
    pyinstaller --onefile -w Calendar.py
    '''
    
    