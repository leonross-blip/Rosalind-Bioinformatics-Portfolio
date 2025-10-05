# Problem statement
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'. The reverse complement of a DNA string s is the string s<sup>c</sup> formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement of s.

# My approach
To generate the reverse complement of the DNA string, I broke the problem down into two main steps:

Reverse the String: First, I read the DNA string from the input file. I then used Python's extended slice syntax ([::-1]) to create a reversed copy of the entire string.

Complement the Bases: Next, I needed to find the complement of each nucleotide in the reversed string. To do this efficiently, I created a dictionary to map each DNA base to its complement ('A' -> 'T', 'T' -> 'A', 'C' -> 'G', 'G' -> 'C'). I then iterated through the reversed string, looked up each character in the dictionary, and built the final complemented string.

This two-step process is clear and correctly computes the reverse complement as required.