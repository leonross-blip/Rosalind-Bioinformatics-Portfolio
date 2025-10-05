# Problem statement
Given two strings s and t of equal length, the Hamming distance between s and t, denoted d<sub>H</sub>(s,t), is the number of corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance d<sub>H</sub>(s,t).

# My approach
To calculate the Hamming distance, the program must compare two DNA strings of equal length and count the number of positions at which the characters are different.

My approach was to first read the two strings from the input file. I then initialized a counter variable to zero. I used a single for loop that iterates from the first to the last index of the strings. Inside the loop, I compared the characters from both strings at the current index. If the characters did not match, I incremented the counter.

After the loop finished, the counter held the total number of mismatches, which is the Hamming distance. This value was then printed to the console.