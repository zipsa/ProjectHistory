#Solve the same problems with enumerate and numpy
import numpy as np

def gc_skew(seq):
    skew_dict = {'A': 0, 'T': 0, 'C': -1, 'G': 1}
    skew_list = [0] #Define first value as 0
    for pos, val in enumerate(seq):
        skew_list.append(skew_list[pos] + skew_dict[val])
    return skew_list


def minimum_gc_skew(seq):
    arr = np.array(gc_skew(seq))
    #print(type(array))
    #print(type(np.where(array == array.min())))
    return np.where(arr == np.amin(arr))[0]

def maximum_gc_skew(seq):
    arr = np.array(gc_skew(seq))
    return np.where(arr == np.amax(arr))[0]

with open("data/dataset_7_6.txt") as file:
    genome = file.read().split('\n')

print(minimum_gc_skew(genome[0]))

print("Minimun skew for quiz answer:", minimum_gc_skew("CATTCCAGTACTTCATGATGGCGTGAAGA"))
print("Maximum skew for quiz answer:", maximum_gc_skew("CATTCCAGTACTTCATGATGGCGTGAAGA"))