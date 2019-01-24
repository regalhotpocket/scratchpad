
def minheapinsert(h, v):
    cur = len(h)
    h.append(v)
    while cur > 0:
        p = (cur-1)//2
        if h[p] > h[cur]:
            h[p], h[cur] = h[cur], h[p]
        else:
            break
        cur = p

heap = []
minheapinsert(heap, 3)
minheapinsert(heap, 2)
minheapinsert(heap, 1)
minheapinsert(heap, 2)
print(heap)