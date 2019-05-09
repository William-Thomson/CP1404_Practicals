from prac_08.silver_service_taxi import SilverServiceTaxi


def test_silver_taxi():
    new_taxi = SilverServiceTaxi('Hummer', 200, 2)
    print(new_taxi)
    new_taxi.drive(18)
    print(new_taxi)
    print('${}'.format(new_taxi.get_fare()))


test_silver_taxi()
