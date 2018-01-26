#========================================================  Documentation  ==================================================================================
#Add polymorphism to your parent and child classes (subclasses) by adding __str__ functions.
#The __str__ function should print the parent attributes as well as the unique child attributes.
#The makeNoise() function of the Animal class will need to be overridden in each subclass. 
#The makeNoise function will need to print the sound the animal makes to the screen.
#All instantiated Animal objects should be stored in the Zoo list. 
#Traverse the Zoo list using a loop and have each animal polymorphically print its attributes and call the makeNoise function. 
#===========================================================================================================================================================

import Animal #import the class Animal

#define main as a function
def main():

    #create 2 instances named dog1 and dog2 these have attributes from the parent class as well as from its sublclss
    dog1 = Animal.Dog('Dog', 'Terrier', 14, 'brown', 'medium', 'fluffy')
    dog2 = Animal.Dog('Dog', 'Chihuahua', 12, 'white', 'small', 'short')

    #create 2 instances named snake1 and snake2 these have attributes from the parent class as well as from its sublclss
    snake1 = Animal.Snake('Snake', 'Cobra', 7, 'black', 15, 'venomous')
    snake2 = Animal.Snake('Snake', 'Corn Snake', 3, 'orange', 4.5, 'not venomous')

    #create 2 instances named bird1 and bird2 these have attributes from the parent class as well as from its sublclss
    bird1 = Animal.Bird('Bird', 'Eagle', 11, 'white', 'yellow beak', 15)
    bird2 = Animal.Bird('Bird', 'African Grey Parrot', 4, 'grey', 'black beak', 13)

    run = True #create a variable 'run' to True

    #establish a while loop with run being the sentinal
    while run == True:
        #set a try/catch loop
        try:
            mode = 0 #set mode to 0 and ask for user input
            mode = int(input('\nPlease select what animal you want to see\n\n(1)'
                               ' Dog1'
                               '\n\n(2) Dog2\n\n'
                               '(3) Snake1\n\n'
                               '(4) Snake2\n\n'
                               '(5) Bird1\n\n'
                               '(6) Bird2\n\n'
                               '(7) Exit\n\n---------------------------------'
                               '-----------------------------------------\n:'))
            
#if any of these if statements are proven true then they would print a specific animals information
            if mode == 1:
                print (dog1) #print dog1 instance attributes
                show_animal_info(dog1) #run the function show-animal-info which prints out the make_sound method in the class
                input ('Press ENTER to continue')
            if mode == 2:
                print (dog2) #print dog2 instance attributes
                show_animal_info(dog2) #run the function show-animal-info which prints out the show_species and make_sound method in the class
                input ('Press ENTER to continue')
            if mode == 3:
                print (snake1) #print snake1 instance attributes
                show_animal_info(snake1) #run the function show-animal-info which prints out the show_species and make_sound method in the class
                input ('Press ENTER to continue')
            if mode == 4:
                print (snake2) #print snake2 instance attributes
                show_animal_info(snake2) #run the function show-animal-info which prints out the show_species and make_sound method in the class
                input ('Press ENTER to continue')
            if mode == 5:
                print (bird1) #print bird1 instance attributes
                show_animal_info(bird1) #run the function show-animal-info which prints out the show_species and make_sound method in the class
                input ('Press ENTER to continue')
            if mode == 6:
                print (bird2) #print bird2 instance attributes
                show_animal_info(bird2) #run the function show-animal-info which prints out the show_species and make_sound method in the class
                input ('Press ENTER to continue')
            if mode == 7:
                input('Exit\nPress enter to exit.')
                run = False #this exits out of the loop
            else:
                print ('You Need To Enter A Number Between 1 and 7')

        #these except functions catch all user input errors
        except ValueError:
            print ('That is not a valid input')
        except UnboundLocalError:
            print ('That is not a valid input')

#the show_animal_info function accepts an object as an argument, and call its make_sound and show_species method
def show_animal_info(species):
    species.show_species()
    species.make_sound()

#execute the main function
main()
