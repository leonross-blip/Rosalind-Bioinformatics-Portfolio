with open("rosalind_rna.txt") as f:
    s = f.read().strip()
s = s.replace("T", "U")
print(s)