# David Hynes
# G00295205
# Date 29/03/2016


import random
import itertools
from LetterGenerator import gen_a_word

#word = input("Enter your 9 Letters, Minimum of 3 vowles, minimum of 3 consonants, and mix of either 3: ")
word = "gen_a_word()"
#listOf = []
sen = 1
print ("Your chosen word is: "+word)

#while (sen > 0):

def shuffle(word):
	word = list(word)
	random.shuffle(word)
	word = "".join(word)
	return word


#fourword = word

#return all(count <=input_counter[key] for key, count in word_counter.items())
#lister = [word for word if len(word) <= len(user)]
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
	  #sen =0
	for word in words:
		print(word)
		
	    
	#elif words:
	  #word = list(itertools.combinations(s,len(word)-2))
	
else:
	  #shortWord = list(itertools.combinations(word,len(word)-1))
	  #for word in words:
	  #    print(word)
	print("There are no words.")
	  #print(any((True for word in shortWord if word in words)))



#=======================================================================
#1 point: E ×12, A ×9, I ×9, O ×8, N ×6, R ×6, T ×6, L ×4, S ×4, U ×4
#2 points: D ×4, G ×3
#3 points: B ×2, C ×2, M ×2, P ×2
#4 points: F ×2, H ×2, V ×2, W ×2, Y ×2
#5 points: K ×1
#8 points: J ×1, X ×1
#10 points: Q ×1, Z ×1
#======================================================================




