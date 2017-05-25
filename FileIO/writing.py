# cities = ['Seattle', 'Bellevue', 'Renton', 'Everett', 'Olympia']
#
# with open('cities.txt', 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

cities = []

with open('cities.txt', 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))

print(cities)
for city in cities:
    print(city)

