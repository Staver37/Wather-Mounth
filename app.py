from os import system
system("clear")

## data procesing / 2d lists

## Simulate Temperature Value for April (1 month)

#  * lists
#  * biodimensional lists
#  * loops
#  * conditionals
#  * sun , avg , min, max, flat
#  * ploting




april_temps = [
    # days ------->
    # Mo   Tu   Wd   Th   Fr   Sa   Su
    [None,None,None,None, 5.0, 6.0, 7.0,],  # |
    [ 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0,],  # |
    [ 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0,],  # V
    [ 8.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0,],  # < weeks
    [ 3.0, 2.0, 1.0, 2.0, 3.0, 4.0, 5.0,],
]
#HW1 INPUT WEEK 
week =int (input("week>>>"))
week = week - 1
day  = 6

print(f"today's temperature {april_temps[week][day]:7.2}C") 
print("forecast for entire week:")

for day_index in range (7) :
    print(f"t:{april_temps[week][day_index]:7.2}C")