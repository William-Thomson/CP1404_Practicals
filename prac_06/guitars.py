from prac_06.guitar import Guitar


def main():
    """A guitar program using Guitar class"""
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        name = input("Name: ")
    if guitars:
        guitars.sort()
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}. {2:}".format(i + 1, guitar, vintage_string))
    else:
        print("No Guitars.")


main()
