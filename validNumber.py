################## Straight forward ##################
def isNumber(s: str) -> bool:
        s = s.lower()
        parts = s.split('e')
        if len(parts) > 2:
            return False
        if len(parts) == 2:
            if len(parts[0]) == 0 or len(parts[1])== 0:
                return False
            if parts[1][0] == '+' or parts[1][0] == '-':
                parts[1] = parts[1][1:]
            if parts[0][0] == '+' or parts[0][0] == '-':
                parts[0] = parts[0][1:]
            return is_dec_or_int(parts[0]) and is_int(parts[1])

        
        if parts[0][0] == '+' or parts[0][0] == '-':
            parts[0] = parts[0][1:]
            
        return is_dec_or_int(parts[0]) 
        
def is_dec_or_int(s):
    
    parts = s.split('.')
    if len(parts) > 2:
        return False
    if len(parts) == 2:
        if len(parts[0]) == 0:
            return is_int(parts[1])
        if len(parts[1]) == 0:
            return is_int(parts[0])
        return is_int(parts[0]) and is_int(parts[1])
    
    return is_int(parts[0])
    

def is_int(s):
    return s.isdigit()


################## DFA- Deterministic Finite Atomation  ##################
def isNumber2(s: str) -> bool:
    # state is a list where every index represents a state (hashmap), 
    # and every key's value in the state represents the next state/ index
    state = [{'sign':2, 'point':3, 'digit':1},
            {'point':4,'digit':1, 'e':5 },
            {'point':3,'digit':1},
            {'digit':8},
            {'e':5, 'digit': 9},
            {'sign':6, 'digit':7},
            {'digit':7},
            {'digit':7},
            {'digit':8, 'e':5},
            {'digit': 9, 'e': 5}
        
    ]
        
    curr_state = 0
    
    for c in s:
        if c in {'+', '-'}:
            c = 'sign'
            
        elif c == '.':
            c = 'point'
            
        elif c.isdigit():
            c = 'digit'
            
        elif c in {'e', 'E'}:
            c = 'e'
            
        if c not in state[curr_state]:
            return False
        
        curr_state = state[curr_state][c]   
        
    if curr_state in {1, 4, 8, 7, 9}:
        return True
    
    return False


valid = ["2",  "3.", "0089", "-0.1", "0.8", "-1.", "+3.14", "1.431352e7", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
not_valid = ["abc", "0e", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

for v in valid:
    assert (isNumber2(v))
    assert (isNumber(v))

for s in not_valid:
    assert (not isNumber2(s))
    assert (not isNumber(s))