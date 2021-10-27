
class Ninja:
    def __init__ (self, first_name , last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    # implement the following methods:
    def walk(self): # - walks the ninja's pet invoking the pet play() method
        self.pet.play()

    def feed(self): # - feeds the ninja's pet invoking the pet eat() method
        self.pet.eat()

    def bathe(self): # - cleans the ninja's pet invoking the pet noise() method
        self.pet.noise()

class Pet:
    def __init__ (self, name , type , tricks ):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 50
        self.energy = 50

# implement the following methods:
    def sleep(self): # - increases the pets energy by 25
        self.energy += 25

    def eat(self): # - increases the pet's energy by 5 & health by 10
        self.health += 10
        self.energy += 5

    def play(self): # - increases the pet's health by 5
        print(f"{self.name} is being walked...")
        self.health += 5

    def noise(self): # - prints out the pet's sound
        print("Mooo")

# joe = Pet("joe", "cow", "anti-tipping")
bob = Ninja("bob", "ross", "scooby snack", "mutton", Pet("joe", "cow", "anti-tipping"))

bob.walk()
bob.feed()
bob.bathe()