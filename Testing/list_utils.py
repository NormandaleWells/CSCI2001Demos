
def find(a, item):
    for i in range(len(a)):
        if a[i] == item:
            return i
    return None

def count(a, item):
    count = 0
    for i in range(len(a)):
        if a[i] == item:
            count += 1
    return count

def min_element(a):
    if len(a) == 0:
        return None
    min_idx = 0
    for i in range(1, len(a)):
        if a[i] > a[min_idx]:
            min_idx = i
    return min_idx

def max_element(a):
    if len(a) == 0:
        return None
    max_idx = 0
    for i in range(1, len(a)):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx
