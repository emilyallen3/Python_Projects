#Datetime Challenge

from datetime import *
import pytz


class city():

    def getCityTime(self, region):

        tz_city = pytz.timezone(region)
        self.datetime_city = datetime.now(tz_city)
        cityName = self.datetime_city.strftime("%I:%M %p %Z %d %b %Y")
    
        def isOpen():
            self.hoursOpen = self.datetime_city.strftime("%H").split()
            for i in self.hoursOpen:
                X = int(i)
            if X >= 9 and X < 17:
                print("Open")
            else:
                print("Closed")

        isOpen()
        return(cityName)
        

    def getOfficeTimes():

        London = city()
        X = London.getCityTime('Europe/London')
        print("The time at the London office is: {}".format(X),"\n")
       
        New_York = city()
        X = New_York.getCityTime('America/New_York')
        print("The time at the New York office is: {}".format(X),"\n")

        Portland = city()
        X = Portland.getCityTime('America/Los_Angeles')
        print("The time at the Portland office is: {}".format(X),"\n")


city.getOfficeTimes()
