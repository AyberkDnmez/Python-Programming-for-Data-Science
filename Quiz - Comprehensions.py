# Zip Kullanımı

names = ["denise", "jean", "fleur"]

ages = [20, 32, 45]

cities = ["lyon", "lille", "nantes"]

list(zip(names, ages, cities))

# Lambda ve Map Kullanımı

wages = [1000, 2000, 3000, 4000, 5000]

new_wages = lambda x:  x * 0.20 + x

list(map(new_wages, wages))

# Bir Diğer Örnek :

students = ["Denise", "Arsen", "Tony", "Audrey"]

low = lambda x: x[0].lower()

print(list(map(low, students)))

# Örnek :

dictn = {"Denise": 10, "Arsen": 12, "Tony": 15, "Audrey": 17}

new_dict = {k: v * 2 + 3 for (k,v) in dictn.items()}

new_dict