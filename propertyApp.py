#Labib Mansour #B1801314
class Property:
    # declare a magic method ( constructor ) to and takes 4 parameters
    def __init__ (self,location='',price=0.0,ptype='', size=0): # assigning value to determine the data type
        self.__location = location
        self.__price = price
        self.__ptype = ptype
        self.__size = size
    # if conditions to determine Type string although i did create a method for doing that  as you can see below
        if self.__ptype.lower() == 'a':
            self.__ptype =   'apartment'
        elif self.__ptype.lower() == 'b':
            self.__ptype =  'bungalow'
        elif self.__ptype.lower() == 'c':
            self.__ptype = 'condominium'
# simple getter method
    def getLocation(self):
        return self.__location
    def getPrice(self):
        return self.__price
    def getType(self):
        return self.__ptype
    def getSize(self):
        return self.__size
#simple setter methods
    def setLocation(self,location):
        self.__location = location
    def setPrice(self,price):
        self.__price = price
    def setType(self,type):
        self.__ptype = type
    def setSize(self,size):
        self.__size = size
# method type string to determine the type of property based on first character
    def typeString(self):
        if self.__ptype.lower() == 'a':
            self.__ptype =   'apartment'
            return  self.__ptype
        elif self.__ptype.lower() == 'b':
            self.__ptype =  'bungalow'
        elif self.__ptype.lower() == 'c':
            self.__ptype = 'condominium'
# annual tax method which clalculates the tax based on the type
    def annualTax(self):
        if self.__ptype == 'apartment':
            return  self.__price * 0.025
        elif self.__ptype == 'bungalow' :
            return self.__price * 0.045
        elif self.__ptype == 'condominium':
            return  self.__price  * 0.035
# __eq__ magic method wich returns True if two properties are equal and False if are not equal
    def __eq__(self,property20):
        if self.__location == property20.__location and self.__size == property20.__size and self.__ptype == property20.__ptype :
            return 'True'
        else:
            return "False"
# __lt__ is a magic method which returns True if first property is less than second property
    def __lt__(self,property3):
        if self.__size > property3.__size:
            return  True
        else :
            return False
# __le__ is a magic method which return True if first property is less than or equal second property
    def __le__(self,property4):
        if property4.__size <= self.__size :
            return  True
        else :
            return  False
# __str__ is a magic method which returns a single string containing the details of a property
    def __str__(self):
         string = self.__ptype  + ', ' + str(self.__size)  + ' square feet , ' + 'At ' + self.__location + ', Costing '  +  str(self.__price )
         return  (string)


# The main reason of creating this Class is to provide list to store Property Data
class PropertyList  :
    # A magic method takes on parameters and initilaze an empty list
    def __init__(self,name):
        list1 = []
        self.__name = name
        self.__list1 = list1
# get method for Name parameter
    def getName(self):
        return  self.__name
# getter for the list
    def getPropertyList(self):
        return self.__list1
# setter for name
    def setName(self,name):
        self.__name = name
# The main function of this method is to add property to the list
    def addProperty(self,property):
        self.__list1.append(property)
        return  self.__list1
# The main function of this method is to count the property inside the list by using len()
    def noOfProperties(self):
        return  len(self.__list1)

    def allProperties(self):
        porpertyList = self.__list1
        # initialize an empty string
        AllProperties = ''
        # for each loop to store the data inside the empty string
        for  property in porpertyList:
            AllProperties += str(property) + '\n'
        return  AllProperties
    def totalPrice(self):
        # initialize an empty integer
        total = 0
        # for loop for getting the price
        for p in self.__list1:
            total += p.getPrice()
        return "Total price : ${:.2f} ".format(total)
            #print( total)


    def mostExpensiveProperty(self):
        highest_price = 0
        highest_Property = 0
        for x in self.__list1:
            if highest_price < x.getPrice():
                highest_price = x.getPrice()
                highest_Property = x
        return  highest_Property
# method takes one parameter represents the type to find the its information
    def findPropertyByType(self,ptype):
#  these if statements in order to provide the user shortcuts
        for e in self.__list1:
            if ptype.lower() == 'a':
                ptype = 'apartment'
            elif ptype.lower() == 'b':
                ptype = 'bungalow'
            elif ptype.lower() == 'c':
                ptype = 'condominium'
# if statement to retrive the information
            if ptype == e.getType():
                myString = "Price = {}, Size = {}, Location = {} ".format(e.getPrice(), e.getSize(), e.getLocation())
                print(myString)
    def sellProperty(self,location):
# try and except method to avoid broking the program due the user fault
        try:
            # delete the property by using indexing
            self.__list1.pop(location)
        except  (IndexError , ValueError , OverflowError) as error :
             print('OUT OF RANGE , \nPLEASE TRY AGAIN  ')
            # this method retrieves sorted data based on users' criteria
    def sortedProperties(self,criteria):
        list2 = []
        if criteria == 'price' :
            # using a lambda to sort the data based on attribute
            self.__list1.sort(key=lambda r:r.getPrice()  )
            list2.extend(self.__list1)
            for item in list2 :
                print(str(item) + '\n')
        elif criteria == 'tax':
            self.__list1.sort(key=lambda r: r.annualTax() )
            list2.extend(self.__list1)
            for item in list2:
                print(str(item) + '\n')
        elif criteria == 'size':
            self.__list1.sort(key=lambda r: r.getSize())
            list2.extend(self.__list1)
            for item in list2:
                print(str(item) + '\n')

    def saveToFile(self,FileName):
        # Normal file funtion to create file or Write on it
        file =  open(FileName, 'w' )
        # For loop in order to store the data
        for pro in self.__list1:
            file.write(str(pro) + '\n')
        file.close()


        # Normal file function to load file
    def loadFromFile(self,LfileName):
        # Try and except in order to avoid breaking the program due users' mistakes
        try:
            # Lfile which means Load File
            Lfile = open(LfileName , 'r')
            for line in Lfile:
                self.__list1.append(line)
            Lfile.close()
        except FileNotFoundError:
            print('\nFile is not found , Please try again and  ' )





# Virtual instance to use it in propertyDriver , i will delete it from the list in the next file
# therefore it won't effect on the program , by contrary , program will be easier
prop6= Property('',5000,'a',0)
prop2 = PropertyList('name')
prop2.addProperty(prop6)
prop2.sellProperty(0)

