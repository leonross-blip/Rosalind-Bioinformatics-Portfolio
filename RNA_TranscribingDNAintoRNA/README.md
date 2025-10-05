# Problem statement
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'. Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

# My approach
To solve this, the program first reads the DNA sequence from the input file rosalind_rna.txt. The core of the problem is to substitute every thymine ('T') nucleotide with uracil ('U').

I accomplished this efficiently by using Python's built-in replace() string method. This method iterates through the entire string and replaces all instances of a specified character with another. The resulting RNA string is then printed to the console.