with open("rosalind_hamm.txt") as f:
    lines = f.read().splitlines()

s1 = lines[0]
s2 = lines[1]
count = 0

for a, b in zip(s1, s2):
    if a != b:
        count += 1

print(count)