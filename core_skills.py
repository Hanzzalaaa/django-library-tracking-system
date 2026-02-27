import random


# Create list of 10 random numbers b/w 1 - 20
random_numbers = [random.randint(1,20) for i in range(10)]
print("Random Numbers", random_numbers)


#Filter Number Below 10 by using list comprehension
below_ten_list_comp = [num for num in random_numbers if num < 10]

print("Below Ten List Comprehension",below_ten_list_comp)


# Filter Number below 10 by using filter
below_ten_filter = list(filter(lambda a : a < 10, random_numbers))

print("Below Ten Filter",below_ten_filter)


