from pyhdf.SD import *
from numpy import *

filename = 'CAL_LID_L2_01kmCLay-Standard-V4-20.2020-06-30T23-20-07ZD.hdf'
hdfFile = SD(filename, SDC.READ)

file_attrs = hdfFile.attributes()
datasets = hdfFile.datasets()

print("file:", filename)
print("File attributes:")
for key, value in file_attrs.items():
    print(key)
    print("{0}: {1}".format(key, value))

print("Datasets:", len(datasets))
for key, value in datasets.items():
    print(key)

print("Dataset Latitiude:")
lat = hdfFile.select('Latitude')
print(lat.info())

hdfFile.end()
