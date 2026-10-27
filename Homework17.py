grades = {"Ali": 85, "Vali": 72, "Madina": 96, "Jasur": 68}

total = 0
count = 0
high_scorers = ""

for name, score in grades.items():
    total += score
    count += 1
    
    if score >= 90:
        high_scorers += f"{name} - {score} "

average = total / count

print(f"High scorers: {high_scorers}")
print(f"Average score: {average}")