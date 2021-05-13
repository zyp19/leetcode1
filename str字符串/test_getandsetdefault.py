def find(s):
    target={}
    for c in s:
        # 是计算字典中每个键的值，如果键不存在的话，将该值置0，相当于为键做了一个初始化的操作。
        # target[c] = target.setdefault(c, 0)+1
        target[c] = target.get(c, 0) + 1
    values = target.values()
    print(values)
find("abababa")