scores = (12, 18, 15)

total = 0
best_score = 0
best_attempt = 0
current_attempt = 1

for score in scores:
    total += score
    if score > best_score:
        best_score = score
        best_attempt = current_attempt
    current_attempt += 1

print(f"Total score: {total}")
print(f"Best attempt: {best_attempt}")
print(f"Best score: {best_score}")