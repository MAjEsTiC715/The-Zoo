#========================================================  Documentation  ==================================================================================
#Add polymorphism to your parent and child classes (subclasses) by adding __str__ functions.
#The __str__ function should print the parent attributes as well as the unique child attributes.
#The makeNoise() function of the Animal class will need to be overridden in each subclass. 
#The makeNoise function will need to print the sound the animal makes to the screen.
#All instantiated Animal objects should be stored in the Zoo list. 
#Traverse the Zoo list using a loop and have each animal polymorphically print its attributes and call the makeNoise function. 
#===========================================================================================================================================================

#create the parent class Animal
class Animal:

    #Initialize species, aType, age, and color for each animal
    def __init__(self, species, aType, age, color):
        self.species = species
        self.aType = aType
        self.age = age
        self.color = color

    #set the atrribute aType
    def set_aType(self, aType):
        self.aType = aType

    #set the atrribute age
    def set_age(self, age):
        self.age = age

    #set the atrribute color
    def set_color(self, color):
        self.color = color


    #get the atrribute aType
    def get_aType(self):
        return self.aType

    #get the atrribute age
    def get_age(self):
        return self.age

    #get the atrribute color
    def get_color(self):
        return self.color

    #create a stub function called show_species this calls the attribute it is assigned to 
    def show_species(self):
        print ('I am a', self.species)

    #create a stub function called make_sound
    def make_sound(self):
        print ('there is no animal')

#create the sub-class called Dog and inherit attributes from Animal
class Dog(Animal):

    #initialized all parent attributes along with some unique to the sub-class Dog including size and fur
    def __init__(self, species, aType, age, color, size, fur):
        Animal.__init__(self, species, aType, age, color)

        self.size = size
        self.fur = fur

    #set the atrribute size
    def set_size(self, size):
        self.size = size

    #set the atrribute fur
    def set_fur(self, fur):
        self.fur = fur

    #get the atrribute size
    def get_size(self):
        return self.size

    #get the atrribute fur
    def get_fur(self):
        return self.fur

    #create a stub function called show_species this calls the attribute it is assigned to 
    def show_species(self):
        print ('I am a', self.species)
        
    #create a stub function called make_sound, when this class is chosen it prints a statement
    def make_sound(self):
        print ('Woof! Woof!')
        print ('\n--------------------------------------------------------------------------\n')

    #create a __str__ function
    #this will reprint eveytime this subclass is chosen printing the different instances of that object
    def __str__(self):
        return '\n--------------------------------------------------------------------------\n' + \
                'I am a ' + self.size + ' sized ' + self.aType + ' dog \n' + \
                'My fur is ' + self.fur + '\n' +\
                'my age is: ' + format(self.age, '.0f') + '\n' + \
                'my color is: ' + self.color + \
                '\n--------------------------------------------------------------------------\n'

#create the sub-class called Snake and inherit attributes from Animal
class Snake(Animal):

    #initialized all parent attributes along with some unique to the sub-class Snake including length and if its harmful
    def __init__(self, species, aType, age, color, length, harmful):
        Animal.__init__(self, species, aType, age, color)

        self.length = length
        self.harmful = harmful

    #set the atrribute length
    def set_length(self, length):
        self.length = length

    #set the atrribute harmful
    def set_harmful(self, harmful):
        self.harmful = harmful

    #get the atrribute length
    def get_length(self):
        return self.length

    #get the atrribute harmful
    def get_harmful(self):
        return self.harmful

    #create a stub function called show_species this calls the attribute it is assigned to 
    def show_species(self):
        print ('I am a', self.species)
        
    #create a stub function called make_sound, when this class is chosen it prints a statement
    def make_sound(self):
        print ('Hisss')
        print ('\n--------------------------------------------------------------------------\n')

    #create a __str__ function
    #this will reprint eveytime this subclass is chosen printing the different instances of that object
    def __str__(self):
        return '\n--------------------------------------------------------------------------\n' + \
               'I am a ' + self.aType + ' and ' + format(self.length, '.2f') + ' feet in length \n' + \
               'I am ' + self.harmful + '\n' + \
               'my age is: ' + format(self.age, '.0f') + '\n' + \
               'my color is: ' + self.color + \
               '\n--------------------------------------------------------------------------\n'

#create the sub-class called Bird and inherit attributes from Animal
class Bird(Animal):

    #initialized all parent attributes along with some unique to the sub-class Bird including type of beak and feather length
    def __init__(self, species, aType, age, color, beak, featherL):
        Animal.__init__(self, species, aType, age, color)

        self.beak = beak
        self.featherL = featherL

    #set the atrribute beak
    def set_beak(self, beak):
        self.beak = beak

    #set the atrribute featherL
    def set_feather(self, featherL):
        self.featherL = featherL

    #get the atrribute beak
    def get_beak(self):
        return self.beak

    #get the atrribute featherL
    def get_feather(self):
        return self.featherL

    #create a stub function called show_species this calls the attribute it is assigned to 
    def show_species(self):
        print ('I am a', self.species)
        
    #create a stub function called make_sound, when this class is chosen it prints a statement
    def make_sound(self):
        print ('Chirp! Chirp!')
        print ('\n--------------------------------------------------------------------------\n')

    #create a __str__ function
    #this will reprint eveytime this subclass is chosen printing the different instances of that object
    def __str__(self):
        return '\n--------------------------------------------------------------------------\n' + \
               'I am an ' + self.aType + ' with a ' + self.beak + ' and ' + format(self.featherL, '.2f') + ' inch wings \n' + \
               'my age is: ' + format(self.age, '.0f') + '\n' + \
               'my color is: ' + self.color + \
               '\n--------------------------------------------------------------------------\n'

    
        
