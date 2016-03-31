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
	# list of vowels
	vowel =['a','a','a','a','a','a','a','a','a','e','e','e','e','e','e','e','e','e','e','e','e','i','i','i','i','i','i','i','i','i','o','o','o','o','o','o','o','o','u','u','u','u',]   
	const = ['b', 'b', 'c', 'c', 'd', 'd', 'd', 'd', 'f', 'f', 'g', 'g', 'g', 'j', 'k', 'l', 'l', 'l', 'l', 'n', 'n', 'p', 'p', 'q', 'r', 'r', 'r', 'r', 'r', 'r', 's', 's', 's', 's', 't', 't', 't', 't', 't', 't', 'v', 'v', 'w', 'w', 'x', 'y', 'y', 'z']
# list of consonants
	both = vowel + const


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

'''
print(genword)
genword = "".join(genword)
print(genword)

weighted letters as per Scrabble. following the provision of a list = ['a', 'a', 'a', 'b', 'k', 'r', 'z', 'z', 'z'].
#=======================================================================
#1 point: E ×12, A ×9, I ×9, O ×8, N ×6, R ×6, T ×6, L ×4, S ×4, U ×4
#2 points: D ×4, G ×3
#3 points: B ×2, C ×2, M ×2, P ×2
#4 points: F ×2, H ×2, V ×2, W ×2, Y ×2
#5 points: K ×1
#8 points: J ×1, X ×1
#10 points: Q ×1, Z ×1
#======================================================================



vowels =['a','a','a','a','a','a','a','a','a','e','e','e','e','e','e','e','e','e','e','e','e','i','i','i','i','i','i','i','i','i','o','o','o','o','o','o','o','o','u','u','u','u',]   
consts =['q','w','w','r','r','r','r','r','r','t','t','t','t','t','t','y','y','p','p','s','s','s','s','d','d','d','d','f','f','g','g','g','j','k','l','l','l','l','z','x','c','c','v','v','b','b','n','n','

'''

