# Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters 
# and is fully (left and right) justified.

# You should pack your words in a greedy approach; as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left justified and no extra space is inserted between words.


def textJustify(words, maxWidth):
    """
    >>> textJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    ['This    is    an', 'example  of text', 'justification.  ']

    >>> textJustify(["What","must","be","acknowledgment","shall","be"], 16)
    ['What   must   be', 'acknowledgment  ', 'shall be        ']

    >>> textJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)
    ['Science  is  what we', 'understand      well', 'enough to explain to', 'a  computer.  Art is', 'everything  else  we', 'do                  ']
    """
    
    curr = words[0]
    sentence = curr
    text = []
    i = 1
    
    while i < len(words):
        word = words[i]
        if len(sentence) == 0 and len(word) == maxWidth:
            sentence = word
            i += 1
        elif len(sentence) + len(word) + 1 <= maxWidth:
            sentence = sentence + ' ' + word
            sentence = sentence.lstrip()
            i+= 1 
            
        else:
            sentence = add_extra_spaces(sentence, maxWidth)
            text.append(sentence)
            sentence = ''

    # take care of last sentence
    if len(sentence) > 0:
        text.append(left_align(sentence, maxWidth))
    else:
        text[-1] = left_align(text[-1], maxWidth)
    
    return text

def count_chars(words):
    count = 0
    for word in words:
        count += len(word)
    return count

def get_list_of_spaces(words, width_left):
    
    blocks_of_spaces = len(words) - 1
    if blocks_of_spaces == 0:
        return [' '*width_left]
    
    spaces = width_left // blocks_of_spaces
    extra_spaces = width_left % blocks_of_spaces

    spaces_list = [" " * spaces]* blocks_of_spaces
    i = 0
    while i < extra_spaces:
        spaces_list[i] = spaces_list[i] + ' ' 
        i += 1
    return spaces_list

def add_extra_spaces(sentence, maxWidth):
                
    words = sentence.split()
    width_left = maxWidth - count_chars(words) 
        
    spaces_list = get_list_of_spaces(words, width_left)    
    
    new_sentence = words[0]
    if len(words) == 1:
        return new_sentence + spaces_list[0]
    i = 0
    for word in words[1:]:
        new_sentence = new_sentence + spaces_list[i] + word
        i += 1
    return new_sentence

def left_align(sentence, maxWidth):
    words = sentence.split()
    new_sentence = ' '.join(words)
    spaces_left = maxWidth - len(new_sentence)
    new_sentence = new_sentence + ' '*spaces_left
    return new_sentence
        
    


if __name__ == "__main__":
    import doctest
    doctest.testmod()