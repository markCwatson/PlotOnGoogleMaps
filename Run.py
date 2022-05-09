# Script for reading .csv file to extract lat/long data
# lat/long data must be in header as "Latitude" and "Longitude"
# Plots results on google map html file and opens in browser

# By Mark Watson
# July 23, 2021

#!! uses PlotMap.py (needs to be in same directory)
#!! uses google_map.html (needs to be in same directory)
#!! may need to do 'pip install gmplot'
#!! may need to do 'pip install os'
#!! may need to do 'pip install pandas'

import os
from PlotMap import map
import pandas as pd

files = [f for f in os.listdir('.') if f.endswith('.csv')]
if len(files) == 0:
    raise ValueError('Include csv file in the current directory')

col_list = ["Latitude", "Longitude"]

for name in files:
    df = pd.read_csv(name, usecols=col_list)
    lat = df[col_list[0]]
    long = df[col_list[1]]

map(lat, long)