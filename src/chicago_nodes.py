import folium
import json
import pandas as pd

map = folium.Map(location  =[41.8781, -87.6298], zoom_start=12)

tooltip = "Click for more info"

path = "/home/arjun/Array_of_things/leaflet_map/src/data/node_data/chicago_nodes.csv"
dataset = pd.read_csv("./leaflet_map/src/data/node_data/chicago_nodes.csv")

longitude = dataset["EPSG:4326_Long"]
latitude = dataset["EPSG:4326_Lat"]
address = dataset["Address"]
description = dataset["Description"]

for i in range(len(dataset)):
    folium.Marker([latitude[i], longitude[i]],
        popup = f"<strong>Address:</strong>{address[i]}",
        icon = folium.Icon(icon='cloud', color="red"),
        tooltip=description[i]
        ).add_to(map)

#generate map
map.save("chicago_aot_nodes.html")





