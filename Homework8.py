temperatures = (18, 20, 17, 23, 25, 21, 19)
above_20 = []

for temp in temperatures:
    if temp > 20:
        above_20.append(temp)

temps_str = ", ".join(map(str, above_20))

print(f"Temperatures: {temps_str}")
print(f"Days count: {len(above_20)}")