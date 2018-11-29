#Sara D'Alessandro
#November 9, 2018
#This program saves info in a .html file

import folium

mapHunter = folium.Map(location=[40.75, -74.125])

folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapHunter)

mapHunter.save(outfile='nycMap.html')

