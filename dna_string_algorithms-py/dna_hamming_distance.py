'''
Hamming Distance Problem: Compute the Hamming distance between two strings.

Input: Two strings of equal length.
Output: The Hamming distance between these strings.

Sample Input:

GGGCCGTTGGT
GGACCGTTGAC

Sample Output:

3
'''

#hamming_distance1 and hamming_distance2 does the same thing.

dat = []
with open("data/dataset_9_3.txt") as file:
    for line in file:
        dat.append(line[:-1])

#Compare distance of two DNA strings with same length.
def hamming_distance1 (s1, s2):
    score = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            score +=1
    return score

#Alternative approach
def hamming_distance2(s1, s2):
    count = sum(1 for a, b in zip(s1, s2) if a != b)
    return count

if __name__ == '__main__':
    ans = hamming_distance2(dat[0],dat[1])
    print (ans)


