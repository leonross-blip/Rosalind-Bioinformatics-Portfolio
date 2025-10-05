# Problem sheet
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet. The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

# My approach
To solve this problem, I first needed a way to map the 3-base RNA codons to their corresponding single-letter amino acids. The most efficient way to do this was to create a Python dictionary representing the RNA codon table provided by Rosalind. I made sure to include the mappings for the "Stop" codons.

With the codon table in place, I read the input RNA string. I then iterated through this string in non-overlapping chunks of three characters. A for loop with a step of 3 was perfect for this. In each iteration, I extracted the 3-character codon.

I looked up this codon in my dictionary to find the corresponding amino acid. A crucial step was to check if the translated amino acid was "Stop." If it was, the loop terminated immediately. Otherwise, the translated amino acid was appended to my result. The final protein string was then printed to the console.