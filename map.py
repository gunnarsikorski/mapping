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


cub_foods = folium.FeatureGroup(name = 'Good Cub Locations')

cub_locations = [[44.97089515982077, -93.34941680718995],
                 [45.00683148574318, -93.2321720985536],
                 [44.882780266340134, -93.32040603725443]]

for coords in cub_locations:
    cub_foods.add_child(folium.Marker(
        location = coords,
        popup = 'Cub Foods',
        icon = folium.Icon(color = 'red')))

map.add_child(cub_foods)

#_________________

map.save('map1.html')
