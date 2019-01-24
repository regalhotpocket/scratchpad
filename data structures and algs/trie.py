from collections import namedtuple
def trieinsert(t, k, v):
    cur = t
    for c in k:
        if not c in cur[1]:
            cur[1][c] = [None, {}]
        cur = cur[1][c]
    cur[0] = v
def trieget(t, k):
    cur = t
    for c in k:
        if not c in cur[1]:
            return None
        cur = cur[1][c]
    return cur[0]
def trieexists(t, k):
    cur = t
    for c in k:
        if not c in cur[1]:
            return False
        cur = cur[1][c]
    return True
def triedel(t, k):
    cur = t
    for c in k[:-1]:
        if not c in cur[1]:
            return None
        cur = cur[1][c]
    if k[-1] in cur[1]:
        val = cur[1][k[-1]][0]
        del cur[1][k[-1]]
        return val
    return None
t = [None, {}]
trieinsert(t, 'a', 1)
trieinsert(t, 'ab', 2)
print("inserted a 1, ab 2")
print("get ab", trieget(t, 'ab'))
print("exsits ab", trieexists(t, 'ab'))
print("delete ab", triedel(t, 'ab'))
print("get ab", trieget(t, 'ab'))
print("exists ab", trieexists(t, 'ab'))
print("get a", trieget(t, 'a'))
print("exists a", trieexists(t, 'a'))