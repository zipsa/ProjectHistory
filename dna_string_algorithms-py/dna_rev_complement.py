# Reverse Complement Problem: Find the reverse complement of a DNA string.
# Input: A DNA string Pattern.
# Output: Pattern rc , the reverse complement of Pattern.

def reverse_complement(seq):
    rev_seq = seq[::-1]
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} #Dictrionary
    bases = list(rev_seq) #Convert string to list containing individual char

    bases_cpl = []
    for char in bases:
        bases_cpl.append(complement[char])

    #Same thing can be achieved with List comprehension
    #bases_cpl = [complement[char] for char in bases]

    return ''.join(bases_cpl)


with open("data/dataset_3_2.txt") as file:
    data = file.read().split('\n')

print("Original Sequence:")
print(data[0])

print("Reverse Complement:")
print(reverse_complement(data[0]))

