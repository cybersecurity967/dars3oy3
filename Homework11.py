math = {"Ali", "Vali", "Madina", "Jasur", "Aziza"}
english = {"Madina", "Jasur", "Sardor", "Aziza", "Malika"}

both = math & english

only_one = math ^ english

both_str = ""
for name in both:
    both_str += name + " "

only_one_str = ""
for name in only_one:
    only_one_str += name + " "

print(f"Both courses: {both_str}")
print(f"Only one course: {only_one_str}")