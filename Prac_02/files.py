# Question 1
OUTPUT_FILE = 'name.txt'

out_file = open(OUTPUT_FILE, 'w')

name = str(input("Enter name: "))
print(name, file=out_file)
out_file.close()

# Question 2
in_file = open('name.txt', 'r')
name = in_file.readline().strip()
print("Your name is ", name)
in_file.close()

# Question 3
in_file = open('numbers.txt', 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print(number1 + number2)
in_file.close()

# Extension Question
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()
