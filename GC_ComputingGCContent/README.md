# Problem statement
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. DNA strings are commonly stored in FASTA format.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.

# My approach
This problem required three main steps: parsing the multi-sequence FASTA file, calculating the GC-content for each sequence, and finding the sequence with the maximum GC-content.

Parsing FASTA: I read the input file line by line. To store the sequences, I used a dictionary where the keys are the FASTA IDs (e.g., "Rosalind_6404") and the values are the corresponding DNA strings. When a line started with '>', I knew it was a new ID, so I created a new entry in the dictionary. All subsequent lines were appended to the value of the most recent ID until the next '>' was found.

Calculating GC-Content: After parsing, I iterated through the dictionary. For each sequence, I counted the number of 'G' and 'C' characters. The GC-content was then calculated using the formula: (G_count + C_count) / total_length * 100.

Finding the Maximum: While iterating and calculating the GC-content for each sequence, I kept track of the ID and GC-content of the sequence with the highest percentage found so far. If the current sequence's GC-content was higher than the maximum I'd seen, I updated my variables.

Finally, I printed the ID and the maximum GC-content value.