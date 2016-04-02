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

##Efficiency and Results

Here's some stuff about how efficient my code is, showing the time taken for algorithm to 1) generate a the required letters that will be used, 2) generate a list/map from the wordlist.txt file which will be the dictionary to check against, 3) generate all the possible combinations of letter that are betwen 3 and 9 letters in length, 4) pass the generated letters into the searching method, 5) check all the posible matches, and 6) pass back a result (list, if more that 1 possiblity of match).

dave@dave-Aspire:~/Documents/CountdownGame$ python3 WordGame.py
completed

Generated leters are: aaddeeiqr

returned ['readied']

Time taken: 

###8.150018402375281e-07

dave@dave-Aspire:~/Documents/CountdownGame$ 



My script runs very quickly, and certainly within the 30 seconds allowed in the Coutdown letters game.

##References

LetterGenmerator.py
WordGame.py


## This is the function that actually selects the random letters .
The LetterGenerator is call from the WordGame to generate the letters.
There is 3 loops, each calling from a different lists  which are, 1 of vowels, 1 of consonants, and 1 of all letters.
This is the easiesy way match the requirements of the rules on the letter selection.

	for l in range(0,3):
		random.shuffle(vowel,random.random)
		genword.insert(0,vowel.pop())

	for l in range(0,4):
		random.shuffle(const,random.random)
		genword.insert(0,const.pop())

	for l in range (0,2):
		random.shuffle(both,random.random)
		genword.insert(0,both.pop())
	return genword

This is one of the preprocesses that is required, however it is run every time the main script is run.

The second preprocess is that of creating the check list. It is split in two sections 1) of generating a list of the words by reading the wordslist.txt file and 2) generating the map of the word and keys. As the words are been added to the map they are checked to ensure that the word is between 3 and 9 caracters in length as this are the only allowable variations.

def	fillmap():
	count=0
	f = open('wordlist.txt', 'r')
	words = f.read().split()
	for word in words:
		key = sorted(word)
		sortedKey = "".join(key)
		count +=1
		addToMap(sortedKey,word)

def	addToMap(key,value):
	if(len(key)>2 and len(key)<10):
		if key in wordDict:
			wordDict.get(key).append(value) #if key exists, get the reference to the list(value) and add it.
			#print(wordDict.get(key).append(value))
		else:
			wordDict.update({key:[value]})


When the Letters are generated the list is concantinated into a word and is passed into the search function. This function will find all of the possible combinations of letters from the 9 letter word.

def	finder(gentext):
	maxi = 9
	wordcombs = []
	wordcomb= []
	for i in range(0, maxi):
		wordcombs = itertools.combinations(gentext, maxi)
		#print(itertools.combinations(gentext,maxi))
		wordcomb = ["".join(a) for a in wordcombs]
		#print(["".join(a) for a in wordcombs])
		maxi -=1
		for combination in wordcomb:
			if combination in wordDict.keys():
				#print(wordDict[combination])
				return(wordDict[combination])

, and finally runs the solver.
