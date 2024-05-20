# Training

# Taking user input.
name = input('\nCould you please tell me your name?: ')
while True:
    age_input = input('Could you please tell me your age?: ')
    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Please enter a valid age in numbers.")
hair_color = input('Could you please tell me your hair color?: ')
eye_color = input('Could you please tell me your eye color?: ')

# Creating the class and methods.
class Adult:
    def __init__(self, name, age, hair_color, eye_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color
        
    def can_drive(self):
        print(f'\nThis is {self.name} and they are {self.age} years old.')
        print('Meaning they are old enough to drive.\n')


# Creating child class.
class Child(Adult):
    def can_drive(self):
        print(f'\nThis is {self.name} and they are {self.age} years old.')
        print('Sorry, they are too young to drive.\n')


# Creating an instance of the Child class if age < 18, else an instance of the Adult class.
if age < 18:
    person = Child(name, age, hair_color, eye_color)
else:
    person = Adult(name, age, hair_color, eye_color)

# Calling the method.
person.can_drive()


