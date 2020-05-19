'''
Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.

Input: Strings Pattern and Text along with an integer d.
Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.

Sample Input:

ATTCTGGA
CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT
3
Sample Output:

6 7 26 27
'''

#used hamming distance algorithm previous devloped.
def hamming_distance(s1, s2):
    d = sum(1 for a, b in zip(s1, s2) if a != b)
    return d

#identify index of given pattern in string_dna, allowing d mutations.
def pattern_matching_mut (string_dna, pattern, d):
    idx = list()
    for i in range(0, len(string_dna) - len(pattern) + 1):
        curr_pattern = string_dna[i:i + len(pattern)]
        curr_distance = hamming_distance(pattern, curr_pattern)
        if curr_distance <= d:
            idx.append(str(i))
    return idx

#Count numbers of occurance of pattern in string_dna, allowing d mutations.
def pattern_count_mut (string_dna, pattern, d):
    count = 0
    for i in range(0, len(string_dna) - len(pattern) + 1):
        curr_pattern = string_dna[i:i + len(pattern)]
        curr_distance = hamming_distance(pattern, curr_pattern)
        if curr_distance <= d:
            count += 1
    return count


with open("data/dataset_9_4.txt") as file:
    dat = file.read().split('\n')
print(' '.join(pattern_matching_mut(dat[1], dat[0], int(dat[2]))))

with open("data/dataset_9_6.txt") as file:
    dat2 = file.read().split('\n')
print("Matchin index:", ' '.join(pattern_matching_mut(dat2[1], dat2[0], int(dat2[2]))))
print("Matched count:", pattern_count_mut(dat2[1], dat2[0], int(dat2[2])))


#Find most frequent kmers in given DNA string (when k<=12 and d<3)
#Where k is length of kmer, d is numbers of mutation allowed,
def find_frequent_kmer_mut (string_dna, k, d):
    max_count = 0
    pattern_dict = dict()
    most_frequent_kmer = list()

    for i in range(len(string_dna) - k + 1):
        curr_pattern = string_dna[i:i+k]
        curr_count = pattern_count_mut(string_dna, curr_pattern, d)

        if curr_pattern not in pattern_dict:
            pattern_dict[curr_pattern] = curr_count #This is a key implementation
        if curr_count > max_count:
            max_count = curr_count

    for key in pattern_dict:
        if pattern_dict[key] == max_count:
            most_frequent_kmer.append(key)
    return most_frequent_kmer

print(find_frequent_kmer_mut ("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1))

with open("data/dataset_9_7.txt") as file:
    dat3 = file.read().split('\n')

print(find_frequent_kmer_mut(dat3[0], 6, 2))