
def index(a, key):
    ''' Returns an index idx such that a[idx] == key,
    or None if there is no such index.
    
    If there are multiple such indices, the one returned
    is indeterminate.

    The list MUST be sorted.  Otherwise the code will not
    fail, but the results will be unpredicable.
    '''
    lo = 0
    hi = len(a)

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if key < a[mid]:
            hi = mid
        elif key > a[mid]:
            lo = mid + 1
        else:
            return mid
    return None


def index_cc(a, key):
    ''' index() with comparison count'''
    lo = 0
    hi = len(a)
    cc = 0

    while lo < hi:
        cc += 1
        mid = lo + (hi - lo) // 2
        if key < a[mid]:
            hi = mid
        elif key > a[mid]:
            lo = mid + 1
        else:
            return mid,cc
    return None,cc
