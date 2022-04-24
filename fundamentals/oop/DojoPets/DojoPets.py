
class Ninja:
    def __init__(self, firstName , lastName , pet ):
        self.firstName = firstName
        self.lastName = lastName
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        print(f"Your Dog {self.pet.name} is being fed")
        self.pet.eat()

    def bathe(self):
        self.pet.noise()
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method
class Pet:
    def __init__(self, name , type , tricks, noise ):
# implement the following methods:
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.energy = 100
        self.health = 100

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(self.noise)
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound

Moxie = Pet("Ms. Moxie", "Dog", "Shake", "Woof")

Brody = Ninja("Brody", "Henry", Moxie)

Brody.feed()