from classes.trip import Trip


class Visitor:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) == str and 1 <= len(value) <= 15:
            self._name = value
        else:
            raise Exception("Invalid Visitor name")

    def trips(self):
        pass

    def national_parks(self):
        pass

    def __repr__(self):
        return f"<Visitor: {self.name}>"
