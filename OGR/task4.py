
#import all the necessary modules
import os
import gdalconst
import sys
import ogr

#This points to the PowerLine.shp
InputFile = 'PowerLine.shp'
#This is where our output buffered Powerline shapefile will be
OutFileName = 'PowerLine_250_2.shp'
#This points to our Parcels.shp
Parcels = 'Parcels.shp'
#This points to where our output parcels that fall within the buffered area will be
Selected_parcels = 'SelectedParcels2.shp'

#Set out buffer value to 250 feet
Buffer_Val = 250

#define the driver as an ESRI Shapefile type
driver = ogr.GetDriverByName('ESRI Shapefile')

#The inputDS points to the PowerLine.shp
inputDS = driver.Open(InputFile)





#if the PowerLine.shp does not exists then error
if inputDS is None:
    print "could not open ", InputFile
    sys.exit(1)
#This points to the powerline layer
Original_input_layer = inputDS.GetLayer()
#This grabs the extent of our powerline layer
extent_of_layer = Original_input_layer.GetExtent()
#if the buffered powerline shapefile already exists then delete it
if os.path.exists(OutFileName):
    os.remove(OutFileName)

    
#Try creating the OutFileName else print the error message to the screen
try:
    outputDS = driver.CreateDataSource(OutFileName)
except:
    print "could not create the output data source"
    sys.exit(1)

#using the driver create the layer for the buffer powerline shapefile
Buffer_layer = outputDS.CreateLayer(OutFileName, Original_input_layer.GetSpatialRef(), geom_type = ogr.wkbPolygon)

#If Buffer_layer is non-existent then print the following error message
if Buffer_layer is None:
    print "Could not create the Buffer_layer"
    sys.exit(1)

#our feature ID
FID = 0

#oldFeature points to the 2nd feature in the powerline shapefile
oldFeature = Original_input_layer.GetNextFeature()

#assign the layer definition of the buffer shapefile to the Buffer_layerDef
Buffer_layerDef = Buffer_layer.GetLayerDefn()

#While still in the original PowerLine.shp
while oldFeature:
    #grab the geometry of the powerline shapefile
    geometry = oldFeature.GetGeometryRef()
    #buffer that piece of geometry based on the original value we defined earlier
    buffer_var = geometry.Buffer(Buffer_Val)
    #our new output feature will comprise the buffer layer definition
    #which has each piece of the buffered powerline geometry added to it
    newFeature = ogr.Feature(Buffer_layerDef)
    newFeature.SetGeometry(buffer_var)
    newFeature.SetFID(FID)
    #Creates the acctual buffered powerline
    Buffer_layer.CreateFeature(newFeature)

    #newFeature and oldFeature are freed up
    newFeature = None
    oldFeature = None

    #oldFeature is assigned the next part of the power line geometry
    oldFeature = Original_input_layer.GetNextFeature()
    #iterate FID by 1 so as to maintain uniqueness
    FID += 1

#When the powerline has been successfully buffered this message is printed on screen
print 'Buffered the powerline'

#free up the powerline and the powerline buffer data sources
outputDS = None
inputDS = None

#assign ParcelsDS and Buffer_powerlineDS to the parcels shapefile and buffered powerline shapefile
ParcelsDS = driver.Open(Parcels, gdalconst.GA_ReadOnly)
Buffer_powerlineDS = driver.Open(OutFileName, gdalconst.GA_ReadOnly)

#if ParcelsDS or the Buffer_powerlineDS do not exists, print the error message and end
if ParcelsDS is None:
    print "could not open ", ParcelsDS
    sys.exit(1)

if Buffer_powerlineDS is None:
    print "could not open", Buffer_powerlineDS
    sys.exit(1)


#Define the layer, feature and geometry of the powerline buffer shapefile using the GetLayer(), GetFeature(), and GetGeometryRef() methods
#and storing them in the appropriate variables
PowerLine_bufferlayer = Buffer_powerlineDS.GetLayer(0)
PowerLine_bufferfeature = PowerLine_bufferlayer.GetFeature(0)
#PowerLine_bufferlayer_geometry = PowerLine_bufferfeature.GetGeometryRef()


#stores the values of the number of features in the powerline shapefile layer
PowerLine_bufferlayer_featureCount = PowerLine_bufferlayer.GetFeatureCount()

#if the selected shapefile parcels already exists then delete it
if os.path.exists(Selected_parcels):
    os.remove(OutFileName)
    
#our new outputDS creates the data source for the selected parcels
outputDS = driver.CreateDataSource(Selected_parcels)

#grabs the parcel_layer, the SRS, and creates the layer for the selectedparcels output using the
#path pointing to the selected parcels, uses the SRS based on off of the spatial reference of the parcel layer, and defines the geom_type as a polygon
Parcel_layer = ParcelsDS.GetLayer(0)
SRS = Parcel_layer.GetSpatialRef()
SelectedParcels = outputDS.CreateLayer(Selected_parcels, SRS,ogr.wkbPolygon)

#Stores the number of features within the parcel layer
Parcel_featureCount = Parcel_layer.GetFeatureCount()


#This loops through both the powerline buffer layer and the parcel layer features
for i in range(0, PowerLine_bufferlayer_featureCount):
    for x in range(0, Parcel_featureCount):

        #grabs the geometries for each parcel and buffered powerline features 
        PowerLine_bufferfeature_ref = PowerLine_bufferlayer.GetFeature(i)
        PowerLine_buffergeom_ref = PowerLine_bufferfeature_ref.GetGeometryRef()
        Parcel_Layer_ref = Parcel_layer.GetFeature(x)
        Parcel_geom_ref = Parcel_Layer_ref.GetGeometryRef()

        #if the geometry of the parcel is within the powerline buffer
        if Parcel_geom_ref.Within(PowerLine_buffergeom_ref):

            #the parcel is added to the output Selected parcels shapefile
            Parcel_selected_feature = Parcel_Layer_ref
            SelectedParcels.CreateFeature(Parcel_selected_feature)


#free up our ouputDS, ParcelsDS, and BufferPowerlineDS
outputDS = None
ParcelsDS = None
Buffer_powerlineDS = None

