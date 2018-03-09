base = float(raw_input("What base would you like to convert to? "))
print ""
n = float(raw_input("What number would you like to convert? "))

for i in range (0,4):
    place = 1
    while n >= place:
        ##print place
        place = base*place

        print place/base

        print int(n/(place/base))
        leftovers = n - place/base
      ##print leftovers
