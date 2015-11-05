######### - O'Reilly - Python Beyond the Basics - ######### 
######### - Object-Oriented Programming - ######### 


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Classes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Class: a blueprint for an instance
# Instance: a constructed object of the class
# Type: Indicates the class the instance belongs to
# Attribute: Any object value: object.attribute
# Method: a "callable attribute" defined in the class

# Every instance of a particular class is expected to have the same attributes.

# A method is a function defined in the class that can be used by the instance

class MyClass(object):
	pass

this_obj = MyClass()
print this_obj
<__main__.MyClass object at 0x1007d3e90>

that_obj = MyClass()
print that_obj
<__main__.MyClass object at 0x1005e5110>

# This way we can see that we created objects from the class, and that they are two different ones because they occupy different hex-code.

class MyClass(object):
	var = 10

this_obj = MyClass()
that_obj = MyClass()
print this_obj.var
print that_obj.var
<10>
<10>
# We can access to the class variables from every instance of that class


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Instance Methods ~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Joe(object):
	def callme(self):
		print('calling "callme" method with instance: ')

thisjoe = Joe()
thisjoe.callme()

# Instance methods are variables defined in the class, access through the instance instance.method()
# When called through the instance, the instance is automatically passed as 1st argument to the method
# Instance methods are known as "bound methods" 


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Instance Attributes ~~~~~~~~~~~~~~~~~~~~~~~~~~~

import random

class MyClass(object):
	def dothis(self):
		self.rand_val = random.randint(1,10)

myinst = MyClass()
myinst.dothis()
print(myinst.rand_val)

# Self: is the instance upon which the method was called (myinst in this case)
# We have seen that an instance can access variables defined in the class
# But an instance can also get and set values in itself
# Because these values change according to what happens to the object, we call this values "State"
# Instance data takes the form of instance attributes values, set and accessed through object.attribute syntax

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Encapsulation ~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MyClass(object):
	# The function set_val will take the argument and set it as an attribute in the instance, under an attribute called value
	# It is a setter method, because it sets a value in the instance
	def set_val(self, val):
		self.value = val  #Instance attribute

	# This is a getter method
	def get_val(self):
		return self.value

a = MyClass()
b = MyClass()

a.set_val(10)
b.set_val(100)
# We can access the attribute in the object and change the value:
a.value = 'hello'
# But creating the method to set the value, we can ensure the integrity of the instance attribute and maintain the encapsulation

print(a.get_val())
print(b.get_val())

# The instance is being passed as the implicit first argument

### ENCAPSULATION ###
# It's the first of the three pillars of OOP
# Encapsulation refers to the safe storage of data (as attributes) in an instance.
# Data should be accessed only through instance methods
# Data should be validated as correct (depending on the requirements set in class methods)
# Data should be safe from changes by external processes
### Breaking Encapsulation ###
# Although normally set in a setter method, instance attribute values can be set anywhere
# Encapsulation in Python is a voluntary restriction
# Python does not implement data hiding, as does other languages

# ~~~~~~~~~~~~~~~~~~~~~~~~ The __init__ Constructor ~~~~~~~~~~~~~~~~~~~~~

# It's a special methods that allows us to initialize attributes at the time that an instance is constructed
# As we've seen attributes are traditionally set using a setter method, but what if we want some to be created right at the beginning, before an instance is created? 
# This can be done in the constructor
# Init is called automatically any time a new instance is constructed
# Like any other instance method, inti has a self in its argument list this is actually the first appearance of the instance, it hasn't exactly been passed anywhere, but because it's an instance method, it's present, and it's present of course because we are going to modify in the initialization, we will be setting its attributes. And by initializing an object, we mean setting attributes or doing any preparatory work that is necessary when creating a new instance

class MyNum(object):
	def __init__(self):
		print 'calling __init__'
		self.val = 0

	def increment(self):
		self.val = self.val + 1

dd = MyNum()    # calling __init__
dd.increment()
dd.increment()

print dd.val    # 2

# Another option
class MyNum(object):
	def __init__(self, value):
		# we add an integrity gate, and if it isn't and integer, which is what we really needed the attribute to be, we capture the error and set the value to 0 which is what goes into the attribute. Otherwise, we accept the value as correct, if it can be integerize.
		try:
			value = int(value)
		except ValueError:
			value = 0
		self.val = value
	
	def increment(self):
		self.val = self.val + 1

aa = MyNum('hello')        #calling __init__
bb = MyNum(100)
aa.increment()
aa.increment()
bb.increment()
print aa.val
print bb.val

# __init__ is a keyword variable: it must be named init
# It is a method automatically called when a new instance is constructed
# If it is not present, it is not called
# The self argument is the first appearance of the instance
# __init__ offers the opportunity to initialize attributes in the instance at the time of construction

# ~~~~~~~~~~~~~~~ Class Attributes vs. Instance Attributes ~~~~~~~~~~~~~~~~

# The variables defined in the class as well as attributes set in the object, are both accessed through the instance using object.attribute

class YourClass(object):
	classy = 10		# class variable (a variable set in the class)

	def set_val(self):
		self.insty = 100 # attribute set in the instance

dd = YourClass()
dd.set_val()
print(dd.classy) # the instance has access to both, the class variable and its attribute
print(dd.insty)

# There is an attribute lookup order, first in the instance and then in the class

# Attributes / variables in the class are accessible through the instance
# Instance attributes are also accessible by the instance
# When we use the syntax object.attribute, we're asking Python to look up the attribute:
# First in the instance
# Then in the class
# Methods calls through the instance follow this lookup

################ - 6 POINTS TO UNDERSTANDING CLASSES - ######################

# An instance of a class knows what class it's from
# Vars defined in the class are available to the instance
# A method on an instance passes instance as the first argument to the method (named self in the method)
# Instances have their own data, called instance attributes
# Variables defined in the class are class attributes
# When we read an attribute, Python looks for it first in the instance, and then in the class 

# ~~~~~~~~~~~~~~~ Working with classes and instance data ~~~~~~~~~~~~~~~

class InstanceCounter(object):
	count = 0 # class attribute (accessible through any instance created from the class). It's a global variable

	def __init__(self, val):
		self.val = val # instance attribute set in the instance
		InstanceCounter.count += 1 # class.attribute

	def set_val(self, newval):
		self.val = newval

	def get_val(self):
		return self.val

	def get_count(self):
		return InstanceCounter.count

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
	print "val of obj: %s" % (obj.get_val())  # initialized value (5, 13,..)
	print "count: %s" % (obj.get_count())   # always 3


# Any variable set in the class needs to be accessed using object.attribute syntax, In this case we use the class object to access to the variable count, because it is a class variable.
# Classes are objects too 

################ - INHERITANCE AND POLYMORPHISM - ######################

# ~~~~~~~~~~~~~~~~~~~~~ Inheriting Attributes ~~~~~~~~~~~~~~~~~~~~~~~~~

# The ability to have one class inheriting the attributes of another class. In every case, python will follow a lookup order to try to find an attribute


# Object.Attribute Lookup Hierarchy
# - The instance
# - The class to which the instance belongs
# - Any class from which this class inherits 

# Some Inheritance Terms:

# * An inheriting class ----> class MyClass(YourClass):
# - Child Class
# - Derived Class
# - Subclass

# * An inherited class ----> class YourClass(object):
# - Parent Class
# - Base Class
# - Superclass

# ~~~~~~~ Inheritance: The second pillar of OOP ~~~~~~~~~
# One class can inherit from another:
# - The class' attributes are inherited
# - In particular it's methods are inherited 
# - This means that instances of an inheriting (child) class can access attributes of the inherited (parent) class
# - This is simple another level of lookup:
# Instance, then class, then inherited classes

class Animal(object):
	def __init__(self, name):
		self.name = name
	def eat (self, food):
		print '%s is eating %s' % (self.name, food)

class Dog(Animal):
	def fetch(self, thing):
		print '%s goes after the %s' % (self.name, thing)

class Cat(Animal):
	def swatstring(self):
		print '%s shreds the strings!' % (self.name)

r = Dog('Rover')
f = Cat('Fluffy')

r.fetch('paper')
f.swatstring()
r.eat('dog food')
f.eat('cat food')


########################### - POLYMORPHISM - ###########################

# The third pillar of OOP
# Two classes with some interface (ie method name)
# The methods are often different, but conceptually similar
# Allows for expressiveness in design: we can say that this group of related classes implement the same action 
# Duck typing refers to reading an object's attributes to decide whether it is of a proper type, rather than checking the type itself

class Animal(object):
	def __init__(self, name):
		self.name = name

	def eat (self, food):
		print '{0} is eating {1}'.format(self.name, food)

class Dog(Animal):

	def fetch(self, thing):
		print '{0} goes after the {1}'.format(self.name, thing)

	def show_affection(self):
		print '{0} wags tail'.format(self.name)


class Cat(Animal):
	def swatstring(self):
		print '{0} shreds the strings!'.format(self.name)

	def show_affection(self):
		print '{0} purrs'.format(self.name)

for a in (Dog('Rover'), Cat('Fluffy'), Cat('Precious'), Dog('Scout')):
	a.show_affection()

# >>> Rover wags tail
# >>> Fluffy purrs
# >>> Precious purrs
# >>> Scout wags tail

# We are calling the same method and obtaining different results, we use this method on an animal without having to worry about what kind of animal we are dealing with.

# Being able to work with different types to call methods without checking that is possible ahead of time, and handling error using exceptions handling, is called duck typing (If it walks like a duck, and it ducks like a duck, it must be a duck)
# We generally do what we want to do, and then trap errors as they occur 

# Python itself, has classes that are polymorphic. The len function can be use with multiple objects: strings, lists, tuples, dictionaries and sets. Thew truth is, build in functions, we are allow to use them as build in functions, because its convenient for us, but when we do use build in functions they translate into a method called on the objects being passed

# >>> var = 'hello'
# >>> len(var)    -> 5
# >>> var.__len__()   -> 5


# ~~~~~~~~~~~~~~~~~~~~ Inheriting the Constructor ~~~~~~~~~~~~~~~~~~~~~~~~

# ~ How and why we may inherit a constructor from the parent class in addition to any constructor we may want to have in our own class. In our first Animal example, init was located in the parent class, because the child class, Dog, didn't have an init method. Python uses the inheriting attribute lookup, to find init in the animal class (Dog), if it cant find it, then look in Animal, and call it there.
# As our class design become complex, we may wish to initialize an instance, by first processing it though the parent class constructor, and then through the child constructor

class Animal(object):
	def __init__(self, name):
		self.name = name

class Dog(Animal):
	def __init__(self, name):
		Super(Dog, self).__init__(name)
		self.breed = random.choice(['Shih Tzu', 'Beagle', 'Mutt'])

	def fetch(self, thing):
		print '%s goes after the %s' % (self.name, thing)

d = Dog('dogname')

print d.name  ---> dogname
print d.bread ---> Shih Tzu

# Here we are giving all animals a name, and our dogs, a particular dog's breed. We call a parent class constructor with super, so now Dog has it own init, but the first thing that happens is we call super. Super is a build in function, and its designed to relate a class to its superclass or its parent class. In this case we are saying: get the superclass of Dog and pass the Dog instance to a certain method (in this case init)

# ~ __init__ is like any other method; it can be inherited
# ~ If class does not have an __init__ constructor, Python will check it's parent class to see if it can find one
# ~ As soon as it finds one, Python calls it and stops looking
# ~ We can use the super() function to call methods in the parent class
# ~ We may want to initialize in the parent as well, as our own class


######################## - MULTIPLE INHERITANCE - ###########################

# http://i.imgur.com/FR0v2Bf.png

#The method resolution order will be D-B-A-C, this means that Python will depth first, and breadth second

class A(object):
	def dothis(self):
		print 'doing this in A'

class B(A):wakaw
	pass

class C(object):
	def dothis(self):
		print 'doing this in C'

class D(B,C):
	pass

d_instance = D()
d_instance.dothis()

print D.mro()

# --> [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <type 'object'>]

# However things get more complicated if the same class appears in two other classes inheritance list, which creates an ambiguous order

# http://i.imgur.com/NdVFRPg.png

# The way Python handles ambiguity is to remove early appearances of multiple referred to classes, in other words: A.
# So the depth-first tree will say D-B-A-C-A, but because A is repeated it removes the earlier occurrence of A, so the method resolution order in a diamond shape pattern is D-B-C-A

class A(object):
	def dothis(self):
		print 'doing this in A'

class B(A):
	pass

class C(A):
	def dothis(self):
		print 'doing this in C'

class D(B, C):
	pass

d_instance = D()
d_instance.dothis()

print D.mro()

# --> [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>]

# Any class can inherit from multiple classes
# Python normally uses a "depth-first" order when searching inheriting classes
# But when two classes inherit from the same class, Python eliminates the first mention of that class from the mro (method resolution order)
# The above applies to "new style" classes (inheriting from object)

############## Decorators, Static And Class Methods ########################


# - A class method takes the class (not instance) as argument and works with the class object

# - A static method requires no argument and does not work with the class or instance (but it still belongs to the class code)

# - A decorator is a processor that modifies a function

# - @classmethod and @staticmethod modify the default binding that instance method provides

# In this lesson we will look at two special kind of methods, that are alternatives to the methods we have seen so far. The methods that we've seen so far are called instance methods, because they are designed to work in the instance.
# Here is an example:

class InstanceCounter(object):
	count = 0

	def __init__(self, val):
		self.val = val
		InstanceCounter.count += 1

	def set_val(self, newval):
		self.val = newval

	def get_val(self):
		return self.val

	def get_count(self):
		return InstanceCounter.count

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
	print 'val of obj: %s' % (obj.get_val()) # initialized value (5, 13, etc.)
	print  'count: %s' % (obj.get_count()) # Always 3


# how do I know they are instance methods? Because the instance is the first argument to each one of them, and this is an automatic behavior when calling a method on an object. The object, the instance get passed automatically to an instance method, and because of this automatic passing, we sometimes call, instance methods bound methods, and that is because the instance is bound to the method, it works with the method, and this is often useful when we want to modify the object, that is set a value, or get a value.
#The new special method that we are going to look at in this lesson, are called class methods and static methods, and they are not bound to the instance.
# and if you think about it, a class is really a library of functionality that is associated with the instances that it produces, but some of the functionality may not actually have to with the instance itself, some of the functionality may be related to the class itself, dealing with class data, for example, the InstanceCounter count attribute, or we might even have some methods that are just utility methods that are not designed to work with the class or the instance, so that's why we might want to have this other kind of methods, which we call class methods, for working with the class, and static methods to work independently of either the class or the instance.

# So let's look at the get_count method, it take the instance as the first argument and that is automatically passed, so it's a bound method, it's and instance method
# What are we doing in this instance method? For each of the three instances that we created, we passed an integer to each one of them, we are getting the value that is stored in the instance and we are also calling get_count on each of the instances, so what get_count do? We have the value of the object stored in the instance, that's from get_val, and that was the value that we set in the constructor, but count is 3 for each one of them, because return Instance Counter.count is returning something that happens up in the __init__ method, and it is incrementing a value for each time we create an instance, so the instance is not coming into play. So this is where the class method comes in, the method that is intended to work with the class as get_count does.
# What we can do is, replace self with cls, now the label itself doesn't make a difference, with this we haven't really affected the functionality of the method. it's still a bound method and we are still going to see the instance assigned to cls. We can't use the word class because it's reserved for defining a class, so what we will do change the method into a class method, is put a special modifier above the method in question, this is what we call a function or method decorator
f
# ~ A decorator is a special function that can modify functions. If we apply the class method decorator to a method, we can cause that method to pass the class automatically when called, instead of the instance.

class InstanceCounter(object):
	count = 0

	def __init__(self, val):
		self.val = val
		InstanceCounter.count += 1

	def set_val(self, newval):
		self.val = newval

	def get_val(self):
		return self.val

	@classmethod   # <--------------|
	def get_count(cls):
		return cls.count

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
	print 'val of obj: %s' % (obj.get_val()) # initialized value (5, 13, etc.)
	print  'count: %s' % (obj.get_count()) # Always 3

# Its important that we make sure that our code is as logically designed as possible, because if we leave this as an instance method, it implies that we intend to work with the instance, but that's definitely not the case when it come to get_count, so it's absolutely correct to make this into a class method, because it work with the class
# Now we can use the class object, that is now being passed to get count, as the object from which we will read the count attribute. Now is very clear, from reading this code, that I intended to work with a class attributes, and count of course, is a class attribute, it would have been misleading to keep it as instance attribute, even if it does work the same way
# In addition I can use the class itself to call the method and this should work as well:


print InstanceCounter.get_count()



# Another decorator that is available for us, is called Static Method


class InstanceCounter(object):
	count = 0

	def __init__(self, val):
		self.val = self.filterint(val)
		InstanceCounter.count += 1

	@staticmethod
	def filterint(value):
		if not isinstance(value, int):
			return 0
		else:
			return value

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

print a.val
print b.val
print c.val

# In this example we include a new decorator and a new method called filterint. filterint is being used in the constructor to make sure that the argument passed to the constructor is an integer
# Once the value goes from the constructor call up until the constructor its passed to the filterint method, which takes the value and makes sure that it is an integer. It has to be of the type integer and that's what isinstance is doing. If it is, the value will be returned and then it will be assigned to the attribute val, but if it is not, it will return 0, which means that if we attend to set a bad value in the attribute, we will see 0 instead.

# The reason we decorated filterint with the static method decorator it's because it's neither a class method, which will work with the class, or an instance method, which will work with the instance, instead it's just and utility class, it belongs in the class code because it works with the class code, but it's neither an instance nor a class method, so we make it a static method
# Notice that self is missing, and the value that gets passed, is simply passed directly, with no implicit argument added, in other words, it's not a bound method, it's a static method

# We could have made it an instance method, and it wouldn't really have been a problem to do so, but once again, we don't want to be misleading. If the method is intended to be just an utility method, and it doesn't need the instance to work, we shouldn't be implying that it does, which is what an instance method really does, instead we will use static method, and now the method doesn't require any implicit argument at all


####################### Abstract Base Classes ################################

# - An abstract class is a kind of 'model' for other classes to be defined. It's not designed construct instances, but can be subclasses by regular classes
# - Abstract classes can define an interface, or methods that must be implemented by it's subclasses
# - The python abc module enables the creating of abstract base classes


# When we are working in a collaborative environment with other developers who are creating classes that will fin into a larger hierarchy we may want to define a class that indicates and enforces what methods a subclass should implement, and we will call this, an abstract class


import abc 

class GetterSetter(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def set_val(self, input):
		"""Set a value in the instance"""
		return

	@abc.abstractmethod
	def get_val(self):
		"""Get and return a value from the instance"""
		return


# If we were working on a team, or we would have designed a library that requires other members to contribute classes, we may wanna to require that the developers implements certain methods. In this example we have a class that gets a value and gets a value, if that's the basic interface that we like other developers to implement we can ask them to subclass or inherit from our class, and we want to declare our methods in such a way that defining this methods is required in any subclass

# The abc module imported here provides facilities for creating abstract base classes, which are classes that are not designed to be instantiated but only to be subclass, in other words, we don't create a GetterSetter instance, we are only going to inherit from GetterSetter  

# One way of create an abstract base class is to make use of a __metaclass__, which is basically a class that can define another classes. Basically, when we assign ABCmeta to the __metaclass__ magic attribute, we are basically saying that this should be defined as an abstract base class.
# Then above each of the methods, we placed a decorator, indicating that this methods are abstract methods. 

# Now we've created the template from which other classes that subclass GetterSetter, will have to follow, so let's subclass GetterSetter:

class MyClass(GetterSetter):

	def set_val(self, input):
		self.val = input

	def get_val(self):
		return self.val

x = MyClass()
print x

# If we omit any of this methods, or use a different name, python will give us an error

# GetterSetter can't be instantiated 

############## Method Overloading - Extending and providing ###################


# ~~~~~~~~~~~~~~~~~~~ Inheritance Examples ~~~~~~~~~~~~~~~~~~~

# When working in a child class we can choose to implement parent class methods in different ways:
# - Inherit: simply use the parent class defined method
# - Override/overload: provide child's own version of a method
# - Extend: do work in addition to that in parent's method
# - Provide: implement abstract method that parent requires 

import abc 

class GetSetParent (object):

	__metaclass__ = abc.ABCmeta

	def __init__(self, value):
		self.value = 0

	def set_val(self, value):
		self.val = value

	def get_value(self):
		return self.val

	@abc.abstractmethod
	def showdoc(self):
		return

# 1st child class

class GetSetInt(GetSetParent):

	def set_val(self, value):
		if not isinstance(value, int):
			value = 0
		super(GetSetInt, self).set_value(value) # this means it's going to look for the superclass of GetSetInt, call set_val and pass the instance as an argument, we just call the parent 

	def showdoc(self):
		print('GetSetInt object {0}, only accepts '
			'integer values'.format(id(self)))

# This is called specializing, the set_val method in GetSetInt is specializing the set_val method in GetSetParent, it's making use of the behavior in both 
# The we are implementing the showdoc method because it's required in each child class inheriting from GetSetParent, show doc is simply designed to explain what this class is all about, and this print statement is showing the instance's id, which is an identifying value, specific to this instance as well as explaining what the instance is used for

###################### -  COMPOSITION VS INHERITANCE - ########################

# In this lesson we are going to look at another approach of working with classes, and an alternative to inheritance. It's called Class Composition
# The inheritance approach can lead to unnecessary restrictions, as it establishes dependency between child and parent classes.
# We refer to this approach as brittle, because one change in one part of the code can easily break it.

# The basic concept behind composition is to use two or more classes that are not related by inheritance but they can work together.

import random
import StringIO

class WriteMyStuff(object):
	def __init__(self, writer):
		self.writer = writer

	def write(self):
		write_text = "this is a silly message"
		self.writer.write(write_text)

fh = open('test.txt', 'w')
w1 = WriteMyStuff(fh)
w1.write()
fh.close()

sioh = StringIO.StringIO()
w2 = WriteMyStuff(sioh)
w2.write()

print 'file object: ', open('test.txt', 'r').read()
print 'StringIO object: ', sioh.get_value()

# So look how we are using the code, we are creating a file object and then passing ti to WriteMyStuff, also we are creating a StringIO object and also passing it to WriteMyStuff , and then later on the WriteMyStuff object, we are calling write.
# How does WriteMyStuff works? 
# The init method simply accept the writer object, as is the file object or the StringIO object, and store it in the object under the attribute writer, then when we call write, it takes that writer, whatever it happens to be, and calls write on it.
# Notice that it doesn't check type, it simply assumes that it can call the right method on that object, a very polymorphic behavior.
# So this is an example of composition, the chief advantage here is modularity, it really doesn't matter what type of object get sent up to the WriteMyStuff constructor. In fact, we could create our own class that produces objects that support the right method, our own class could be write into a data base, to a network connection, it could be sending a request over the web, it doesn't really matter to the WriteMyStuff class, because it is simply taking whatever we sent and calling write on it, again polymorphic behavior.

# The different objects that we are working with are decoupled, they don't depend in one another, they are aware of each other interface though, and that's really the key. As long as the interface stay the same on any of this objects, WriteMyStuff can work with it.
# So we can make changes to any of this classes, internal changes won't make a difference to WriteMyStuff as long as we can call write.
# So the benefit here is that we don't have to worry about a class hierarchy, we don't have to ask how a class will affect another if we make a change, instead we just keep in mind the interface that we need to use and we can use this classes together.

# ~ The Composition approach uses independent classes, they work together but they are not related in a particular way. There is a word sometimes used when discussing design: Decoupling which refers to allow elements to be interactive, but essentially independent.

# ~ Inheritance can be brittle (a change may require changes elsewhere)
# ~ Decoupled code is classes, functions, etc. that work independently and don't depend on one another
# ~ As long as the interface is maintained, interactions between classes will work
# ~ Not checking or requiring particular types is polymorphic and Pythonic














