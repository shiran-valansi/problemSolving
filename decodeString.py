def decodeString(s):
    """
    Given an encoded string, return its decoded string.
    You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

    >>> decodeString("3[a]2[bc]")
    'aaabcbc'

    >>> decodeString("3[a]10[bc]")
    'aaabcbcbcbcbcbcbcbcbcbc'

    >>> decodeString("3[a2[c]]")
    'accaccacc'

    >>> decodeString("2[abc]3[cd]ef")
    'abcabccdcdcdef'

    >>> decodeString("abc3[cd]xyz")
    'abccdcdcdxyz'

    """
        
    # for each char in string:
    # push chars into stack until we get a closing bracket
    # pop until we get opening bracket
    # pop until we get full number (might be more than 1 digit)
    # string to int
    # multiply and then push back into stack
    # continue reading the string
    # pop whats left in the stack and return
    
    stack = []
    
    for c in s:
        if c != ']':
            stack.append(c)
        else:
            
            word = get_word_to_encode(stack)
            num = get_num(stack)

            word = word * num
            stack.append(word)
    
    return concat_stack(stack)
            
            
def get_word_to_encode(stack):     

    word = ''
    while stack[-1] != '[':
        word = stack.pop() + word
    stack.pop()     
    return word


def get_num(stack):
    
    num = ''
    while stack and stack[-1].isdigit():
        num = stack.pop() + num
        
    return int(num)
        
    
def concat_stack(stack):
    
    result = ''        
    while stack:
        result = stack.pop() + result
    return result
                
if __name__ == "__main__":
    import doctest
    doctest.testmod()               