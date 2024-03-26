class Dog:
    # attributes
    fur = True
    legs = 4
    fur_color = "brown"

    # constructor - setup every variable
    def __init__(self, fur, num_of_legs, fur_color):
        self.fur = fur
        self.legs = num_of_legs
        self.fur_color = fur_color
    def __str__(self):
        return "fur: " + str(self.fur) + " legs: " + str(self.legs) + " Fur color: " + str(self.fur_color)

    def get_fur(self):
        return self.fur

    def get_legs(self):
        return self.legs

    def get_fur_color(self):
        return self.fur_color

    def set_fur(selfself, new_fur):
        self.fur = new_fur

    def set_legs(self, new_legs):
        self.legs = new_legs

    def set_fur_color(self, new_fur_color):
        self.fur_color = new_fur_color