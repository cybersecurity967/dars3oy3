first = {"Ali", "Madina", "Jasur", "Aziza"}
second = {"Jasur", "Sardor", "Aziza", "Bekzod"}

only_first = first - second

only_second = second - first

both = first & second

only_first_str = ""
for name in only_first:
    only_first_str += name + " "

only_second_str = ""
for name in only_second:
    only_second_str += name + " "

both_str = ""
for name in both:
    both_str += name + " "

print(f"Only first: {only_first_str}")
print(f"Only second: {only_second_str}")
print(f"In both: {both_str}")