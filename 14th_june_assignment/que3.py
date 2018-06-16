# QUESTION 3: TEMPRATURE     FAHRENHEIT TO CELCIOUS   AND CELCIOUS TO FAHRENHEIT
class temprature:
    def convertFahrenheit(self,):
        cel = float(input("\n ENTER THE TEMPERATURE IN CELCIOUS"))
        f = (cel * 1.8)+ 32
        print("\nThe Temperature %0.2f Celsius = %0.2f Fahrenheit."%(cel, f))
    def convertCelsius(self):
        fe = float(input("\n ENTER THE TEMPERATURE IN FARHENHEIT  :"))
        c = (fe - 32) / 1.8
        print("\nThe Temperature %0.2f Fahrenheit = %0.2f Celcious."%(fe, c))
temp = temprature()
temp.convertCelsius()
temp.convertFahrenheit()