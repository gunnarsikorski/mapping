import folium
import pandas

map = folium.Map(
    location = [44.986, -93.269],
    zoom_start = 10,
    tiles = 'Stamen Terrain')

cub_data = pandas.read_csv('./assets/cub-locations.csv')
lat = list(cub_data['Latitude'])
lon = list(cub_data['Longitude'])
locale = list(cub_data['Cub Location'])

# Will use zip function on line 21 to merge the lat and lon variables in the loop

#_________________
## MARKERS ##

cub_foods = folium.FeatureGroup(name='Good Cub Locations')

for lt, ln in zip(lat, lon):
    cub_foods.add_child(folium.Marker(
        location=[lt, ln],
        popup='Cub Foods',
        icon=folium.Icon(color='red')))

map.add_child(cub_foods)



fav_foods = folium.FeatureGroup(name = 'Favorite Eateries')

fav_foods.add_child(folium.Marker(
    location = [44.95286, -93.28779],
    popup = 'Milkjam Creamery',
    icon = folium.Icon(color='purple')))

map.add_child(fav_foods)


#_________________
## END MARKERS ##

map.save('map1.html')
