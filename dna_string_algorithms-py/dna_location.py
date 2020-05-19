'''
Input: Two strings, Pattern and Genome.
Output: A collection of space-separated integers specifying all starting positions where Pattern appears
as a substring of Genome.
'''


def find_location (dna, pattern):
    location = []
    for i in range (0, len(dna) - len(pattern) + 1):
        if dna[i : i + len(pattern)] == pattern:
            location.append(str(i)) #need to cast it to str to use .join.
    return ' '.join(location) #Convert the results to space-sperated values

with open ("data/dataset_3_5.txt") as file:
    dna_string = file.read().split('\n')
print(find_location(dna_string[1], dna_string[0]))


with open ("data/Vibrio_cholerae.txt") as file:
    dna_cholerae = file.read().split('\n')
print(find_location(dna_cholerae[0], "CTTGATCAT"))


print(find_location("ATGACTTCGCTGTTACGCGC", "CGC"))