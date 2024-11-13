'''
1-
a) [2, 1, 4, 3, 'c', 'a', 'b']
b) [2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 'c', 'a', 'b', 'c', 'a', 'b']
c) 1
d) [1, 4]
e) [2, 1, 4, 3, 'b']
'''

#2-
import random

def shuffle_fisher_yates(myList):
    shuffled_list = myList[:]
    n = len(shuffled_list)
    
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        shuffled_list[i], shuffled_list[j] = shuffled_list[j], shuffled_list[i]

    return shuffled_list

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:", myList)


shuffled_list = shuffle_fisher_yates(myList)
print("Shuffled List:", shuffled_list)
