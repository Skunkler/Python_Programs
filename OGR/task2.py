import ogr
import gdalconst
import sys
import math

filename = r'Parcels.shp'


#This driver specifies that we are working with an ESRI Shapefile format
driver = ogr.GetDriverByName('ESRI Shapefile')

#The dataSource variable opens up the shapefile and reads it
dataSource = driver.Open(filename, gdalconst.GA_ReadOnly)

#This error checks to make sure we can open up the shapefile otherwise print the following
#error messages to the screen
if dataSource is None:
    print "Failed to open"
    sys.exit(1)

#Grabs the Parcel_layer using the GetLayer(0) method on the parcels shapefile
Parcel_layer = dataSource.GetLayer(0)


#grabs the features in Parcel_layer.GetFeature(0) and stores the values in parcel_features
parcel_features = Parcel_layer.GetFeature(0)


#grabs the layer definitions from the Parcel_layer variable usig the GetLayerDefn() method and stores them
#in the Parcel_FEatureDefn variable
Parcel_FeatureDefn = Parcel_layer.GetLayerDefn()

#Grab the total number of fields in the layer and store them in a variable called fieldCount
fieldCount = Parcel_FeatureDefn.GetFieldCount()

#This solves task 2
#Iterate through the number of fields within the parcel shapefile


for i in range(0, fieldCount):
    #Grabs the field of the parcel
    Parcel_Def_of_Field = Parcel_FeatureDefn.GetFieldDefn(i)
    #Grabs the name of the field
    Parcel_fieldName = Parcel_Def_of_Field.GetNameRef()
    #grab the data type of the field and describe the datatype in a text format
    Parcel_FieldDataType = Parcel_Def_of_Field.GetType()
    Parcel_FieldDataTypeText = Parcel_Def_of_Field.GetFieldTypeName(Parcel_FieldDataType)


    #print the field names and data types to the user
    print "There is a field called ", Parcel_fieldName, " which has a data type of ", Parcel_FieldDataTypeText, "."

dataSource = None
