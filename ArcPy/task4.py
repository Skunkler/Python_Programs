
#import arcpy and env
import arcpy
from arcpy import env

#set out env variable
env = r'\HomeDir'

#Set the overwrite output to True so we can keep running the script over that will write over all our previous data sets
arcpy.env.overwriteOutput = True

#PowerLine points to our PowerLine.shp, the Parcel variable points to the Parcel.shp
PowerLine = r'OtherDir\PowerLine.shp'
Parcel = r'OtherDir\Parcels.shp'

#The PowerLine_buffer is the destination of our output buffered powerline shapefile
PowerLine_buffer = r'OtherDir\PowerLine_buffer.shp'

#creates a simple Parcel layer
Parcel_lyr = 'Parcel_lyr'

#This calls the Buffer tool that takes our PowerLine.shp, gives it a 250 foot buffer and points it to where we want the output
#buffered powerline shapefile to be
arcpy.Buffer_analysis(PowerLine, PowerLine_buffer, '250 Feet', 'FULL', 'ROUND', 'NONE', '', 'PLANAR')

#This creates a feature layer based off of our Parcel.shp, sort of like a temporary copy of the parcel data for computations
arcpy.MakeFeatureLayer_management(Parcel, Parcel_lyr)

#Creates an empty feature class called Parcels_Buffer.shp with a geometry type of Polygon
arcpy.CreateFeatureclass_management(r'\HomeDir', 'Parcels_Buffer.shp', 'POLYGON')

#This variable points to the newly created yet still empty feature class
Empty_FC = r''

#selects all of the parcels that fall within the 250 foot buffered powerline shapefile
arcpy.SelectLayerByLocation_management(Parcel_lyr, 'WITHIN', PowerLine_buffer)

#appends the selected features to the newly created Parcels_Buffer.shp
arcpy.Append_management(Parcel_lyr, Empty_FC, 'NO_TEST')

        
