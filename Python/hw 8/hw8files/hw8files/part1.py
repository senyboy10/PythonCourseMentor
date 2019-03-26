class Date(object):
    def __init__(self, mon, day, year):
        self.day = day
        self.mon = mon
        self.year = year
    def __str__(self):
        return "%d/%d/%d" %(self.mon, self.day, self.year)
    def __sub__(self,other):
        days1 = 360*self.year + 30*self.mon + self.day
        days2 = 360*other.year + 30*other.mon + other.day
        return abs(days1-days2) - 1


    d1 = Date(4,21,2014)
    d2 = Date(5,16,2014)
    print '%d days left between %s and %s.' \
          %(d1-d2, str(d1), str(d2))
