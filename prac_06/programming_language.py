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


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print(python)
    print(visual_basic)

main()
