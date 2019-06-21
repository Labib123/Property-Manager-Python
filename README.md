# Property-Manager-Python
 This application keeps track of a property manager’s daily operations . 

The first file named propertyApp.py, contains the following two classes:
• The first is a class called Property which defines a simple object type representing a
property which is put up for sale.
• The second class called PropertyList defines objects which are containers of
Property objects.
• The second file named propertyDriver.py defines a Python application, with main
method, which creates one PropertyList object and allows the various methods of
Property to be called. This class will be an interactive application using the keyboard
and the screen to interact with a human operator. It will not do calculations itself but will
immediately pass user inputs as arguments to methods of PropertyList class. 

The PropertyList class has a group name (of type string), and a collection of
Property objects, no additional attribute is required one enough. The PropertyList must also contain
some methods which allow the collection of properties to be managed. The methods of class
PropertyList should include:
1. An initialiser (constructor) (__init__) with one parameter of type string, which is used to
initialise the group’s name. The constructor also initialises an empty list for storing
properties up for sale.
2. Getter (reader) methods for accessing the attributes, name and the property list.
3. A method named addProperty which accepts a parameter of Property object. This
method will store a reference to this Property object into the list
4. A method named noOfProperties which returns the number of Property objects
currently stored in the list.
