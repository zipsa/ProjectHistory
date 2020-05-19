'''
Find a Profile-most probable k-mer in a string.

Input: A string Text, an integer k, and a 4 × k matrix Profile.
Output: A Profile-most probable k-mer in Text.

Sample input
string = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"

profile = {
    'A': [0.2, 0.2, 0.3, 0.2, 0.3],
    'C': [0.4, 0.3, 0.1, 0.5, 0.1],
    'G': [0.3, 0.3, 0.5, 0.2, 0.4],
    'T': [0.1, 0.2, 0.1, 0.1, 0.2]
}

Sample output
CCGAG

'''
import numpy as np

with open ("data/dataset_159_3.txt") as file:
    data = file.read().split('\n') #Split by line
    profile = {'A': data[2].split(),
               'C': data[3].split(),
               'G': data[4].split(),
               'T': data[5].split()}



#score calculator of given k-mer string(motif).
#length of motif and length of profile['A'] should be the same.
def score_calculator_single_motif (motif, profile):
    #convert string motif into list.
    char_list = list()
    for i in range(len(motif)):
        char_list.append(motif[i])

    #Using the list, calculate the score.
    score = float(1)
    for i in range(len(char_list)):
        #print(profile[char_list[i]][i])
        score = score * float(profile[char_list[i]][i])
    return score


# String as dna string, k as kmer, profile as 4-k metrix.
def motif_greedy(string, k, profile):
    score_list = []
    for i in range(len(string) - k + 1):
        curr_motif = string[i:i + k]
        curr_score = score_calculator_single_motif(curr_motif, profile)
        score_list.append(curr_score)

    score_arr = np.array(score_list)
    max_idxs = np.where(score_arr == np.amax(score_arr))[0]
    max_score = np.amax(score_arr)

    print('max index are', max_idxs[0]) #max index
    print('max score is', max_score) #max elements
    return string[max_idxs[0]: max_idxs[0] + k] #return first one and ignore others.

if __name__ == '__main__':
    #score_calculator("ACCTG", profile)
    #print(profile)
    ans = motif_greedy(data[0], int(data[1]), profile)
    print(ans)