class Volunteer(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def from_dict(source):
        return Volunteer(source['name'], source['age'])

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age
        }