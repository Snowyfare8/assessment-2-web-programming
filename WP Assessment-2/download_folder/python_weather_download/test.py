import geocoder

g = geocoder.google('Mountain View, CA')
g.geojson
g.json
g.wkt
g.osm

print(g.geojson)