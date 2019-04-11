CURRENT_YEAR = 2019
VINTAGE_AGE = 50

class Guitar:
    """Guitar Class"""

    def __init__(self, name="", year=0, cost=0):
        """Constructs a guitar object"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """returns a string of object values"""
        return "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """determines the age of the guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determines if guitar is vintage"""
        return self.get_age() >= VINTAGE_AGE
