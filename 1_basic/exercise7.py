# Challenge - Classes Exercise

# Add a method to the Car class called age
# that returns how old the car is (2019 - year)

# *Be sure to return the age, not print it

class Car:

    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def compute_age(self):
        return(2019 - self.year)

myCar = Car(1996, "Ford", "Everest")
print("The age of my car is " + str(myCar.compute_age()) + " years old.")