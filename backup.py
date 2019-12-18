import geopandas as gpd
import json
import numpy as np
import itertools
from itertools import izip_longest

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.lines import Line2D
from matplotlib.collections import PatchCollection
plt.rcParams['figure.figsize'] = (10, 10)
df_places = gpd.read_file('rbc_floorplan.geojson')
patches = []

with open('rbc_floorplan.geojson') as f:
    data = json.load(f)

fig, ax = plt.subplots(1, 1)
for feature in data['features']:
    print "Done"
    list1 = feature['geometry']['type']
    list2 = feature['geometry']['coordinates']
    if list1 == "Polygon":
        flat_list = list(itertools.chain.from_iterable(list2))
        polygon = Polygon(flat_list,fill=None, closed=True)
        ax.add_patch(polygon)
        #patches.append(polygon)
    elif list1 == "LineString":
        x = list2[0]
        y = list2[1]
        line = Line2D(x, y, marker='o', markerfacecolor='r', animated=True)
    else:
        x = list2[0]
        y = list2[1]
        plt.plot(x, y, marker='.', markersize='3', markerfacecolor='black')

        #ax.Patch(x,y)
#p = PatchCollection(patches)
ax.autoscale_view()
plt.savefig('test4.png')
plt.show()


#for ty in list1:
    #flat_list = list(itertools.chain.from_iterable(list2))
    #print flat_list
    #merged = list(itertools.chain.from_iterable(flat_list))
    #print list2
    #if list1 != "Point":
       #for item in list2:
       #print item[0]
       #print item[1]
       #a = item
       #print a
       # y = item[1]
                    #arr = np.array(flat_list)
                    #row = arr.shape[0]
                    #col = arr.shape[1]
                    #print row
                    #col = arr.shape[z[1]]
                    #colors = list('bgrcmykw')

    #ax.scatter(x, y, color='blue')
    #plt.plot(x, y)
            #for x in range(0, row-1):
             #   for y in range(0, col-1):
              #      ax.scatter(x, y, color='blue')
               #     ax.plot(x, y)
#plt.savefig('/Users/yoginidandekar/Desktop/test.png')












