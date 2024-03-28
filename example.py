class MyClass:
    """Example class for task1"""
    def __init__(self, name, age):
        """Initiate some attributes"""
        self.name = name
        self.age = age

    def __str__(self):
        """Return string representation of the object"""
        return f'{self.name} is {self.age} years'

    def get_name(self):
        """Return the name of the instance"""
        return self.name


class UpdatedMyClass(MyClass):
    """Example class for task1, it is derived from MyClass"""
    def __init__(self, name, age, country):
        """Initiate parent class attributes, add new attributes"""
        super().__init__(name, age)
        self.country = country

    def __str__(self):
        """Return string representation of the object"""
        return f'{super().__str__()}. I am from {self.country}'

    def get_name(self):
        """Overrides version"""
        return "UpdatedMyClass(" + self.name + ")"

    def do_something(self):
        """Does some work in country"""
        print(f"I am do something in {self.country}.")


def print_text(some_text):
    """Show some text"""
    print(some_text)
