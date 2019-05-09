from prac_08.taxi import Taxi

prius = Taxi('Prius 1', 100, 1.23)

prius.drive(40)

print(prius)

prius.start_fare()
prius.drive(100)

print(prius)
prius.get_fare()
