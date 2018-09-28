class Volunteer(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def from_dict(from_dict):
    #     return Volunteer(from_dict['name'], from_dict['age'])

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age
        }