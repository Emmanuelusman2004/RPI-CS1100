'''
Start to the Date class for Lab 9.  This code will not run in Python
until three methods are added:
    __init__,
    __str__
    same_day_in_year
'''

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]

class Date(object):
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    def __str__(self):
        string = '{}/{}/{}'.format(str(self.year),str(self.month),str(self.day))
        return string
    def same_day_in_year(self,date):
        return self.month == date.month and self.day == date.day
#CHECK 1 END
    def is_leap_year(self):
        if self.year % 400 == 0:
            return True
        elif self.year % 4 == 0 and self.year % 100 != 0:
            return True
        else:
            return False
    def __lt__(self,date):
        if self.year < date.year:
            return True
        elif self.year > date.year:
            return False
        elif self.year == date.year:
            if self.month < date.month:
                return True
            if self.month > date.month:
                return False
            elif self.month == date.month:
                if self.day < date.day:
                    return True
                elif self.day > date.day:
                    return False
        else: 
            return True
        

if __name__ == "__main__":
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1996, 4, 13)
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
    print("d2.same_day_in_year(d3)", d2.same_day_in_year(d3)) 
    print ()
    d1 = Date(1972, 3, 27)
    d2 = Date(1998, 4, 13)
    d3 = Date(1998, 5, 13)
    d4 = Date(1998, 4, 11)
    
