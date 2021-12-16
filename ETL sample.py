import glob                         # this module helps in selecting files 
import pandas as pd                 # this module helps in processing CSV files
import xml.etree.ElementTree as ET  # this module helps in processing XML files.
from datetime import datetime

import urllib.request

urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip", "source.zip")
tmpfile    = "temp.tmp"               # file used to store all extracted data
logfile    = "logfile.txt"            # all event logs will be stored in this file
targetfile = "transformed_data.csv"   # file where transformed data is stored
print(glob.glob('*.*'))

"""
def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    #dataframe.set_axis(['Name', 'Height', 'Weight' ], axis = 1, inplace = False)
    dataframe.set_axis(['Name', 'Height', 'Weight' ], axis = 1, inplace = True)
    return dataframe

def extract_from_json(file_to_process):
    dataframe_json = pd.read_json(file_to_process, lines = True)
    dataframe_json.set_axis(['Name', 'Height', 'Weight' ], axis = 1, inplace = True)
    return dataframe_json

def extract_from_xml(file_to_process):
    dataframe_xml = pd.read_xml(file_to_process)
    dataframe_xml.set_axis(['Name', 'Height', 'Weight' ], axis = 1, inplace = True)
    return dataframe_xml

def extract():
    extract_data = pd.DataFrame(columns = ['Name' ,'Height', "Weight"])
    
    #Process all CSV file
    for filesCSV in glob.glob('*.csv'):
        extract_data = extract_data.append(extract_from_csv(filesCSV), ignore_index = True)
    
    #Process all JSON file
    for filesJSON in glob.glob('*.json'):
        extract_data = extract_data.append(extract_from_json(filesJSON), ignore_index=True)
    
    #Process all xml file
    for filesXML in glob.glob('*.xml'):
        extract_data = extract_data.append(extract_from_xml(filesXML), ignore_index = True)
    
    return extract_data
extract()
"""