with open("rosalind_revc.txt") as f:
    s = f.read().strip()
reversed_s = s[::-1]
complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
complement_list = []
for base in reversed_s:
    complement_list.append(complement_map[base])
reverse_complement = ''.join(complement_list)
print(reverse_complement)