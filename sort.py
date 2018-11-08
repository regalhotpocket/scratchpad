from random import randint

def mergesort(l):
    if len(l) < 2:
        return l
    lhs = mergesort(l[:len(l)//2])
    rhs = mergesort(l[len(l)//2:len(l)])
    result = []
    lhs_cur = 0
    rhs_cur = 0
    while lhs_cur < len(lhs) and rhs_cur < len(rhs):
        if lhs[lhs_cur] < rhs[rhs_cur]:
            result.append(lhs[lhs_cur])
            lhs_cur += 1
        else:
            result.append(rhs[rhs_cur])
            rhs_cur += 1
    result += rhs[rhs_cur:] + lhs[lhs_cur:]

    return result

def partition(l, s, e):
    p = l[randint(s,e)]
    i = s - 1
    j = e + 1
    while True:
        i += 1
        while l[i] < p:
            i += 1
        j -= 1
        while l[j] > p:
            j -= 1
        if i >= j:
            return j
        l[i], l[j] = l[j], l[i]
def quicksort(l, start=0, end=None):
    if end == None:
        end = len(l)-1
    if start < end:
        p = partition(l, start, end)
        quicksort(l, start, p)
        quicksort(l, p+1, end)
    return l

for i in range(10):
    l = [randint(0,9) for x in range(10)]
    correct = sorted(l)
    original = l[:]
    if mergesort(l) != correct:
        print("merge sort incorrect")
    if quicksort(l) != correct:
        print(l, original, correct)
        print("quick sort incorrect")
def in_place(l):
    l[0] +=1