register_classes = []


class Meta(type):
    def __new__(cls, name, bases, namespace):
        new_class = super().__new__(cls, name, bases, namespace)
        register_classes.append(new_class)
        return new_class


class User1(metaclass=Meta):
    pass


class User2(metaclass=Meta):
    pass


class User3(metaclass=Meta):
    pass


print(register_classes)
