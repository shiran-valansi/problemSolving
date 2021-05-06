def compress(chars):
    """
    Compress the given string in place with O(1) space and return its new length

    >>> compress(["a","a","b","b","c","c","c"])
    6

    >>> compress(["a","b","c"])
    3

    >>> compress(["a"])
    1

    >>> compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
    4

    """
        
    count = 1
    write = 0
    
    for i in range(1,len(chars)):
        if chars[i] == chars[i-1]:
            count += 1
        else:
            chars[write] = chars[i-1]
            if count > 1:
                for c in str(count):
                    write += 1
                    chars[write] = c
            write += 1        
            count = 1
        
    if len(chars) > 1:
        chars[write] = chars[-1]
        if count > 1:
            for c in str(count):
                write += 1
                chars[write] = c
            
    chars = chars[:write+1]
            
    return write+1
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()       