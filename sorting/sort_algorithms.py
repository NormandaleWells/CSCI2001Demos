
import random
import time

def min_element(a, lo, hi):
    ''' Return the index of the minimum element of a.

    If there is more than one occurence of the
    minimum element, the first one (the one with
    the lowest index) is returned'''
    if hi - lo == 0: return None
    min_idx = lo
    for i in range(lo, hi):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def swap(a, idx1, idx2):
    ''' Swap a[idx1] with a[idx2].'''
    a[idx1], a[idx2] = a[idx2], a[idx1]

def selection_sort(a):
    ''' Sort list a using the selection sort algorithm.'''
    for i in range(len(a)):
        min_idx = min_element(a, i, len(a))
        swap(a, i, min_idx)

def upper_bound(a, lo, hi, key):
    ''' Return the index of the first element of a greater than key.
    
    Two important details (let ret be the return value)
        a[ret] != key
        ret may be len(a)
    '''
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] < key:
            lo = mid + 1
        elif a[mid] > key:
            hi = mid
        else:
            return mid
    return hi

def rotate_right(a, lo, hi):
    ''' Rotate a[lo:hi] right one position.
    
    The last element of the range (a[hi-1]) is moved
    to a[lo].'''
    if hi - lo < 2: return
    i = hi - 1
    t = a[i]
    while i > lo:
        a[i] = a[i-1]
        i -= 1
    a[lo] = t

def insertion_sort(a):
    ''' Sort a using the insertion sort algorithm.
    
    This version uses upper_bound to find the position
    to insert each element, and rotate_right to move
    that element into place.
    '''
    for i in range(1, len(a)):
        idx = upper_bound(a, 0, i, a[i])
        rotate_right(a, idx, i+1)

def is_sorted(a):
    ''' Return True if a is sorted, False otherwise.'''
    for i in range(1, len(a)):
        if a[i] < a[i-1]:
            return False
    return True

def insertion_sort_2(a):
    ''' Sort a using the insertion sort algorithm.
    
    This version uses moves the element being inserted
    back through the array one element at a time.
    '''
    for i in range(1, len(a)):
        j = i
        t = a[j]
        while j > 0 and a[j-1] > t:
            a[j] = a[j-1]
            j -= 1
        a[j] = t

def merge(a1, a2, a):
    '''Merge sorted arrays a1 and a2 into a.
    
    This code assumes that len(a1) + len(a2) == len(a).'''
    i = 0
    j = 0
    for k in range(len(a)):
        if i == len(a1):
            a[k] = a2[j]
            j += 1
        elif j == len(a2):
            a[k] = a1[i]
            i += 1
        elif a1[i] <= a2[j]:
            a[k] = a1[i]
            i += 1
        else:
            a[k] = a2[j]
            j += 1

def mergesort(a):
    ''' Sort a using the mergesort algorithm.
    
    This could be made considerably more efficient
    by using an auxiliary array rather than creating
    two list slices with each recursuve call.
    '''
    if len(a) <= 1: return
    mid = len(a) // 2
    a1 = a[mid:]
    a2 = a[:mid]
    mergesort(a1)
    mergesort(a2)
    merge(a1, a2, a)

def time_1_sort(name, alg, a):
    ''' Sort list a using algorithm alg, with the given name.
    
    I have no idea what the clock resolution is here, but as
    long as times are some number of seconds, it's probably
    fairly accurate.
    '''
    t = a[:]
    start = time.time()
    alg(t)
    end = time.time()
    if not is_sorted(t):
        print(f"{name} failed")
    else:
        elapsed = end - start
        print(f"{name} : {elapsed:.4f}")

def test():
    # a = [27, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214]
    a = [i for i in range(1000000)]
    random.shuffle(a)

    # time_1_sort("  selection sort", selection_sort, a)
    # time_1_sort("  insertion sort", insertion_sort, a)
    # time_1_sort("insertion sort 2", insertion_sort_2, a)
    time_1_sort("      merge sort", mergesort, a)

if __name__ == "__main__":
    test()
