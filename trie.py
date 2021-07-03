class Trie:
    """
    Implement a Trie- prefix tree

    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        print("Inserting ", word)
        word = word.lower()
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = dict()
            curr = curr[char]
            
        curr['*'] = {}
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for char in word:
            if char not in curr:
                print(word, "not in trie")
                return False
            curr = curr[char]
            
        if '*' in curr:
            print(word, "found in trie")
            return True
        print(word, "not in trie")
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for char in prefix:
            if char not in curr:
                print("This prefix is not in the trie: ", prefix)
                return False
            curr = curr[char]
        print("Found the prefix: ", prefix)
        return True
        
        
my_trie = Trie()

tasks = ["insert","search","search","startsWith","insert","search"]
words = ["apple","apple","app","app","app","app"]
results = []

for task, word in zip(tasks, words):
    if task == "insert":
        results.append(my_trie.insert(word))
    elif task == "search":
        results.append(my_trie.search(word))
    elif task == "startsWith":
        results.append(my_trie.startsWith(word))
print(results)


