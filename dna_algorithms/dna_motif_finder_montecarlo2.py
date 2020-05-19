import sys
from random import randint

#file_name = "sys.argv[1]"
file_name = "data/dataset_161_5.txt"

global k,t #allow to update variable outside of current scope.

dna = []
with open(file_name) as f:
	for line in f:
		if len(line.split()) > 1:
			k,t = map(int,line.split())
		else:
			dna.append(line[:-1]) #remove \n at the end of string

def hamming_distance(s1, s2):
	score = 0
	if len(s1) != len(s2):
		print("Error")
	else:
		for i in range(len(s1)):
			if s1[i] != s2[i]:
				score += 1
	return score

def score(motifs):
	'''
	:param motifs: list of randomly selected motifs
	:return: final score from list of motifs
	'''
	score = 0
	for i in range(len(motifs[0])):
		motif = ''.join([motifs[j][i] for j in range(len(motifs))])
		score += min([hamming_distance(motif, homogeneous * len(motif)) for homogeneous in 'ACGT'])
	return score

def profile(motifs):
	prof = []
	for i in range(len(motifs[0])):
		col = ''.join([motifs[j][i] for j in range(len(motifs))])
		prof.append([float(col.count(nuc))/float(len(col)) for nuc in 'ACGT'])
	return prof

def profile_most_probable_kmer(dna, k, prof):
	nuc_loc = {nucleotide:index for index,nucleotide in enumerate('ACGT')}
	max_prob = [-1, None]
	for i in range(len(dna)-k+1):
		current_prob = 1
		for j, nucleotide in enumerate(dna[i:i+k]):
			current_prob *= prof[j][nuc_loc[nucleotide]]
		if current_prob > max_prob[0]:
			max_prob = [current_prob, dna[i:i+k]]

	return max_prob[1]

def profile_with_pseudocounts(motifs):
	prof = []
	for i in range(len(motifs[0])):
		col = ''.join([motifs[j][i] for j in range(len(motifs))])
		prof.append([float(col.count(nuc)+1)/float(len(col)+4) for nuc in 'ACGT'])
	return prof

def motifs_from_profile(profile, dna, k):
	return [profile_most_probable_kmer(seq,k,profile) for seq in dna]

def randomized_motif_search(dna_list,k,t):
	rand_ints = [randint(0,len(dna[0])-k) for a in range(t)] #generate t random integers per string.
	motifs = [dna_list[i][r:r+k] for i,r in enumerate(rand_ints)] #generate t numbers of motifs in individual strings and store it in single list

	best_score = [score(motifs), motifs]

	while True:
		current_profile = profile_with_pseudocounts(motifs)
		motifs = motifs_from_profile(current_profile, dna_list, k)
		current_score = score(motifs)
		if current_score < best_score[0]:
			best_score = [current_score, motifs]
		else:
			return best_score


if __name__ == '__main__':
	best_motifs = [k*t, None]
	for repeat in range(1000):
		current_motifs = randomized_motif_search(dna,k,t)
		if current_motifs[0] < best_motifs[0]:
			best_motifs = current_motifs
	for seq in best_motifs[1]:
		print(seq)