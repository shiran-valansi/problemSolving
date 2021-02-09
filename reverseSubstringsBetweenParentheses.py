def reverseParentheses(s):
    """
    You are given a string s that consists of lower case English letters and brackets. 

    Reverse the strings in each pair of matching parentheses, starting from the innermost one.

    Your result should not contain any brackets.

    >>> reverseParentheses("(abcd)")
    'dcba'

    >>> reverseParentheses("(u(love)i)")
    'iloveu'

    >>> reverseParentheses("(ed(et(oc))el)")
    'leetcode'


    >>> reverseParentheses("a(bcdefghijkl(mno)p)q")
    'apmnolkjihgfedcbq'
    
    """
    # put in a stack, char by char
    # if we get to a closing bracket, start poping from stack and reverse, also reversing substrings
    # until we get to an opening bracket, where we push back our reversed string
    # we finish when we've reached the end of the string
    # then we return our stack as a string

    if len(s) == 0:
        return s
    
    stack = [s[0]]
    i = 1
    while i< len(s):
        
        if s[i] != ')':
            stack.append(s[i])
        
        else:
            reverse = ''
            curr = stack.pop()
            while curr != '(':
                reverse = reverse + curr[::-1]
                curr = stack.pop()
                    
            # print(reverse)
            stack.append(reverse)
        # print(stack)
        
        i += 1

    reverse = ''.join(stack)
        
    return reverse


if __name__ == "__main__":
    import doctest
    doctest.testmod()