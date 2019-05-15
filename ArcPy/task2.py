#import arcpy
import arcpy
from arcpy import env

#sets the environment we'll be working in
env = r'\HomeDir'

#the Parcels variable points to the Parcels.shp
Parcels = 'OtherDir\Parcels.shp'

#our Fields variable stores a list of all the fields within the parcels.shp
Parcel_Fields = arcpy.ListFields(Parcels)

#iterates through the list of fields within the parcels shapefile
for Parcel_field in Parcel_Fields:
    #prints the following message to the user grabbing the field name and data type of that field
    print 'There is a field called ', Parcel_field.name, ' and it is of a type ', Parcel_field.type

