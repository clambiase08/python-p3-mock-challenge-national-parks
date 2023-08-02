from classes.trip import Trip


class Visitor:
    all = []

    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) == str and 1 <= len(value) <= 15 and not hasattr(self, "name"):
            self._name = value
        else:
            raise Exception("Invalid Visitor name")

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]

    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))

    def __repr__(self):
        return f"{self.name}"
