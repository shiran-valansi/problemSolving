def intToRoman(num):
    """
    Given an integer, return its roman representation

    >>> intToRoman(3)
    'III'

    >>> intToRoman(1994)
    'MCMXCIV'

    >>> intToRoman(1786)
    'MDCCLXXXVI'

    >>> intToRoman(500)
    'D'

    """
    ####### Simpler ########
    
    num_to_roman = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'   
    }

    romans = ''

    for base, roman in num_to_roman.items():
        
        romans += roman * (num // base)
        num = num % base
            
    return romans


if __name__ == "__main__":
    import doctest
    doctest.testmod() 