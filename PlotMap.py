import gmplot
import os

def map(lat, long):      
    gmap3 = gmplot.GoogleMapPlotter(lat[0], long[0], 12) 
    gmap3.scatter( lat, long, 'red', size = 15, marker = False )  
    gmap3.plot(lat, long, 'cornflowerblue', edge_width = 2.5)
    gmap3.draw( "google_map.html" )
    os.system("start google_map.html")