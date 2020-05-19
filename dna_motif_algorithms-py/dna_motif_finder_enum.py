'''
A brute force algorithm for motif finding.

Given a collection of strings Dna and an integer d, a k-mer is a (k,d)-motif if it appears in every string from Dna with at most d mismatches.
Implanted Motif Problem: Find all (k, d)-motifs in a collection of strings.

Input: A collection of strings Dna, and integers k and d.
Output: All (k, d)-motifs in Dna.
'''
#Use previous algorithm that I previously generated.
from dna_neighborhood import neighbors

#Input is list of dna
def motif_enumeration(list_dna, k, d):
    collection = list()  # store collection of sets (neighbers) in list.
    for i in range(len(list_dna)):
        curr_dna = list_dna[i]
        curr_neighbor = set()
        for l in range(len(curr_dna)- k + 1):
            curr_neighbor = curr_neighbor.union(neighbors(curr_dna[l: l + k], d)) #union will generate new set, instead of updating it.
        collection.append(curr_neighbor)
    #print(collection)

    motif_set = collection[0] #Initialization
    for j in range(len(collection)):
        motif_set = motif_set.intersection(collection[j])
    return motif_set

#list_dna = ["ATTTGGC","TGCCTTA", "CGGTATC","GAAAATT"]
#print(' '.join(motif_enumeration(list_dna, 3, 1)))

with open("data/dataset_156_8.txt") as file:
    data = file.read().split('\n')

list_dna = [data[1], data[2], data[3], data[4], data[5], data[6]]
print(' '.join(motif_enumeration(list_dna, 5, 1)))