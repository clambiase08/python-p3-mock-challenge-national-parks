class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    def __repr__(self):
        return f"<Trip | visitor: {self.visitor}, park: {self.national_park}, start: {self.start_date}, end: {self.end_date}>"
