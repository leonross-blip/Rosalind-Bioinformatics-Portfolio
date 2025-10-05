fasta_sequences = {}
current_id = ""

with open("rosalind_gc.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            current_id = line[1:]
            fasta_sequences[current_id] = ""
        else:
            fasta_sequences[current_id] += line

gc_percentages = {}

for seq_id, dna_string in fasta_sequences.items():
    total_length = len(dna_string)

    g_count = dna_string.count("G")
    c_count = dna_string.count("C")

    gc_percent = ((g_count + c_count) / total_length) * 100

    gc_percentages[seq_id] = gc_percent

max_gc_id = max(gc_percentages, key=gc_percentages.get)

max_gc_value = gc_percentages[max_gc_id]

print(max_gc_id)
print(max_gc_value)