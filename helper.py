from datetime import date
import os
from glob import glob
import pandas as pd
     

def gettingfiles(read_files):
    try:

        if not read_files:
            raise FileNotFoundError("No files found matching the pattern")
        dataframes = []
        for file in read_files:
            df = pd.read_csv(file)
            dataframes.append(df)
        combined_dataframe = pd.concat(dataframes, ignore_index=True)
        return combined_dataframe
    except Exception as e:
        print(f"An error occurred: {e}")

def getting_month(input_month):
    input_month = int(input_month)
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    if 1 <= input_month <= 12:
        return_month = months[input_month - 1]
        return return_month
    else:
        return "Invalid month"        
'''
def year_path(input_year, input_link):
        files_path = input_link
        read_files = glob(os.path.join(files_path, f'lahore_weather_{input_year}*'))
        combined_dataframe = gettingfiles(read_files)
        return combined_dataframe       

def month_path(input_year,input_month, input_link):
        files_path = input_link
        get_month = getting_month(input_month)
        read_files = glob(os.path.join(files_path, f'lahore_weather_{input_year}_{get_month}*'))
        combined_dataframe = gettingfiles(read_files)
        return combined_dataframe
'''

def extract_city_name(s):
    start_index = s.rfind('/') + 1
    end_index = s.find('_', start_index)
    if start_index != -1 and end_index != -1:
        return s[start_index:end_index]
    else:
        return None

def path(input_year,input_link,inputting_city,input_month = None,):
        files_path = input_link
        read_files = glob(os.path.join(files_path, f'{inputting_city}_weather_{getting_path(input_year,input_month)}*'))
        combined_dataframe = gettingfiles(read_files)
        return combined_dataframe

def getting_path(input_year,input_month=None):
     if(input_month != None):
          get_month = getting_month(input_month)
          returning = f"{input_year}_{get_month}"
          
          return returning
     else:
          returning = f"{input_year}"
          return returning
