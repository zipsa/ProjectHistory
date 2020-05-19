'''
 Implement Neighbors to find the d-neighborhood of a string.

Input: A string Pattern and an integer d.
Output: The collection of strings Neighbors(Pattern, d).
(You may return the strings in any order, but each line should contain only one string.)

Sample Input:
ACG
1

Sample Output:
CCG TCG GCG AAG ATG AGG ACA ACC ACT ACG
'''

# Idea: use set because we dont need order.
# .union()in set will collect all elements but avoid dubplicate element automatically.
# use string slilcing + concatenation in for loop.
# The original answer suggested to use hamming distance.

with open("data/dataset_3014_4.txt") as file:
    data = file.read().split('\n')

def immediate_neighbors(pattern):
    neighbor = set()
    nset = {'A', 'C', 'G', 'T'} #set
    for i in range(len(pattern)):
        for n in nset:
            neighbor.add(pattern[:i] + n + pattern[i+1:])
    return neighbor

def neighbors(pattern, d):
    if d == 0:
        return pattern
    elif d == 1:
        return immediate_neighbors(pattern)
    elif d >= 2:
        #first iteration
        ineighbor = immediate_neighbors(pattern)
        neighbor = ineighbor
        #from send iteration
        for j in range(d-1):
            for p in ineighbor:
                neighbor = neighbor.union(immediate_neighbors(p))
            ineighbor = neighbor
    return neighbor

if __name__ == "__main__":
    print(' '.join(neighbors(data[0], int(data[1]))))

