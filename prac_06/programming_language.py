class ProgrammingLanguage:
    """Represent a programming language object"""

    def __init__(self, name="", typing="", reflection=False, year=""):
        """create an initial construct with the given values"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if program is dynamically typed"""
        return self.typing == "Dynamic"

    def __str__(self):
        """returns string representing object values"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)
