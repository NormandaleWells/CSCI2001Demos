
def index(a, key):
    ''' Returns the smallest index idx such that
    a[idx] == key, or None if not such index exists.
    
    '''
    for i,n in enumerate(a):
        if n == key:
            return i
    return None
