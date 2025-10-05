# Problem statement
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains. An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

# My approach
To solve this problem, I read the DNA string from an input file. I then iterated through the four nucleotides of the DNA alphabet ('A', 'C', 'G', 'T') and used Python's built-in count() string method to count the occurrences of each one. Finally, I printed these four counts to the console, separated by spaces, in the required order.

This approach is efficient for a string of this size as it leverages optimized, built-in functions.