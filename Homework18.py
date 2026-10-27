cities = {"Toshkent": 3000000, "Farg'ona": 300000, "Samarqand": 600000}

large_cities = ""
max_pop = 0
max_city = ""

for city, pop in cities.items():
    if pop > 500000:
        large_cities += city + " "
        
    if pop > max_pop:
        max_pop = pop
        max_city = city

print(f"More than 500,000: {large_cities}")
print(f"Most populated: {max_city}")