'''
run-time: 236 ms (faster than 32.18%)
mem-usage: 33.9 mb (less than 6.15%)
'''

class TrieNode:
    
    def __init__(self):
        self.characters = [None] * 26
        self.endOfWord = False

class Trie:

    
    
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        
        curNode = self.root
        
        for c in word:
            
            idx = ord(c) - ord('a')
            
            if curNode.characters[idx] == None:
                curNode.characters[idx] = TrieNode()
            
            curNode = curNode.characters[idx]
        
        curNode.endOfWord = True
        

    def search(self, word: str) -> bool:
        
        curNode = self.root
        
        for c in word:
            
            idx = ord(c) - ord('a')
            
            if curNode.characters[idx] == None:
                return False
            else:
                curNode = curNode.characters[idx]
        
        return curNode.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        
        curNode = self.root
        
        for c in prefix:
            
            idx = ord(c) - ord('a')
            
            if curNode.characters[idx] == None:
                return False
            else:
                curNode = curNode.characters[idx]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
