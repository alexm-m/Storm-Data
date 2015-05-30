from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import sys



filename = sys.argv[1]

print(sys.argv[1])

def read_csv(path):
    
    output = []
    
    for row in csv.DictReader(open(path)):
        output.append(row)
        
    return output
    



data = read_csv(filename)
lats = [25.]
lons = [-180.]


print(len(data))
for i in range(len(data)):
    lats.append(float(data[i]['LATITUDE']))
    lons.append(float(data[i]['LONGITUDE']))
#print 'lats:',lats

print 'hello'
#print('longs:',longs)

m = Basemap(projection='merc',llcrnrlat=20,urcrnrlat=50,\
            llcrnrlon=-130,urcrnrlon=-60,lat_ts=20,resolution='c')
            
m.drawcoastlines()
x, y = m(lons,lats)
m.fillcontinents(color='brown',lake_color='white')
# draw parallels and meridians.
m.drawparallels(np.arange(-90.,91.,25.))
m.drawmeridians(np.arange(-180.,181.,60.))
m.drawmapboundary(fill_color='white')
m.drawstates()
m.drawcountries()

m.scatter(x,y,20,color='r')

plt.title("Mercator Projection")
plt.savefig('YAY')
plt.show()
#if __name__ == "__main__":
#    main()
