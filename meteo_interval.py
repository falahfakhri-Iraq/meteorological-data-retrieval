# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 14:30:14 2022

@author: FALAH FAKHRI

Function meteo_interval.py
===================================================================================================
This function is written to ease retrieval the meteorological data of any station throught entering 
the id of any meteorological stations they're already retrieved using the stations.py function 
Worthlynotes that this function give the choice to the user whether to decide save the
rusluts as *.csv file or settel for an overview in the screen. 
This function assist the user to go further in order to retrieve Hourly, Daily, or Monthly data.


and also when the user will be asked about the directory path if a decision of save the file
has been made, pleasee enter the path as in the example below, of course type in the desired name

instead of asterisk sign. 

D:/test/*.file

Please have a look at the example!
===================================================================================================
"""
# Import Meteostat library and dependencies
try:
    from datetime import datetime
    from meteostat import Hourly, Daily, Monthly
    import pandas as pd
    pd.set_option('display.max_rows', 30)
    pd.set_option('display.max_columns', 30)
    pd.set_option('display.width', 220)
    import os
    import sys
    from termcolor import colored
    
except ModuleNotFoundError:
    print('Module improt error')
    sys.exit()
else:
    print(colored('\nAll libraries properly loaded. Ready to start!!!', 'green'), '\n')   

def meto_inter_time(staton_id, data):
    
    """Returns information of meteorological data of any nearby point
    parameters
    ----------
    station_id: id number of the required station.
    data: Type of data scale to be retreived, Hourly, Daily, or Monthly.
    
    """
    
    start_date = str(input('Enter date(yyyy-mm-dd): '))
    
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    
    end_date = str(input('Enter date(yyyy-mm-dd): '))
    
    end_date =datetime.strptime(end_date, "%Y-%m-%d")
    
    if data ==  Monthly:
        
        data = Monthly(staton_id, start_date, end_date)
        
        data = data.fetch()
        
    elif data == Daily:
        
        data = Daily(staton_id, start_date, end_date)
        data = data.fetch()
        
    elif data == Hourly:
            
        data = Hourly(staton_id, start_date, end_date)
        data = data.fetch()
        
    answer = input('\nWould you like to save datafrane\n'+ '\n\n(Y/N)')
    
    if(answer == 'N' or answer == 'n'):
        
        print('Skipping...')
        
        print('Check out data on the screen\n\n', data)
       
            
    elif(answer == 'Y' or answer == 'y'):
        
        df = pd.DataFrame(data=data)
        
        user_input = input("Enter the path of your file: ")
        
        directpath = os.path.join(user_input)
        
        df.to_csv(directpath, encoding='utf-8') 
            
