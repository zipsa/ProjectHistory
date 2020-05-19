'''
https://www.coursera.org/learn/dna-analysis/home/welcome
Bioinformatics Course 1 - Week1
'''
#Calculate incidence of DNA pattern on given input DNA string
#Input: Strings
#Output: Count(Text, Pattern)

def pattern_count(input_dna, pattern):
    count = 0
    for i in range(0, len(input_dna) - len(pattern) + 1): #range is upper-bound exclusive
        if input_dna[i:i + len(pattern)] == pattern:
            count += 1
    return count

#In this data file, first line contains DNA string and second line contains pattern to look for
with open("data/dataset_2_7.txt") as file:
    data = file.read().split('\n')

print("The Numbers of Patterns in the DNA string is: ")
print(pattern_count(data[0], data[1]))


#Calculate the most frequent kmers in DNA string
#input: A string DNA text and an integer k
#output: All most frequent k-mers in String

def frequent_kmers (input_dna, k):
    pattern_length = int(k)
    max_count = 0 #Initialize int

    for i in range (0,len(input_dna)-pattern_length +1):
        curr_pattern = input_dna[i:i+pattern_length]
        curr_count = pattern_count(input_dna, curr_pattern)
        if curr_count > max_count:
            max_count = curr_count
            max_pattern = [] #Initialize list within for-loop
            max_pattern.append(curr_pattern)
        elif curr_count == max_count and curr_pattern not in max_pattern:
            max_pattern.append(curr_pattern)
    return max_pattern

print("The most frqeunt kmer is: ")
print(frequent_kmers("CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT", 3))

with open("data/dataset_2_10.txt") as file:
    data2 = file.read().split('\n')

print(type(data2[1])) #String, not int. In function, it was casted as int
print(frequent_kmers(data2[0], data2[1]))

