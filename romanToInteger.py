def romanToInt(s):
    """
    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer.

    >>> romanToInt("III")
    3

    >>> romanToInt("IV")
    4

    >>> romanToInt("LVIII")
    58

    >>> romanToInt("MCMXCIV")
    1994

    """
        
    roman_to_int = { 
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    num = 0
    
    for i in range(len(s)-1):
        
        if roman_to_int[s[i]] < roman_to_int[s[i+1]]:
            num -= roman_to_int[s[i]]
        else:
            num += roman_to_int[s[i]]
            
    num += roman_to_int[s[-1]]
    return num

if __name__ == "__main__":
    import doctest
    doctest.testmod()