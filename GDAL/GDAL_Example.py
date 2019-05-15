#import all the necessary modules we'll need for this lab
import numpy, os
from osgeo import gdal
from osgeo import gdalconst
from osgeo import gdal_array





#The inputs for both the red band, band 3 from landsat, and the NIR band, band 4 from landsat

band30 = r''
band40 = r''

#checks to see if the files for each band exists
if os.path.exists(band30) and os.path.exists(band40):
    try:
        #using gdal.Open method and storing the values for the red and NIR bands in the band_30 and band_40 variables
        band_30 = gdal.Open(band30)
        band_40 = gdal.Open(band40)

        #assigning the appropriate driver, based on the driver of band_30 using the GetDriver() method
        #really you could also use band_40.GetDriver() it doesn't matter
        outDriver = band_30.GetDriver()

        #getting the pixel sizes based on the file information that I got using GDALINFO
        rows = 1500
        cols = 1500

        #we assign our datatype to the appropriate 32 bit float data type
        dataType = gdalconst.GDT_Float32

        #takes the values of the red band and NIR band and multiplies them by 1.0 so the values are converted to a float datatype and
        #will assist in preventing the division by zero
        red_band = 1.0 * band_30.ReadAsArray()
        NIR_band = 1.0 * band_40.ReadAsArray()

        #NDVI_out creates the output data in the proper fiel format with the correct pixel size (columns and rows) the correct number of bands, which is 1, and the
        #the datatype that we want in order to maintain data integrity, which is a 32 bit float
        NDVI_out = outDriver.Create('NDVI2.tif', cols, rows, 1, dataType)

        #set the projected coordinate systeem based on the red band, again this can apply to the NIR band, it really doesn't matter as long as we have the proper
        #spatial reference
       # NDVI_out.SetGeoTransform(band_30.GetGeoTransform())
        NDVI_out.SetProjection(band_30.GetProjection())

        #This if else statement checks to make sure that we are not dividing by 0
        if NIR_band.any() == 0.0 and red_band.any()==0:
            NDVI = 0
        else:
            #calcalates the NDVI index and multiplies the values of this index against an array of 1s that are the same size as the output image that we want
            NDVI = (NIR_band - red_band)/(NIR_band + red_band) * numpy.ones((cols, rows))

        #out_band is equal to the 1 empty band that we created using the outDriver.create() method
        out_band = NDVI_out.GetRasterBand(1)

        #write our array of index values to the empty array/output image thus creating an NDVI image
        out_band.WriteArray(NDVI)

        #free up our variables
        red_band = None
        NIR_band = None
        NDVI_out = None
        out_band = None

    #if the input files for bands 3 and 4 for landsat do not exist or there is some other form of bad input the program will print out this error message and exit 
    except:
        print "Sorry but there was an error with your inputs. Please check over everything and try again."
                       
                       


