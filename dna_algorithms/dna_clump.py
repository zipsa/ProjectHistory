#Idea was to use dictionary.
#Unfortunately, this solution is not fast enough to search for entire genome.
#Takes 10 min to have answer.

def clump_finder(DNA, k, L, t):
    freq = dict()
    words = list()
    k = int(k)
    L = int(L)
    t = int(t)
    for i in range(len(DNA) - L):
        for j in range(i, i + L - k + 1):
            pattern = DNA[j:j + k]
            freq[pattern] = freq.get(pattern, 0) + 1

        for key in freq:
            if (freq[key] >= t) and (key not in words):
                words.append(key)
        freq.clear()
    return words

'''
text = input('Enter genome sequence: ')
k = input('Enter length of k-mer: ')
L = input('Enter length of window: ')
t = input('Enter how many times k-mer should appear in window: ')
'''


#with open ("data/dataset_4_5.txt") as file:
with open ("data/E_coli.txt") as file:
    data = file.read().split('\n')

DNA = str(data[0].upper())
k = 9
L = 500
t = 3

print(clump_finder(DNA, k, L, t))
print(len(clump_finder(DNA, k, L, t)))