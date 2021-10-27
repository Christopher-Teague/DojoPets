
class Ninja:
    def __init__ (self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    # implement the following methods:
    def walk(): # - walks the ninja's pet invoking the pet play() method
        pass

    def feed(): # - feeds the ninja's pet invoking the pet eat() method
        pass

    def bathe(): # - cleans the ninja's pet invoking the pet noise() method
        pass

class Pet:
    def __init__ (self, name , type , tricks ):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

# implement the following methods:
    def sleep(self): # - increases the pets energy by 25
        self.energy += 25

    def eat(): # - increases the pet's energy by 5 & health by 10
        self.health += 10
        self.energy += 5

    def play(): # - increases the pet's health by 5
        self.health += 5

    def noise(): # - prints out the pet's sound
        pass