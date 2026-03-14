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
    
    i = 1
    j = 1
    for i in range(temp):
        l[i] = A[p + i - 1]
    for j in range(_temp):
        _r[j] = A[q + j]
    
    l.append(10**10)
    _r.append(10**10)
    _i = 1
    _j = 1
    for k in range(r):
        if l[_i] < _r[_j]:
            A[k] = l[_i]
            _i += 1
        elif _r[_j] > l[_i]:
            A[k] = _r[_j]
            _j += 1

def merge_sort(A,p,r):
    if p < r:
       q = int((p + r) / 2)
       merge_sort(A,p,q)
       merge_sort(A,q + 1, r)
       merge(A, p, q, r)

def main(A):
    print('initiating with sample array: ', A)
    merge_sort(A, 1, len(A))
    print('ended result: ', A)

if __name__ == '__main__':
    A = [6,2,1,4,5,8,7,9,10,3]
    main(A)
