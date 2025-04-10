
import time

import binary_search as bs
import linear_search as ls

def time_one(f, n):
    ''' Time the given search algorithm with list of size n
    
    Creates a list of n items with a[i] == i, then searches
    for each element.

    This uses wall-clock time rather than process-specific
    CPU time, but should be close enough.

    The results are in milliseconds per function call.
    '''

    a = list(range(n))
    start = time.perf_counter_ns()
    for i,key in enumerate(a):
        if f(a, key) != i:
            print(f"search failed for i = {i}!")
    end = time.perf_counter_ns()
    return ((end - start) / 1000) / n

def main():
    n = int(input("Array size to test: "))

    bs_time = time_one(bs.index, n)
    ls_time = time_one(ls.index, n)

    print(f"{n},{bs_time:.3f},{ls_time:.3f}")

if __name__ == "__main__":
    main()
