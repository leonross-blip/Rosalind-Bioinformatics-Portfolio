# Problem statement
Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s. The position of a symbol in a string is its 1-based index.

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

# My approach
To find all occurrences of the motif t within the larger DNA string s, I used a sliding window approach. I iterated through the main string s with a for loop, moving one character at a time. The loop's range was carefully set to stop when the remaining part of s was shorter than the motif t.

In each iteration, I extracted a substring from s that was the same length as the motif t. I then compared this extracted substring to the motif t. If they matched, I recorded the starting position of the match. It's important to note that Rosalind uses 1-based indexing, so I added 1 to the 0-based Python index before storing it.

After the loop completed, I had a list of all starting positions, which I then printed as the final output.