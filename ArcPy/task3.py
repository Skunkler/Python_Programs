#imports arcpy, sets the overwriteOutput to true
import arcpy
from arcpy import env
arcpy.env.overwriteOutput = True


#set the environment we'll be working in
env = r'HomeDir\'

#the PowerLine variable points to the PowerLine.shp
PowerLine = r'OtherDir\PowerLine.shp'

#The Parcels variable points to the Parcels.shp
Parcels = r'OtherDir\Parcels.shp'

#Creates a layer based on the parcels shapefile
arcpy.MakeFeatureLayer_management(Parcels, 'Parcels_lyr')

#selects the parcels from the parcel layer that intersect the PowerLine
arcpy.SelectLayerByLocation_management('Parcels_lyr', 'INTERSECT', PowerLine)

#using a search cursor, loop through the parcels layer of selected parcels and find the fields 'SITUSADDR', and 'Area'
#store their value in a cursor
with arcpy.da.SearchCursor('Parcels_lyr', ['SITUSADDR', 'Area']) as cursor:
    #looping through each row in the cursor
    for row in cursor:
        #print the first element, or the address of each of the selected parcels, as well as the second element of the cursor
        #or the area of each of the selected parcels
        print row[0], row[1]

