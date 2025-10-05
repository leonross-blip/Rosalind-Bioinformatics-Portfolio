# Problem statement
A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge. For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s ≠ t.

Given: A collection of DNA strings in FASTA format having a total length of at most 10 kbp.

Return: The adjacency list corresponding to the overlap graph O<sub>3</sub>.

# My approach
To construct the adjacency list for the overlap graph, I first needed to parse all the DNA strings from the given FASTA file. I used a dictionary to store the data, mapping each FASTA ID to its corresponding DNA sequence.

With the data structured, the main task was to compare every sequence against every other sequence to find overlaps of length k=3. I implemented this using a nested for loop that iterates through all possible pairs of sequences.

Inside the inner loop, I performed two checks for each pair (s1, s2):

I ensured the sequences were not identical by comparing their FASTA IDs.

I checked for the overlap condition by extracting the suffix of s1 and the prefix of s2, both of length 3, and testing for equality.

If both conditions were met, I recorded the pair of FASTA IDs as a directed edge in the graph. The final output is the complete list of these identified edges.