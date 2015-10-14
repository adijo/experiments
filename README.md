# Experiments

Programming exercises done during my spare time for fun and learning.

# Current Content

* ## Recursive Descent Parser: 
  A basic recursive descent parser that accepts strings that conform to the following productions
  
  ```
  E -> T | T + E
  T -> int | int * T | ( E )
  ```
  
* ## Binary Search Tree Iterator: 
  The implemented iterator has a `hasNext` and `next` method that yields elements in an in-order fashion.
  
* ## Evaluate Expression: 
  The implemented expression evaluator takes in a simple expression of the form `(3 + 2) - 1` and evaluates it, in this case yielding an answer of `4.`
  This is done by first tokenizing the input, then converting it into the **reverse polish notation** or the postfix notation and then evaluate it using a **stack.**
  
* ##Longest Word: 
  This is a problem that I encountered in the book: Cracking the Coding Interview. Given a list of words, the algorithm finds the length of the longest word
  that can be made up from the words in the given list. For example, in the list
  
  ```
  words = ["cat", "banana", "dog", "nana", "walk", "walker", "dogwalker"]
  
  ```
  The answer is `dogwalker.` This was solved using **dynamic programming.** (I know, fancy word for caching results.)
  
* ## Print matrix in a spiral order.

  ```
  1 2 3
  4 5 6
  7 8 9
  ```
  Answer in this case is `1 2 3 6 9 8 7 4 5.`
  
* ## Tram probability: 
  Modelling the probability of getting optimal number of 
  visits by police officers in a tram.
  1. `k` are the number of stops travelled by the average traveler.
  2. `p` is the probability of an officer entering station at stop `i` in
   range `[1..k]`
  3. `n` are the number of passengers travelling without tickets in the day.
  4. Another parameter, say `q`, that gives us the percentage of people
   that we want to catch. Example: If `q = 0.5`, that would mean that we 
   expect that out of n people travelling without tickets, `n/2` SHOULD be caught
   in expectation.
  5. The problem would then boil down to estimate the value of the parameter `p.`

