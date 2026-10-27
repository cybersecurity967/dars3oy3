ali = {"comedy", "adventure", "fantasy"}
vali = {"fantasy", "drama", "comedy"}

common = ali & vali

only_one = ali ^ vali

common_str = ""
for genre in common:
    common_str += genre + " "

only_one_str = ""
for genre in only_one:
    only_one_str += genre + " "

print(f"Common genres: {common_str}")
print(f"Only one likes: {only_one_str}")