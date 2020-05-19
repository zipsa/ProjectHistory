'''
Input: An integer k, followed by a collection of strings Dna.
Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all possible choices of k-mers.
(If there are multiple such strings Pattern, then you may return any one.)
'''
import timeit
from itertools import product,chain
from collections import defaultdict

def read_file(input_file):
    f = open(input_file)
    data = [item.strip() for item in f.readlines()]
    f.close()
    return (int(data[0]),data[1:]) #return tuple with two components

def correct(seq,k):
    return set(seq[i:i+k] for i in range(len(seq)-k+1))

def hamming_distance(pattern,text,k):
    return sum([1 for i in range(k) if pattern[i] != text[i]])

def cartesian_products(k):
    '''
    >>> cartesian_products(k)
    ['AAA', 'AAC', 'AAT', 'AAG', 'ACA', 'ACC', 'ACT', 'ACG', 'ATA', 'ATC', 'ATT', 'ATG', 'AGA', 'AGC', 'AGT', 'AGG',
     'CAA', 'CAC', 'CAT', 'CAG', 'CCA', 'CCC', 'CCT', 'CCG', 'CTA', 'CTC', 'CTT', 'CTG', 'CGA', 'CGC', 'CGT', 'CGG',
     'TAA', 'TAC', 'TAT', 'TAG', 'TCA', 'TCC', 'TCT', 'TCG', 'TTA', 'TTC', 'TTT', 'TTG', 'TGA', 'TGC', 'TGT', 'TGG',
     'GAA', 'GAC', 'GAT', 'GAG', 'GCA', 'GCC', 'GCT', 'GCG', 'GTA', 'GTC', 'GTT', 'GTG', 'GGA', 'GGC', 'GGT', 'GGG']
    '''
    return [''.join(item) for item in product('ACTG',repeat=k)]

def distance(kmer,dna_string,k):
    '''
    >>> distance('AAA','AAATTGACGCAT',k)
    ('AAA', 0)
    >>> distance('GGC','AAATTGACGCAT',k)
    ('GGC', 1)
    '''
    return (kmer,min([hamming_distance(kmer,sk,k) for sk in correct(dna_string,k)]))

def kmer_Dna_distance(kmer,Dna,k):
    '''
    Note: calculate d(Pattern, Dna)
    >>> Dna
    ['AAATTGACGCAT', 'GACGACCACGTT', 'CGTCAGCGCCTG', 'GCTGAGCACCGG', 'AGTACGGGACAG']
    >>> kmer_Dna_distance('AAA',Dna,k)
    {'ACC': [('GACGACCACGTT', 0), ('GCTGAGCACCGG', 0), ('AAATTGACGCAT', 1), ('CGTCAGCGCCTG', 1), ('AGTACGGGACAG', 1)],
     'ATG': [('AAATTGACGCAT', 1), ('GACGACCACGTT', 1), ('CGTCAGCGCCTG', 1), ('GCTGAGCACCGG', 1), ('AGTACGGGACAG', 1)],
     ...
     'TCT': [('CGTCAGCGCCTG', 1), ('GCTGAGCACCGG', 1), ('AAATTGACGCAT', 2), ('GACGACCACGTT', 2), ('AGTACGGGACAG', 2)]}
    '''
    return [(distance(kmer,dna_string,k)[0],(dna_string,distance(kmer,dna_string,k)[1])) for dna_string in Dna]

def all_kmers_Dna_distance(Dna,k):
    apks = cartesian_products(k)
    d = list(chain(*[kmer_Dna_distance(kmer,Dna,k) for kmer in apks]))
    df = defaultdict(tuple)
    for tup in d:
        df[tup[0]] += (tup[1],)
    return dict([(key,sorted(value,key=lambda x:x[1])) for key,value in df.items()])

def medianstring(Dna,k):
    '''
    Note: calculate d(Pattern, Dna)
    '''
    akDd = all_kmers_Dna_distance(Dna,k)
    result = [(key,sum([item[1] for item in value])) for key,value in akDd.items()]
    return sorted(result,key=lambda x:x[1])[0]

def result(filename):
    k,Dna = read_file(filename) #assign returned tuple to k and Dna
    return medianstring(Dna,k)[0]

if __name__ == "__main__":

    start = timeit.default_timer()
    results = result("data/dataset_158_9_quiz.txt")
    print(results)
    stop = timeit.default_timer()
    print(stop - start)


