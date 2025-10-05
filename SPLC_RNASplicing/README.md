# Problem statement
After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s.

# My approach
This problem required a multi-step pipeline to simulate the process of gene splicing, transcription, and translation.

Parse FASTA: First, I parsed the input FASTA file. Since the main DNA string is always the first sequence provided, I read all sequences into a list. The first element of the list became my main DNA string, and the rest were stored as a list of intron strings.

Splice Introns: I then iterated through the list of intron strings. In each iteration, I used Python's .replace() method to remove the current intron from the main DNA string. After the loop, the main string contained only the remaining exon sequences.

Transcribe to RNA: The resulting DNA string was transcribed into RNA by replacing all instances of thymine ('T') with uracil ('U').

Translate to Protein: Finally, I used the codon table dictionary and the translation logic from the PROT problem to translate the RNA string into a protein sequence, stopping at the first "Stop" codon. The final protein string was then printed as the result.