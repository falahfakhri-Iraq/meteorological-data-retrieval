# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:30:58 2022

@author: FALAH FAKHRI


Function stations.py
===================================================================================================
This function is written to ease retrieval the id and more other information of any 
meteorological stations around the glob, might be some is missed, in this case please
visit the source webpage, https://dev.meteostat.net/ 
Worthlynotes that this function give the choice to the user whether to decide save the
rusluts as *.csv file or settel for an overview in the screen. 
This function assist the user to go further to use the other one meteo_interval, in order
to retrieve Hourly, Daily, or Monthly data.

When the user will be asked to enter the latitude, and langitude please enter the data as

-33.4050
150.6412 

and also when the user will be asked about the directory path if a decision of save the file
has been made, pleasee enter the path as in the example below, of course type in the desired name

instead of asterisk sign. 

D:/test/*.file

Please have a look at the example!
===================================================================================================
"""

try:
    from meteostat import Stations
    import pandas as pd
    import os
    import sys
    from termcolor import colored
    pd.set_option('display.max_rows', 30)
    pd.set_option('display.max_columns', 30)
    pd.set_option('display.width', 220)
    
except ModuleNotFoundError:
    print('Module improt error')
    sys.exit()
else:
    print(colored('\nAll libraries properly loaded. Ready to start!!!', 'green'), '\n')   


def station_meteo_data():
    
    """Returns information of meteorological stations of any nearby point
    parameters
    ----------
    follow the questions of the funtion and enter the lat, lon, and y, n with regard
    to save or not the dataframe, and a directory path of a decision of saving the file
    is made
    
    """
    lat = float(input('Please enter Latitude Decimal coordinate : '))
    lon = float(input('Please enter Longitude Decimal coordinate: '))
    num_stations = int(input('Enter the number of stations to be retrieved please : '))
    
    stations = Stations()
    stations = stations.nearby(lat, lon)
    
    station = stations.fetch(num_stations)
    
    answer = input('\nWould you like to save datafrane\n'+ '\n\n(Y/N)')
    if(answer == 'N' or answer == 'n'):
        print('Skipping...')
        
        print('An overview of nearby meteorological stations :\n\n',station)
        
    elif(answer == 'Y' or answer == 'y'):
        
        
        df = pd.DataFrame(station)
        
        user_input = input('Enter the path of your file with an extention *.csv: ')
        
        directpath = os.path.join(user_input)
        
        df.to_csv(directpath, encoding='utf-8')
    
   
    


