import ogr
import gdalconst
import sys
import math


#This points to the file we need to complete task1
filename = r'PowerLine.shp'


#This driver specifies that we are working with an ESRI Shapefile format
driver = ogr.GetDriverByName('ESRI Shapefile')

#These dataSource variables open up each of the two shapefiles and reads them
dataSource = driver.Open(filename, gdalconst.GA_ReadOnly)


#This error checks to make sure we can open up the shapefiles otherwise print the following
#error messages to the screen
if dataSource is None:
    print "Failed to open"
    sys.exit(1)

#We get the Powerline layer using the GetLayer() method on the first dataSource variable
PowerLine_layer = dataSource.GetLayer(0)

#We grab the feature and store it in PowerLine_feature using the GetFeature() method on our PowerLine_layer variable
PowerLine_feature = PowerLine_layer.GetFeature(0)

#we grab the geometry and store it in the PowerLine_geometry variable using the GetGeometryRef()
#method on our PowerLine_feature variable
PowerLine_geometry = PowerLine_feature.GetGeometryRef()

#our nPts variable stores all the points within the PowerLine_geometry using the GetPointCount() method
nPts = PowerLine_geometry.GetPointCount()
#Our initial counter for the points in the powerline geometry that are to be used for the calculation
calc_base = 0
#Our final output variable that will be used to store up the distance
Final_answer_Feet = 0

#This loop solves task 1
for i in range(1, nPts):
    #As long as our iterator does not equal the total number of points within PowerLine.shp
    if calc_base != nPts:
        #FirstX stores the geometry at the point using the GetX() method on the Powerline geometry
        FirstX = PowerLine_geometry.GetX(calc_base)
        #FirstY stores the geometry at the point using the GetY() method on the Powerline geometry
        FirstY = PowerLine_geometry.GetY(calc_base)
        #Store the x and y values from the iterator by using the PowerLine_geometry.GetX() and GetY methods
        X = PowerLine_geometry.GetX(i)
        Y = PowerLine_geometry.GetY(i)
        #Calculates the distance between each point
        answer = math.sqrt((((X-FirstX)**2)+((Y-FirstY)**2)))
        #sums the values between each point in Final_anwer_Feet
        Final_answer_Feet += answer
        #increments calc_base by 1
        calc_base += 1
#Prints out the final answer in miles        
print Final_answer_Feet/5280

