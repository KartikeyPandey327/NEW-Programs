import csv
from gmplot import gmplot

gmap = gmplot.GoogleMapPlotter(18.596759606572064, 73.95410571855871, 17)

gmap.coloricon= "https://www.googlemapsmarkers.com/v1/%s/"

with open(r"C:\Users\karti\OneDrive\Documents\python\route.txt", 'r') as f:
    reader = csv.reader(f)
    k=0
    
    for row in reader:
        lat = float(row[0])
        log = float(row[1])
        print(lat)
        print(log)
        print(lat+log)

        if(k==0):
            gmap.marker(lat,log,'yellow')
            k=1

        else:
             gmap.marker(lat,log,'blue')

gmap.marker(lat,log,'red')
            
gmap.draw("mymap.html")