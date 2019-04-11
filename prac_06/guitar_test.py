from prac_06.guitar import Guitar

def run_tests():
    gibson = Guitar("Gibson L-5", 1922, 16035.40)
    print("{} get_age() - Expected 97. Got {}".format(gibson.name, gibson.get_age()))
    print(gibson.is_vintage())


run_tests()
