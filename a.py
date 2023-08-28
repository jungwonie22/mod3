def palindrom(word):
    first = []
    second = []
    for i in word:
        first.append(i)
    for a in reversed(word):
        second.append(a)
    if first == second:
        print(True)
    else:
        print(False)
palindrom('шалаш')