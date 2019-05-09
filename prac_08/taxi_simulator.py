from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi('Prius', 100), SilverServiceTaxi('Limo', 100, 2), SilverServiceTaxi('Hummer', 200, 4)]
    current_taxi = None
    print("Let's Drive!")
    choice = input(MENU)
    while choice != "q":
        if choice == "c":
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
            print("Bill to date: ${}".format(current_taxi.get_fare()))
        choice = input(MENU)
        if choice == "d":
            distance = int(input("Drive how far? "))
            current_taxi.drive(distance)


main()
