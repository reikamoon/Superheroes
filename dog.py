#dog.py
class Dog:
    def __init__(self, name, breed, greeting):
        self.name = name
        self.breed = breed
    def bark(self):
        print("Snort!")
    def sit(self):
        print("<> sits")
    def roll_over(self):
        print("<> rolls over")

my_dog = Dog("Mochi", "Boston Terrier", "*scratchy bark*")
my_other_dog = Dog("Mika", "Minature Schnauzer", "BAUR!")
my_last_dog = Dog("Biskit", "Maltipoo", "Yap!")
my_dog.breed = "Boston Terrier"
my_dog.bark()
my_other_dog.sit()
my_last_dog.roll_over()
#print(my_dog)
#print(my_dog.name)
#print(my_dog.breed)
Dog.greeting = "Woah"
