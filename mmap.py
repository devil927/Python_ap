# importing the library
import folium
import pandas as pd
# Import the data for volcanoes
data=pd.read_csv('volcanoes.txt')
lat=list(data['LAT'])
lon=list(data['LON'])
elev=list(data['ELEV'])

# Color preducer
def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif elevation<3000 and elevation>=1000:
        return 'orange'
    else:
        return 'red'
   
# Making an map for visualizing
m=folium.Map(location=[38,-99],zoom_start=6,tiles="Mapbox Bright")
# Adding markings of volcanoes
fg=folium.FeatureGroup(name="volcanoes")
for lt,ln,el in zip(lat,lon,elev):
   fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6,fill=True, popup=str(el)+" m",
    fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=open('world.json',encoding='utf-8-sig').read()))


m.add_child(fg)
m.add_child(folium.LayerControl())

    

# Saving the Html file
m.save("Map.html")
