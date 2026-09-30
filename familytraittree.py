class Parent:
    def __init__(self, eye_colour, height):
        self.eye_colour = eye_colour
        self.height = height

    def show_traits(self):
        print('Eye colour :', self.eye_colour)
        print('Height :', self.height)

class child(Parent):
    def __init__(self, name, age, eye_colour, height):
        self.age = age
        self.name = name
        super().__init__(eye_colour, height)

    def show_traits(self):
            print('Eye colour :', self.name)
            print('Age :', self.age)
            super().show_traits()