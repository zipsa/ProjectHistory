def entropy(motifs):
    profile = {}
    # check that all motifs are the same length
    list_length = len(motifs)
    l1 = len(motifs[1])  # length of the first motif
    print('There are {} motifs of length {}'.format(list_length, l1))
    for i in range(len(motifs)):
        if len(motifs[i]) != l1:
            short_motif = motifs[i]
            short_motif_len = len(short_motif)
            print('Oops, Motif {} is {} nucleotides instead of {}!'.format(short_motif, short_motif_len, l1))
            break

    # fill all positions with frequency of 0
    for nucleotide in 'ACGT':
        values = [0] * l1 #generate a list with 0 in it x l1 length
        profile[nucleotide] = values #dictionary containing nucleotide and list consist of 0

    # iterate through each position in the motif matrix, counting nucleotide frequencies
    total_entropy = 0
    for key, values in profile.items():
        for m in motifs:
            for i in range(len(m)):
                if m[i] == key:
                    profile[key][i] += 1

        # convert nucleotide frequencies to probabilities
        for i in range(len(values)):
            profile[key][i] = profile[key][i] / float(list_length)

        # calculate total entropy (Sum of (Prob_value * log2 Prob_n))
        import math
        for value in values:
            if value > 0:
                total_entropy += abs(value * math.log(value, 2))
            else:
                continue

    return (total_entropy)


motifs1 = [
    "TCGGGGGTTTTT",
    "CCGGTGACTTAC",
    "ACGGGGATTTTC",
    "TTGGGGACTTTT",
    "AAGGGGACTTCC",
    "TTGGGGACTTCC",
    "TCGGGGATTCAT",
    "TCGGGGATTCCT",
    "TAGGGGAACTAC",
    "TCGGGTATAACC"
]

print(entropy(motifs1))