# David Hynes
# G00295205
# Date

import random
import itertools
from LetterGenerator import gen_a_word
import timeit

wordDict = dict()

def	getWord():
	word = gen_a_word()#Call from LetterGenerato to provide a 9 letter which is in a list 
	#['u', 't', 't', 'b', 'p', 't', 'e', 'e', 'i']
	sortword = sorted(word)
	joinword = "".join(sortword)#join list
	#print ("The LETTERS chosen are: "+word)# pintout to show the word

	#
	#word = "".join(word)
	#print(joinword)
	return joinword

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
		else:
			wordDict.update({key:[value]})

fillmap()

def	finder(gentext):
	maxi = 9
	wordcombs = []
	wordcomb= []
	for i in range(0, maxi):
		wordcombs = itertools.combinations(gentext, maxi)
		wordcomb = ["".join(a) for a in wordcombs]
		i -=1
		for combination in wordcomb:
			if combination in wordDict.keys():
				return(wordDict[combination])

def	runner():
	gentext = getWord()
	result =finder(gentext)
	return result
'''
def processWord(word):
    sortword = sorted(word)
    joinword = "".join(sortword)
    return joinword
'''

# test for 10000 runs
if __name__=='__main__':
	import timeit
	print(runner())
	print(timeit.timeit("runner()",setup="from __main__ import runner", number = 10000))
	
