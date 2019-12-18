import json
import itertools

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.lines import Line2D

plt.rcParams['figure.figsize'] = (10, 10)
patches = []

with open('rbc_floorplan.geojson') as f:
    data = json.load(f)

fig, ax = plt.subplots(1, 1)
for feature in data['features']:
    types_list = feature['geometry']['type']
    coords_list = feature['geometry']['coordinates']
    if types_list == "Polygon":
        flat_list = list(itertools.chain.from_iterable(coords_list))
        polygon = Polygon(flat_list, fill=None, closed=True)
        ax.add_patch(polygon)
    elif types_list == "LineString":
        x = coords_list[0]
        y = coords_list[1]
        line = Line2D(x, y, marker='.', markerfacecolor='r')
    else:
        x = coords_list[0]
        y = coords_list[1]
        plt.plot(x, y, marker='.', markersize='3', markerfacecolor='black')
ax.autoscale_view()
plt.savefig('geojsonimageplot.png')
print "Image plotted using GeoJson"
















