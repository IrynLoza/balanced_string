""":
>>> balanced_string('azABaabza')
5
>>> balanced_string('TocoCat')
-1
>>> balanced_string('AcZCbaBz')
8
>>> balanced_string('abcdefghijklmnopqrstuvwxyz')
-1
"""

def check_register(s):
    for i in range(len(s)):
        if s[i].islower() and s[i].upper() not in s:
            return False
        if s[i].isupper() and s[i].lower() not in s:
            return False
    return True

def balanced_string(s):
    min_num = len(s)
    isMin = False
    for i in range(len(s)+1):
        for j in range(i+1, len(s)+1):
            if check_register(s[i:j]) and min_num >= j-i:
                min_num = j-i
                isMin = True
    if isMin:
        return min_num
    return -1




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ROCK STAR! ALL TESTS PASSED!\n')
