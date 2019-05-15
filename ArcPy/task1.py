
#imports arcpy
import arcpy
from arcpy import env

#sets our environment that we're working in
env = r'\\homeDir'


#points to our PowerLine.shp
PowerLine = 'OtherDir\PowerLine.shp'

#create an empty list
List_coords = []

#uses a search cursor to loop through each object ID and piece of geometry
for row in arcpy.da.SearchCursor(PowerLine, ["OID@", "SHAPE@"]):
    #grabs each line segment of the powerline
    for line in row[1]:
        #iterates through the points of each line in the powerline shapefile
        for point in line:
            #creates a tuple of x and y coordinates for each point
            coords = point.X, point.Y
            #adds these coordinate pairs to our List_coords
            List_coords.append(coords)

#creates a counter variable sets it to 0
distance_sum = 0

#iterates through the List of coordinates, starts at 0 and ends before the last point
for i in range(0, len(List_coords)-1):

    #calculates the distance formula by grabbing the x1 and x2 as well as the Y1 and Y2 coordinates by incrementing i or keeping i the same as
    #the value of i in the loop
    distance = math.sqrt(((List_coords[i+1][0]-List_coords[i][0])**2) + ((List_coords[i+1][1]-List_coords[i][1])**2))
    #sums the distances between each of the points in the powerline shapefile
    distance_sum += distance

#print the length of the powerline shapefile in miles
print distance_sum/5280


