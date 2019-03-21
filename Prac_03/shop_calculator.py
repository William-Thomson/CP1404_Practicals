total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    total_price += float(input("Price of item: "))
print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))
