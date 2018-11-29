#Sara D'Alessandro
#November 9, 2018
#This program saves info in a .html file

import folium
import pandas as pd

csvFile = input("Enter CSV file name: ")
output = input("Enter output file: ")

df = pd.read_csv(csvFile)
df.head()

tiles = "Cartodb Positron"

mapCollision = folium.Map(location = [40.75, -74.125])

folium.Marker(location = ["LATITUDE", "LONGITUDE"], popup = "TIME").add_to(mapCollision)

mapCollision.save(outfile = output)
