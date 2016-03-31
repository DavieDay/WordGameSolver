# from http://stackoverflow.com/questions/17176887/python-get-all-permutation-of-a-list-w-o-repetitions


from itertools import combinations
i=1
b=[]
lis = ["a","b","c","d"]
for i in range(2, len(lis)+i):  #xrange will return the values 1,2,3,4 in this loop
    
	#print(list(combinations(lis, i)))
	print(["".join(a) for a in combinations(lis, i)])
	#b = ["".join("".join(a) for a in combinations(lis, i))]
	b.insert(0,["".join(a) for a in combinations(lis, i)])

    

#word = "catch"
#word = list(word)
#print(word)
#word = "".join(word)
print(b)


