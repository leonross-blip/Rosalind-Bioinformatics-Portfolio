fasta_sequences = {}
current_id = ""

with open("rosalind_grph.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            current_id = line[1:]
            fasta_sequences[current_id] = ""
        else:
            fasta_sequences[current_id] += line

k =3
results = []

for id_a, seq_a in fasta_sequences.items():
    for id_b, seq_b in fasta_sequences.items():
        if id_a != id_b and seq_a[-k:] == seq_b[:k]:
            results.append(f"{id_a} {id_b}")

for result in results:
    print(result)