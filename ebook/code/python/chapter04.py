def strstr(haystack, needle):
    """
    >>> strstr("abcdf", "cd")
    True
    >>> strstr("abcdf", "ef")
    False
    """
    return any(
        all((haystack[i + j] == needle[j] for j in xrange(0, len(needle))))
        for i in xrange(0, len(haystack) - len(needle) + 1))


def find_no_repeat_char(string):
    """
    >>> find_no_repeat_char('abaccdeff')
    ['b', 'd', 'e']
    """
    maxchar = 256
    charlst = [0 for i in xrange(maxchar)]
    for c in string:
        charlst[ord(c)] += 1
    return [chr(i) for i in xrange(0, maxchar) if charlst[i] == 1]
