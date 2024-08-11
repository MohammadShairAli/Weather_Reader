import sys
from PartA import lowest_temp,highest_humidity,highest_temp
from partB import highest_average,lowest_average,humidity_average
from partC import graph_plotting
from helper import path,extract_city_name

def arg_pass():
    arg = sys.argv
    if arg[1] == '-e':
        concat = arg[2]+" "+arg[3]
        spliting = concat.split('/')
        input_years = spliting[0]
        input_link = '//'.join(spliting[1:])
        inputting_city = extract_city_name(input_link)
        combined_dataframe = path(input_years, input_link,inputting_city)
        high_temp,H_date = highest_temp(combined_dataframe)
        print(f"Highest : {high_temp}% on {H_date}")
        low_temp,L_date = lowest_temp(combined_dataframe)
        print(f"Lowest : {low_temp}% on {L_date}")   
        high_hum,H_date = highest_humidity(combined_dataframe)
        print(f"humidity : {high_hum}% on {H_date}")    

    elif (arg[1] == '-a'):
        concat = arg[2]+" "+arg[3]
        spliting = concat.split('/')
        input_years = spliting[0]
        input_months = spliting[1]
        input_link = '//'.join(spliting[2:])
        inputting_city = extract_city_name(input_link)
        combined_dataframe = path(input_years, input_link,inputting_city,input_months)
        highest_average(combined_dataframe)
        lowest_average(combined_dataframe)
        humidity_average(combined_dataframe)
    
    elif (arg[1] == '-c'):
        concat = arg[2]+" "+arg[3]
        spliting = concat.split('/')
        input_years = spliting[0]
        input_months = spliting[1]
        input_link = '//'.join(spliting[2:])
        inputting_city = extract_city_name(input_link)
        combined_dataframe = path(input_years, input_link,inputting_city,input_months)
        high_temp,H_date = highest_temp(combined_dataframe)
        low_temp,L_date = lowest_temp(combined_dataframe)
        graph_plotting(high_temp,low_temp)

arg_pass()
