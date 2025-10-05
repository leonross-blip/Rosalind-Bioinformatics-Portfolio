with open("rosalind_subs.txt") as f:
    lines = f.read().splitlines()

s = lines[0]
t = lines[1]

len_s = len(s)
len_t = len(t)

locations = []

for i in range(len_s - len_t + 1):
    if s[i:i+len_t] == t:
        locations.append(i + 1)

print(' '.join(map(str, locations)))