emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]

unique = set()

for e in emails:
    name, dom = e.split("@")

    name = name.split("+")[0]
    name = name.replace(".", "")
    unique.add(f"{name}@{dom}")

print(len(unique))
