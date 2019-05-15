#import necessary modules
import ogr
import gdalconst
import sys
import math

#This points to each file we need to complete task3
filename = r'PowerLine.shp'
filename2 = r'Parcels.shp'

#This driver specifies that we are working with an ESRI Shapefile format
driver = ogr.GetDriverByName('ESRI Shapefile')

#These dataSource variables open up each of the two shapefiles and reads them
dataSource = driver.Open(filename, gdalconst.GA_ReadOnly)
dataSource2 = driver.Open(filename2, gdalconst.GA_ReadOnly)

#This error checks to make sure we can open up the shapefiles otherwise print the following
#error messages to the screen
if dataSource is None:
    print "Failed to open"
    sys.exit(1)
if dataSource2 is None:
    print "Failed to open"
    sys.exit(1)

#We get the Powerline layer using the GetLayer() method on the first dataSource variable
PowerLine_layer = dataSource.GetLayer(0)

#We grab the feature and store it in PowerLine_feature using the GetFeature() method on our PowerLine_layer variable
PowerLine_feature = PowerLine_layer.GetFeature(0)

#Grabs the Parcel_layer using the GetLayer(0) method on the parcels shapefile
Parcel_layer = dataSource2.GetLayer(0)

#grabs the features in Parcel_layer.GetFeature(0) and stores the values in parcel_features
parcel_features = Parcel_layer.GetFeature(0)

#Stores the values of the parcel and powerline shapefile feature counts
Parcel_Layer_featureCount = Parcel_layer.GetFeatureCount()
PowerLine_layer_featureCount = PowerLine_layer.GetFeatureCount()

#This is for task 3 which prints the address of each parcel that the powerline crosses
#loops through the powerline_layer_feature count
for i in range(0, PowerLine_layer_featureCount):
    #loops through the Parcel layer feature count
    for x in range(0, Parcel_Layer_featureCount):

        #Grabs the geometry of both the powerline and the parcel
        Powerline_feature_ref = PowerLine_layer.GetFeature(i)
        Powerline_geom_ref = Powerline_feature_ref.GetGeometryRef()
        Parcel_Layer_ref = Parcel_layer.GetFeature(x)
        Parcel_geom_ref = Parcel_Layer_ref.GetGeometryRef()
        #if a powerline geometry crosses a parcel geometry then print the address of that parcel
        if Powerline_geom_ref.Crosses(Parcel_geom_ref):
            address = Parcel_Layer_ref.GetField('SITUSADDR')
            print address    

dataSource = None
dataSource2 = None

