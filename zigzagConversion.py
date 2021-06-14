from collections import defaultdict
def convert(s, numRows):
    """
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R
    And then read line by line: "PAHNAPLSIIGYIR"
    Write the code that will take a string and make this conversion given a number of rows

    >>> convert("PAYPALISHIRING", 3)
    'PAHNAPLSIIGYIR'

    >>> convert("PAYPALISHIRING", 4)
    'PINALSIGYAHRPI'

    >>> convert("A", 1)
    'A'

    """
    
    if numRows == 1:
        return s
        
    row_to_chars = defaultdict(list)
    i = 0
    going_down = True
    
    for char in s:
        
        row_to_chars[i].append(char)
        
        if i % (numRows-1) == 0:
            going_down = not going_down
        if going_down:
            i += 1
        else:
            i -= 1
    
    converted = []
    for row in row_to_chars:
        converted.extend(row_to_chars[row])
        
    return ''.join(converted)

def convert2(s, numRows):
    """
    >>> convert2("PAYPALISHIRING", 3)
    'PAHNAPLSIIGYIR'

    >>> convert2("PAYPALISHIRING", 4)
    'PINALSIGYAHRPI'

    >>> convert2("A", 1)
    'A'

    """
        
    if numRows == 1:
        return s
        
    row_to_chars = ['' for i in range(numRows)]
    i = 0
    
    direction = -1
    
    for char in s:
        
        row_to_chars[i] += char
        
        if i % (numRows-1) == 0:
            direction = -direction
            
        i += direction

    return ''.join(row_to_chars)
        

if __name__ == "__main__":
    import doctest
    doctest.testmod() 