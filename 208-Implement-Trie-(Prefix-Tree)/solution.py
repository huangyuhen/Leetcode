class TrieNode(object):
    def __init__(self, k):
        """
        Initialize your data structure here.
        """
        self.word = False
        self.child = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in word:
            if i not in node.child:
                node.child[i] = TrieNode(i)
            node = node.child[i]
        node.word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        node = self.root
        for i in word:
            if i not in node.child:
                return False
            node = node.child[i]
        return node.word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for i in prefix:
            if i not in node.child:
                return False
            node = node.child[i]
        return True
# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")