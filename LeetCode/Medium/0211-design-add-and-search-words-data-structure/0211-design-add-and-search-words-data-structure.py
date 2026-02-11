class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = Node()
            curr = curr.children[i]
        
        curr.end = True
        

    def search(self, word: str) -> bool:
        
        def walk(i, node):

            if i == len(word)-1:
                if node and (word[i] == "." or word[i] in node):
                    return True if word[i] == "." else node[word[i]].end
                return False

            if word[i] != ".":
                if word[i] not in node:
                    return False
                return walk(i+1, node[word[i]].children)

            for child in node:
                if walk(i+1, node[child].children):
                    return True

            return False

        return walk(0, self.root.children)

            

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)