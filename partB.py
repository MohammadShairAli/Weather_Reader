import math

def highest_average(df):
    high = df['Max TemperatureC']
    average = high.mean()
    average = math.floor(average)
    print(f"Highest Average : {average}C")


def lowest_average(df):
    low = df['Min TemperatureC'].min() 
    average = low.mean()
    average = math.floor(average)
    print(f"Lowest Average: {low}C")

def humidity_average(df):
    high = df['Max Humidity']
    average = high.mean()
    average = math.floor(average)
    print(f"humidity : {average}C")



