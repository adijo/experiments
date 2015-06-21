"""
Author: Aditya Joshi
Finds the length longest word that can be made up from
words in the given list.
Few more optimizations are possible.
"""


def longest(words):
    words = sorted(words, key = len, reverse = True)
    dictionary = set(words)
    dp = {}
    answer = longest_dp(words[0], dictionary, dp)
    for i in xrange(1, len(words)):
        answer = max(answer, longest_dp(words[i], dictionary, dp))
    return answer

def longest_dp(word, dictionary, dp):
    if len(word) == 0:
        return 0
    elif word in dp:
        return dp[word]
    else:
        answer = 0
        for candidate in dictionary:
            if len(candidate) <= len(word) and word[:len(candidate)] == candidate:
                answer = max(answer, 1 + longest_dp(word[len(candidate) : ], dictionary, dp))
        dp[word] = answer
        return answer

words = ["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker"]
print longest(words)
