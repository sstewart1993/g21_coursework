numbers = range(1,11)
even_squared = [x*x for x in numbers if x % 2 == 0]
print(even_squared)

for number in numbers:
    if number % 2 == 0:
        even_squared.append(number*number)
    
print(even_squared)

ages = [5, 15, 64, 27, 84, 26]
odd_ages = [x for x in ages if x % 2 != 0]
print(odd_ages)

chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
more_than_ten = [name for name in chicken_names if len(name) > 10]
print(more_than_ten)
start_with_h = [name for name in chicken_names if name[0] == ("H" or "h")]      # can use name.startswith("H")
print(start_with_h)

words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
lower_first = [letter[0].lower() for letter in words]
print(lower_first)