# The question was: given a dictionary ( array of English words) and a prefix as an input, return true if dictionary has the prefix?

# For my brute forcesolution I looped over the dictionary and used startsWith method, 
# and then tried to improve my solution by sorting the dictionary first. 
# However the interviewee told me i can find a better solution which uses log(k) time complexity where k is the length of the longest word. 
# i couldn't come up with a solution with O(log(k)). Can anyone help me? (I was coding in javascript)


# Solution
# Trie created O(nlogk), and search is O(k)


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True