from classes.trip import Trip


class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

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
        for trip in Trip.all:
            if isinstance(trip, Trip):
                return [trip for trip in Trip.all if trip.national_park == self]

    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        return max(self.visitors(), key=[trip.visitor for trip in self.trips()].count)

    @classmethod
    def most_visited(cls):
        return max(cls.all, key=lambda park: park.total_visits())

    def __repr__(self):
        return f"{self.name}"
