total = 0
count = 0

while True:
    expense = int(input())
    if expense == 0:
        break
    total += expense
    count += 1

if count > 0:
    average = total / count
    print(f"Total: {total}")
    print(f"Count: {count}")
    print(f"Average: {average:.2f}")