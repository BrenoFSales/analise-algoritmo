def merge(A,p,q,r):
    '''
        A is the entry array,
        p is the init of the array,
        q is the half init of the array 
        and r is the end index of the array
    '''
    temp, _temp = (q - p + 1), (r - q)
    l  = [n for n in range(1, temp + 1)] 
    _r = [m for m in range(1, _temp + 1)]
    
    for i in range(temp):
        l[i] = A[p + i - 1]
    for j in range(_temp):
        _r[j] = A[q + j]
    
    l.append(0.1)
    _r.append(0.1)
    i = 0
    j = 0
    for k in range(r):
        if l[i] <= _r[j]:
            A[k] = l[i]
            i += 1
        else:
            A[k] = _r[j]
            j += 1
    return A

def merge_sort(A,p,r):
    p += 1
    if p < r:
       q = int((p + r) / 2)
       merge_sort(A,p,q)
       merge_sort(A,q + 1, r)
       merge(A, p, q, r)
    return A

def main():
    A = [6,2,1,4,5,8,7,9,10, 3]
    A = merge_sort(A, 0, len(A))
    print(A)
    
if __name__ == '__main__':
    print('initiating . . .')
    main()
    print('ended.')
