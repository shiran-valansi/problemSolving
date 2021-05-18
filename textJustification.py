# Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters 
# and is fully (left and right) justified.

# You should pack your words in a greedy approach; as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left justified and no extra space is inserted between words.


#################### Better version after my coding skills improved ####################

def fullJustify(words, maxWidth):
    """
    For every word we see if it can be added to the current sentence- then add to a list of current words and ke3ep count of the number of letters
    If it cannot be added- turn the list of words we currently have into a sentence
    And our current word will start a new list of words

    >>> fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    ['This    is    an', 'example  of text', 'justification.  ']

    >>> fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
    ['What   must   be', 'acknowledgment  ', 'shall be        ']

    >>> fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)
    ['Science  is  what we', 'understand      well', 'enough to explain to', 'a  computer.  Art is', 'everything  else  we', 'do                  ']
    """

    par = []
    temp_words = []
    letter_count = 0
    
    for word in words:
        
        if can_add_word(word, temp_words, letter_count, maxWidth):
            temp_words.append(word)
            letter_count += len(word)
        else:
            sentence = words_to_sentence(maxWidth, temp_words, letter_count)
            par.append(sentence)
            
            temp_words= [word]
            letter_count = len(word)
                
    sentence = words_to_left_justified_sentence(maxWidth, temp_words, letter_count)
    par.append(sentence)
            
    return par
        
                
def can_add_word(word, temp_words, letter_count, maxWidth):
    
    return len(temp_words) + len(word) + letter_count <= maxWidth
    
                
def words_to_sentence(maxWidth, words, letter_count):
        
    if len(words) == 1:
        return words[0] + (' ' * (maxWidth - letter_count))
    
    space_count = (maxWidth - letter_count) // (len(words)-1)
    extra_space = (maxWidth - letter_count) % (len(words)-1)
    sentence = '' 
    
    for word in words[:-1]:
        sentence = sentence + word + (' ' * space_count)
        if extra_space > 0:
            sentence = sentence + ' '
            extra_space -= 1
    sentence = sentence + words[-1]
    
    return sentence
    
    
def words_to_left_justified_sentence(maxWidth, words, letter_count):
    
    space_count = maxWidth - letter_count - len(words) + 1
    sentence = ' '.join(words)
    sentence = sentence + ' ' * space_count
    
    return sentence
    




#####################################################################################################################

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