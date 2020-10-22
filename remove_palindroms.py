def remove_palindroms(spells):
    sp = []
    for word in spells:
        k = ''.join(word.lower().split())
        print(k, k[::-1])
        if k == k[::-1]:
            sp.append(word)
    for word in sp:
        if word in spells:
            spells.remove(word)
