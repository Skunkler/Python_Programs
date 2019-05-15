

#import necessary modules
import math, os

#create our City class
class City:

    #our Cities list that stores all the instances of the City class
    Cities = []
    #Cities instances attributes
    Cities_instances_attributes = []
    
    #this allAtt_Dict stores all the attributes for all the cities
    allAtt_Dict = {}


            
    def __init__(self, name, Cityname = 'None', label = 'None', latitude = 'None', Longitude = 'None', pop_1970 = 'None', pop_1975 = 'None', pop_1980 = 'None', pop_1985 = 'None', pop_1990 = 'None', pop_1995 = 'None', pop_2000 = 'None', pop_2005 = 'None', pop_2010 = 'None'):# label, latitude, longitude, pop_1970, pop_1975, pop_1980, pop_1985, pop_1990, pop_1995, pop_2000, pop_2005, pop_2010)
        #Starts the first part of our program by designating the name of the instance for class City      
        self.name = name
        #This stores the attribute names for the user so if the user knows what to type in as commands
        all_list=[]

        #Checks to see if the CityPop.csv exists
        if os.path.exists('CityPopulation.csv'):
            try:
                #loop through the csv
                fileinput = open("CityPopulation.csv", "r")

                
                for line in fileinput:
                    #store each row in the csv into our city attribute dictionary using the label as the key
                    City.allAtt_Dict[line.split(',')[4]] = line.split(',')[1:]
                    #if the names entered by the user matches the label field in each row of the csv continue
                    if name == line.split(',')[4]:
                        #assigning values to Cityname, label, latitude, longitude, and populations for years 1970-2010
                        #the values are assigned based on where each element in the line.split(',') list is for each row
                        self.Cityname = line.split(',')[3]  
                        self.label = line.split(',')[4]
                        #for the name and label, we keep as a string data type but for longitude, latitude, and the populations for each year
                        #are converted to a float data type
                        self.latitude = float(line.split(',')[1])
                        self.longitude = float(line.split(',')[2])
                        self.pop_1970 = float(line.split(',')[5])
                        self.pop_1975 = float(line.split(',')[6])
                        self.pop_1980 = float(line.split(',')[7])
                        self.pop_1985 = float(line.split(',')[8])
                        self.pop_1990 = float(line.split(',')[9])
                        self.pop_1995 = float(line.split(',')[10])
                        self.pop_2000 = float(line.split(',')[11])
                        self.pop_2005 = float(line.split(',')[12])
                        self.pop_2010 = float(line.split(',')[13])
                        
                        #we append each attribute for the specific instance in a list so the user can query the whole row
                        #this is also used to help with the calculations in other methods
                        all_list.append(line.split(',')[3])
                        all_list.append(line.split(',')[4])
                        all_list.append(float(line.split(',')[1]))
                        all_list.append(float(line.split(',')[2]))
                        all_list.append(float(line.split(',')[5]))
                        all_list.append(float(line.split(',')[6]))
                        all_list.append(float(line.split(',')[7]))
                        all_list.append(float(line.split(',')[8]))
                        all_list.append(float(line.split(',')[9]))
                        all_list.append(float(line.split(',')[10]))
                        all_list.append(float(line.split(',')[11]))
                        all_list.append(float(line.split(',')[12]))
                        all_list.append(float(line.split(',')[13]))


                #append the instance of City to the Cities list
                City.Cities.append(self)
                City.Cities_instances_attributes.append(all_list)
                
                
                
                #close the CityPop.csv
                fileinput.close()
                #assign the value of All_City_Attributes to the dictionary that stores the values for every city in CityPop.csv
                self.All_City_Attributes = City.allAtt_Dict

                #assigns the list of attributes for a particular instance
                self.List_Instance_Attributes = all_list
                
                #if you want all the attributes for all instances of Class City entered by the user
                self.List_AllInstances_Attributes = City.Cities_instances_attributes
            except:
                print 'Sorry there was an error with your input or the csv file doesn\'t exists please check to make sure the file exists'
            
        
        #print City.Cities
        
        
    def printDistance(self, othercity):
        
        #assigns the value of othercity based on user input
        self.othercity = othercity

        #the list that stores the particular values for the City the user entered
        testList = []
        
        #appends the values for other particular city the user is interested in by pulling all the values from the dictionary
        try:
            testList.append(City.allAtt_Dict[self.othercity])
            #print testList

            #assigns the latitude and longitude coordinates for each of the two cities
            #the othercity value has to have its latitude and longitude coordinate values converted from a string datatype
            #to a numeric data type in order for the calculations to be made
            lat_POI1 = math.radians(self.latitude)
            lat_POI2 = math.radians(float(testList[0][0]))
            lon_POI1 = math.radians(self.longitude)
            lon_POI2 = math.radians(float(testList[0][1]))

            #variable d stores the values for the great circle distance equation
            d = math.acos(math.sin(lat_POI1) * math.sin(lat_POI2) + math.cos(lat_POI1) * math.cos(lat_POI2) * math.cos(lon_POI1 - lon_POI2))

            #answer converts d to a distance in Kilometers
            answer = 6300 * d

            #print the answer back to the user
            print answer
        except:
            print "Sorry please try again."

    def printPopChange(self, year1, year2):
        
        if type(year1) == int and year1%5 == 0 and type(year2) == int and year2%5 == 0 and year1 >= 1970 and year1 <= 2010 and year2 >= 1970 and year2 <= 2010:
        #checks to make sure the user entered the years in the proper order in order
        #to get the proper values for the population change
            if year1 < year2:
                self.year1 = year1
                self.year2 = year2
            elif year1 > year2:
                self.year1 = year2
                self.year2 = year1

            
        #pulls the baseline year based on the list defined in the __init__ method
            if self.year1 == 1970:
                baseline = self.List_Instance_Attributes[4]
            elif self.year1 == 1975:
                baseline = self.List_Instance_Attributes[5]
            elif self.year1 == 1980:
                baseline = self.List_Instance_Attributes[6]
            elif self.year1 == 1985:
                baseline = self.List_Instance_Attributes[7]
            elif self.year1 == 1990:
                baseline = self.List_Instance_Attributes[8]
            elif self.year1 == 1995:
                baseline = self.List_Instance_Attributes[9]
            elif self.year1 == 2000:
                baseline = self.List_Instance_Attributes[10]
            elif self.year1 == 2005:
                baseline = self.List_Instance_Attributes[11]
            elif self.year1 == 2010:
                baseline = self.List_Instance_Attributes[12]

            #defines the second year based on the list for the particular city instance
            #that was defined in the __ini__ method
            if self.year2 == 1975:
                year_calc = self.List_Instance_Attributes[5]
            elif self.year2 == 1980:
                year_calc = self.List_Instance_Attributes[6]
            elif self.year2 == 1985:
                year_calc = self.List_Instance_Attributes[7]
            elif self.year2 == 1990:
                year_calc = self.List_Instance_Attributes[8]
            elif self.year2 == 1995:
                year_calc = self.List_Instance_Attributes[9]
            elif self.year2 == 2000:
                year_calc = self.List_Instance_Attributes[10]
            elif self.year2 == 2005:
                year_calc = self.List_Instance_Attributes[11]
            elif self.year2 == 2010:
                year_calc = self.List_Instance_Attributes[12]

            #print the answer back to the user
            print year_calc - baseline
        else:
            #if the user doesn't enter a valid input then this error message is printed on screen
            print "Sorry but please enter a valid input for both years."

       
