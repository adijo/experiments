class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        t = Trie()
        for word in A:
            t.insert(word)
        res = t.call()
        ans = {}
        for r in res:
            ans[r[1]] = r[0]
        result = []
        for word in A:
            result.append(ans[word])
        return result

class Trie:
    def __init__(self):
        self.root = {}
        
    def _construct_node(self):
        return {}

    def _insert_helper(self, word, curr, node):
        if curr == len(word) - 1:
            # something
            char = word[curr]
            if char in node:
                node[char] = (node[char][0], True, node[char][2] + 1)
            else:
                node[char] = (None, True, 1)
        else:
            # something else.
            char = word[curr]
            if node != None and char not in node:
                new_node = self._construct_node()
                node[char] = (new_node, False, 1)
                self._insert_helper(word, curr + 1, new_node)
            else:
                new_node = node[char][0]
                if new_node == None:
                    # something
                    new_node = self._construct_node()
                    node[char] = (new_node, False, 1)
                    self._insert_helper(word, curr + 1, new_node)
                else:
                    node[char] = (node[char][0], node[char][1], node[char][2] + 1)
                    self._insert_helper(word, curr + 1, new_node)

    def _search(self, node):
        if node == None:
            return ""
        else:
            k = None
            for key in node:
                k = key
                break
            k = k + self._search(node[k][0])
            return k

    def call(self):
        res = self.operation(self.root, "")
        return res

    def operation(self, node, buff):
        # find node with current capacity one, then search for the complete word.
        answers = []
        for key in node:
            if node[key][0] == None:
                answers.append((buff + key, buff + key))
            elif node[key][2] == 1:
                # found a candidate.
                rest = self._search(node[key][0])
                answers.append((buff + key, buff + key + rest))              
            else:
                # recurse further
                res = self.operation(node[key][0], buff + key)
                for results in res:
                    answers.append(results)
        return answers

    def insert(self, word):
        self._insert_helper(word, 0, self.root)
        
s = Solution()
print s.prefix(["zebra", "dog", "duck", "dove"])