import pandas as pd
def highest_temp(df):
    
    high = df['Max TemperatureC']
    if high is None:
            high = df.fillna(None)
    high = high.max()
    location = df.loc[df['Max TemperatureC'] == high]
    try:
        date = location['PKT'].values.tolist()
    except Exception as e1:
        try:
            date = location['PKST'].tolist() 
        except Exception as e2:
            date = location['GST'].tolist() 
    series = pd.Series(date)
    if series.isna().any():
        date = location['PKST'].tolist()
    return high,date       

def lowest_temp(df):
    low = df['Min TemperatureC'].min()
    location = df.loc[df['Min TemperatureC'] == low]
    try:
        date = location['PKT'].values.tolist()
    except Exception as e1:
        try:
            date = location['PKST'].tolist() 
        except Exception as e2:
            date = location['GST'].tolist()  
    series = pd.Series(date)
    if series.isna().any():
        date = location['PKST'].tolist()  
    return low,date    
    

def highest_humidity(df):
    high = df['Max Humidity'].max()
    location = df.loc[df['Max Humidity'] == high]
    try:
        date = location['PKT'].values.tolist()
    except Exception as e1:
        try:
            date = location['PKST'].tolist() 
        except Exception as e2:
            date = location['GST'].tolist() 
    series = pd.Series(date)
    if series.isna().any():
        date = location['PKST'].tolist()
    return high,date       
    
