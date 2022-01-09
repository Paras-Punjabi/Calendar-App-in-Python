import datetime
import calendar

class Day:
    def __init__(self,date,day):
        self.day = day
        self.date = date

    def toDict(self):
        return {"date":self.date,"day":self.day,"dayName":Calendar.weekdays[self.day]}

class Calendar:
    weekdays = ["MON","TUE","WED",'THU','FRI','SAT','SUN']
    months = ("January","February","March","April","May","June","July","August","September","October","November","December")
    
    def getTotalDaysInMonth(self,year:int,monthIndex:int):
        if monthIndex == 1 or monthIndex==3 or monthIndex==5 or monthIndex == 7 or monthIndex==8 or monthIndex==10 or monthIndex==12:
            return 31
        elif monthIndex==2:
            if self.isLeapYear(year):
                return 29
            else:
                return 28
        else :
            return 30
        
    def isLeapYear(self,year:int):
        return calendar.isleap(year)
    
    @staticmethod
    def getToday():
        return datetime.datetime.today()
    
    def getCalendarArray(self,year:int,month:int):
        array = []

        for i in range(self.getTotalDaysInMonth(year,month)):
            element = Day(datetime.datetime(year,month,i+1).day,datetime.datetime(year,month,i+1).weekday())
            array.append(element.toDict())
        
        return array

