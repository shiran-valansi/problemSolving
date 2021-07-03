# Given a class such as:



# And an input text file contains a list of words. The list contains all the words in the English language dictionary (approximately 600,000+ words). Example:
# ==================
# apple
# cat
# table
# dog
# from
# fish
# select
# selected

# ...
# ==================

# Implement the method  "findWords(String str)" so that when given any input string, return the valid words that were found in the text file and the indexes that they appear in this string

# Example:
# If an input string "abcSELECTxyzFrom123Table selected@567" was passed into the method findWords
# The program should be able to find the words and the indexes they appear in the string such as
# "select": 3, 25
# "from": 12
# "table": 19
# "selected": 25

# "apple"
# "app", "apple"

# {a: {p: {p:}}

from collections import defaultdict
from trie import Trie

class WordsFinder:

    def __init__(self, dictionary):

        self.trie = Trie()
        self.trie.insertMany(dictionary)
        self.trie.printTrie()
        # self.build_trie(dictionary)
        # self.trie = dictionary

    
    def findWords(self, s):

        results = defaultdict(list)

        for i, char in enumerate(s):
            # curr -> pointing to a
            curr = self.trie.root
            j = i
            while j< len(s) and s[j] in curr:
                # curr- > pointing to the values of key p (second)

                curr = curr[s[j]]
                j += 1

                # legal word ends with '*'
                if '*' in curr:
                    results[s[i:j]].append(i)

        print(results)



s = "apples"

dictionary = ["apples", "apple"]
finder = WordsFinder(dictionary)
finder.findWords(s)

# what the trie should look like:
# d = {'a': {'p': {'p': {'*':'*', 'l': {'e': {'*'}}}}}
# }
# finder = WordsFinder(d)
# finder.findWords(s)