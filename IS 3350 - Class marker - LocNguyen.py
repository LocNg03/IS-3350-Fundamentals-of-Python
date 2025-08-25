"""
Author: Loc Nguyen
Date: 03/10/2022
"""
class Car:
    """Used to illustrate information of a car."""
    def __init__(self, brand, model, horsePower): 
        """Set information of a car"""
        self.brands = brand
        self.models = model
        self.horse = horsePower
    """Return a string representation of car."""
    def __str__(self): #automatically invoked to obtain the string that str returns
        result = ""
        result += "Brand:" + self.brands + "\n" #Return the output of brands
        result += "Model:" + self.models + "\n" #Return the output of models
        result += "Horse power:" + str(self.horse) + "\n" #Return the output of horsePower
        return result
car1 = Car('Ford', 'F-150', 450)
car2 = Car('Any brand', 'Any types', 1000)
print(car1)
print(car2)