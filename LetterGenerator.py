"""
solver.letter_gen
~~~~~~~~~~~~
This module generates random letters.
As per the countgame there is a 9 letters.
The string generated consists of a minimum of 3 vowels and 4 consonants, withe the 2 remainer being a mix of either.

"""

import random
import itertools

def gen_a_word():

	genword = []#empth list for the word
	vowel =["a","e","i","o","u"]# list of vowels
	const = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]# list of consonants
	both = vowel + const


	for l in range(0,3):
		random.shuffle(vowel,random.random)
		genword.insert(0,vowel[0])

	for l in range(0,4):
		random.shuffle(const,random.random)
		genword.insert(0,const[0])


	for l in range (0,2):
		random.shuffle(both,random.random)
		genword.insert(0,both[0])

	return genword

'''
print(genword)
genword = "".join(genword)
print(genword)
'''


print(genword())
