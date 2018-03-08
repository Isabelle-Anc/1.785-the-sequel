base = float(raw_input("What base would you like to convert to? "))

n = float(raw_input("What number would you like to convert? "))

place = 1

while n >= place:
    print place
    place = base*place
