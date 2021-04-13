import folium

map = folium.Map(
    location = [44.986, -93.269],
    zoom_start = 10,
    tiles = 'Stamen Terrain')

#_________________
## MARKERS ##

fav_foods = folium.FeatureGroup(name = 'Favorite Eateries')

fav_foods.add_child(folium.Marker(
    location = [44.95286, -93.28779],
    popup = 'Milkjam Creamery',
    icon = folium.Icon(color='purple')))

map.add_child(fav_foods)

#_________________

map.save('map1.html')
