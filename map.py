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
favorite = list(cub_data['Favorite'])

# Will use zip function on line 21 to merge the lat and lon variables in the loop

def color_maker(fav):
    if fav == True:
        return 'green'
    else:
        return 'red'

#_________________
## MARKERS ##

cub_foods = folium.FeatureGroup(name='Good Cub Locations')

for lt, ln, loc, fav in zip(lat, lon, locale, favorite):
    cub_foods.add_child(folium.Marker(
        location = [lt, ln],
        popup = f'Cub Foods: {loc}',
        icon = folium.Icon(color = color_maker(fav))))

map.add_child(cub_foods)


fav_foods = folium.FeatureGroup(name = 'Favorite Eateries')

fav_foods.add_child(folium.Marker(
    location = [44.95286, -93.28779],
    popup = 'Milkjam Creamery',
    icon = folium.Icon(color = 'purple')))

map.add_child(fav_foods)


group = folium.FeatureGroup(name = 'Country Populations')

group.add_child(folium.GeoJson(
    data = open('./assets/world.json', 'r', encoding = 'utf-8-sig').read(),
    style_function = lambda x: {'fillColor': 'blue' if x['properties']['POP2005'] < 10000000 else 'green'}))

map.add_child(group)


#_________________
## END MARKERS ##


map.add_child(folium.LayerControl())
# adds control layers to toggle what the map shows

map.save('map1.html')
