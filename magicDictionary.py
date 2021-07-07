class MagicDictionary:
    """
    Design a data structure that is initialized with a list of different words. 
    Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.
    Notice, you must change exactly one character, and you cannot add a character.

    """
    def __init__(self):
        """
        we use a trie to keep the list of words
        """
        
        self.root = dict()

    def buildDict(self, dictionary) -> None:
        
        for word in dictionary:
            self.addWord(self.root, word)

        print(self.root)


    def addWord(self, curr, word):  

        for char in word:
            if char not in curr:
                curr[char] = dict()
            curr = curr[char]
                
        curr['*'] = word
        

    def search(self, searchWord: str) -> bool:
     
        if self.dfs(self.root, 0, searchWord):
            return True
        return False
        
        
    def dfs(self, curr, count, searchWord):
        
        if count > 1:
            return False

        if len(searchWord) == 0:
            if '*' in curr and count == 1:
                return True
            return False
    
        for char in curr:
                    
            if char == '*':
                continue

            if searchWord[0] != char:
                found = self.dfs(curr[char], count+1, searchWord[1:])
            else:
                found = self.dfs(curr[char], count, searchWord[1:])
                
            if found:
                return True


def main():
   
    dictionary = ["hello","hallo","leetcode","judge"]
    search_words = ["hello", "hallo", "hell", "leetcodd", "leetcoded", "judgeea"]
    expected_results = [True, True, False, True, False, False]

    my_dict = MagicDictionary()
    my_dict.buildDict(dictionary)

    for word, result in zip(search_words, expected_results):
        assert my_dict.search(word) == result


if __name__ == "__main__":
    main()     

