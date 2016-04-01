#Countdown Letters Game Solver

##Student name (David Hynes)

##Student number (G0295205)

##Date (29th March 2016)


The "Countdown Letters Game" is a word game based on obtaining the longest word derived from a set of nine letters. The set of letters comprises of a selection that must include at least 4 consonants and 3 vowels,whilst the remaining 2 letters are a mix of either types.

As the solver is based on the Countdown game to solver the "word" I set a function to produce a string of 9 letters, matching the above which is then passed to to the solver. The string is checked against a list of words in "wordsList.txt" file.

##Background


##Words list

My words list is in the file wordslist.txt in this repoistory. I search on line for a ready made words list and found a downloadable zip fie at http://dreamsteep.com/downloads/word-games-and-wordsmith-utilities/120-the-english-open-word-list-eowl.html. The file came as a cvs and was split into lettered files, so when unzipped it held 26 files.I then ran code to read each file and write it one dictionary txt file. code was obtained from http://codereview.stackexchange.com/questions/81990/manipulating-csv-files-to-regular-text-file. I ammened the cose to remove blank lines amd numberingwhich would of repeated throught the new txt file.



##Python script

My script is in the files WordGame.py in this repository.

My script is in the files solver.py in this repository and it works as follows. 

When run in your terminal as "python3 WordGame.py" the game will generate a random 9 letter word which will be used. This word will be passed to the finder. The second stage is a map of is generated to check the list of words from the dictionary   
The most important section is:

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

dave@dave-Aspire:~/Documents/CountdownGame$ python3 WordGame.py
completed
Generated leters are: aaddeeiqr
['readied']
Time taken:
8.150018402375281e-07
dave@dave-Aspire:~/Documents/CountdownGame$ 

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
