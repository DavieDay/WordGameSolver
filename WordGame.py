# David Hynes
# G00295205
# Date 29/03/2016


import random
import itertools

#word = input("Enter your 9 Letters, Minimum of 3 vowles, minimum of 3 consonants, and mix of either 3: ")
word = "cautionz"
#listOf = []
sen = 1
print ("Your chosen word is: "+word)

while (sen > 0):

	def shuffle(word):
	  word = list(word)
	  random.shuffle(word)
	  word = "".join(word)
	  return word


#fourword = word

#word1 = shuffle(word)



	def loadcheckd(filepath, checkd={}):
	  f = open(filepath, 'r')
	  for word in f:
	    word = word.strip()
	    sortword = sorted(word)
	    sortword = "".join(sortword)
	    hashword = hash(sortword)
	    words = checkd.get(hashword, set())
	    words.update({word})
	    checkd[hashword] = words
	  return checkd
	
	def check(word, checkd):
	  word = list(word)
	  sortword = sorted(word)
	  sortword = "".join(sortword)
	  hashword = hash(sortword)
	  results = checkd.get(hashword, None)
	  return results

	checkd = loadcheckd("wordlist.txt")
	anagram = shuffle(word)
	
	print("Looking for a word of %s." % anagram)
	
	words = check(word, checkd)
	if words:
	  
	  print("Found %d word:" % len(words))
	  sen =0
	  for word in words:
	      print(word)
		
	    
	#elif words:
	  #word = list(itertools.combinations(s,len(word)-2))
	
	else:
	  word = list(itertools.combinations(word,len(word)-1))
	  #print("There are no words.")


