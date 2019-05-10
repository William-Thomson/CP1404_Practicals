from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi('Prius', 100), SilverServiceTaxi('Limo', 100, 2), SilverServiceTaxi('Hummer', 200, 4)]
    current_taxi = None
    print("Let's Drive!")
    menu_choice = input(MENU)
    while menu_choice != "q":
        if menu_choice == "c":
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
        elif menu_choice == "d":
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${}".format(current_taxi.name, trip_cost))
            total_bill += trip_cost
        else:
            print("Invalid Option")
        print("Bill to date: ${:.2f}".format(total_bill))
        menu_choice = str(input(MENU))
    print("Total Trip Cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
