#Countdown Letters Game Solver

##Student name (David Hynes)

##Student number (G0295205)

##Date (29th March 2016)


The "Countdown Letters Game" is a word game based on obtaining the longest word derived from a set of nine letters. The set of letters comprises of a selection that must include at least 4 consonants and 3 vowels,whilst the remaining 2 letters are a mix of either types.

As the solver is based on the Countdown game to solver the "word" I set a function to produce a string of 9 letters, matching the above which is then passed to to the solver. The string is checked against a list of words in "wordsList.txt" file.

##Background

The first task I completed as part of this project was to Google "countdown letters game solver". Google gave me two relevant results on the first page, these are Cool Project name and Cool Solver.

##Words list

My words list is in the file wordslist.txt in this repoistory. I got my words list is from a previous project that was to reproduce the "Zimmerman code breaker". As this file is constant there is no need to regenerate it every time the code is run, however it may be necessary to check this against a current dictionary from time to time as new words are ad every so often.

(the Oxford Learner's Dictionaries website)

##Python script

My script is in the fies solver.py in theis repository

My script is in the files solver.py in this repository and it works as follows. The most important section is:

import random
print(random.shuffle("My code is cool."))
Previously it looks like this:

### Note that the following snippet of code was adapted from
### the Stack Overflow post available here: http://www.so.com/post/123
import nothing
That didn't work too well, so I changed it.

##Preprocessing

My script does a lot of preprocessing, which only needs to be run once. Once the preprocessing is done we can run the game solver again and again without that overhead.

##Efficiency

Here's some stuff about how efficient my code is, including an analysis of how many calculations my algorithm requires.

##Results

My script runs very quickly, and certainly within the 30 seconds allowed in the Coutdown letters game.

##References
Raw  solver.py
## This is the function that actually checks the random letters for words.
def check(letters):
  while (letters):
    letters.pop()
  return []

### This function is just a wrapper that shows how my script works.
### It does the preprocessing, then creates a random list of letters, and finally runs the solver.
