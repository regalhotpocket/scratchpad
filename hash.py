def hash(data):
    result = 0
    for c in data:
        result += ord(c)
    return result
def hash_insert(table, key, value):
    table["current"] += 1
    if table["current"]/len(table["content"]) > 0.75:
        new_content = [[] for x in range(2*len(table["content"]))]
        for old in table["content"]:
            for old_key, old_value in old:
                index = hash(old_key)%len(new_content)
                new_content[index].append((old_key, old_value))
        table["content"] = new_content
    index = hash(key)%len(table["content"])
    table["content"][index].append((key, value))
def hash_get(table, key):
    index = hash(key)%len(table["content"])
    bucket = table["content"][index]
    for k in bucket:
        if k[0] == key:
            return k[1]
    return None
table = {"content": [[],[]], "current":0}
hash_insert(table, "a", 1)
hash_insert(table, "b", 2)
hash_insert(table, "c", 3)
hash_insert(table, "d", 4)
hash_insert(table, "e", 5)
print(hash_get(table, "a"))
print(hash_get(table, "b"))
print(hash_get(table, "c"))
print(hash_get(table, "d"))
print(hash_get(table, "e"))