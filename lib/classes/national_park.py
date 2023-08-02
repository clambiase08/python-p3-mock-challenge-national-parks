class NationalPark:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) == str and not hasattr(self, "name"):
            self._name = value
        else:
            raise Exception("Invalid Park name")

    def trips(self):
        from classes.trip import Trip

        for trip in Trip.all:
            if isinstance(trip, Trip):
                return [trip for trip in Trip.all if trip.national_park == self]

    def visitors(self):
        from classes.visitor import Visitor

        for visitor in Visitor.all:
            if isinstance(visitor, Visitor):
                return list(set([trip.visitor for trip in self.trips()]))

    def total_visits(self):
        pass

    def best_visitor(self):
        pass

    @classmethod
    def most_visited(cls):
        pass

    def __repr__(self):
        return f"{self.name}"
