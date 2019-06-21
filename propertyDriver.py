# Import everything from propertyApp File
from propertyApp import *

# Delete the instance
# prop2.sellProperty(0)
# save the name of company
company = input("What's the name of your property company?")
def main():
    # While True ( While without )
    while True:
        # assign menu to choice
        Userchoice = menu()
        interface = prop2

        # If statement to determine what does each choice represent

        if Userchoice ==  1 :
            addproperty(interface)
        elif Userchoice == 2  :
            allProperties(interface)
        elif Userchoice == 3  :
            getPropertyList(interface)
        elif Userchoice== 4 :
            findPropertyByType(interface)
        elif Userchoice == 5 :
            sellProperty(interface)
        elif Userchoice == 6:
            sortedProperties(interface)
        elif Userchoice == 7:
            loadFromFile(interface)
        elif Userchoice == 8 :
            saveToFile(interface)
        elif Userchoice == 0 :
            print('Sayonara...')
            break
            # Try and except statement to avoid breaking the program
        try:
            # if statement to print an Error message if the user goes out of the range
            if Userchoice > 8:
                print('\nPlease type a number that represents a choice \n')
        except TypeError:
            print('\nPlease type a number that represents a choice \n')


def menu():
# User interface menue
    print (str(company))
    print ( '-' * 25 )
    print('1 Add a property')
    print('2 Display all properties')
    print('3 Display summary information about property list')
    print('4 Display properties with user-specified type')
    print('5 Sell a property based on given index')
    print('6 Display all properties, sorted according to Property values')
    print('7 Read properties information from file')
    print('8 Write properties information to file')
    print('0 quit')
    try : # to avoid breaking the app 
        option = int(input('Your choice:'))
        return  option
    except ValueError :
        print('\nPlease type a number that represents a choice \n')

# Method to handle with adding property interface which allows the user to add properties
def addproperty(interface1):
    print('Adding a new property')
    location = input('Location:')
    price = input('Price:')
    Property_type = input("Property type ('A'partmen, 'B'ungalow, 'C'ondominium)")
    Size = input('Size (in square feet, eg. 1438):')
    Psample = Property(location,float(price),Property_type,Size)
    interface1.addProperty(Psample )
    # prop2 to is and virtual instance

    print('... added successfully.')


# method which allows the user to show all Properties in the list
def allProperties(interface1):
    print('Details of all properties:')
    print(interface1.allProperties())
    if interface1.noOfProperties() == 0 :
        print('No property has been registered yet')
# method which displays summary information about property such as number of properties and most expensive property
def getPropertyList(interface1):
    print('Summary Information')
    print('Number of registered properties: : ' + str(interface1.noOfProperties()))
    print( interface1.totalPrice() )
    print( 'Most expensive property: '  )
    print(interface1.mostExpensiveProperty())
# method provies console interface for the user to display the information based on specified type
def findPropertyByType(interface1):
    user = input("Property type ('A'partmen, 'B'ungalow, 'C'ondominium):")
    # If condition to print a message that tells the users No property for their type
    if interface1.findPropertyByType(user.lower()) == None :
        print ('No property of that specific type yet')
    else :
        print(interface1.findPropertyByType(user.lower()))
#method provides an interface for the user to choose an property to sell it (console interface)
def sellProperty(interface1):
    try :
        user = int(input('Property to sell ? ( 1 .. {} )'.format(interface1.noOfProperties())))
        UserInput = user - 1

        interface1.sellProperty(UserInput)


    except ValueError :
        print('PLEASE ENTER AN INTEGER NUMBER ')

def sortedProperties(interface1):
    user = input('- criteria (price, tax, or size)?')
    interface1.sortedProperties(user.lower())
def loadFromFile(interface1):
    user = input('File name to load from  ')
    interface1.loadFromFile(user)

def saveToFile(interface1):
    if interface1.noOfProperties() >= 1:
        user = input('File name to save to  :' )
        interface1.saveToFile(user)
    else :
        print('No property has been registered yet  ')
# to execute the program
main()



