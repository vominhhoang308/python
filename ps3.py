import string
# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'



### the following procedure you will use in Problem 3


def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers
        
#Problem 1
def countSubStringMatch(target, key):
    count = 0
    initialIndex = 0
    while string.find(target, key, initialIndex) != -1:
        count += 1
        initialIndex = string.find(target, key, initialIndex) + len(key) - 1
    print count

def countSubStringMatchRecursive(target, key):
    if string.find(target,key) == -1:
        return 0
    if string.find(target,key) != -1:
        print 1
        countSubStringMatchRecursive(target[string.find(target,key)+len(key)-1:],key)
    
            
#Problem 2
def subStringMatchExact(target,key):
    startingList = []
    initialIndex = 0
    while string.find(target,key,initialIndex) != -1:
        startingList.append(string.find(target,key,initialIndex))
        initialIndex = string.find(target, key, initialIndex) + len(key) - 1
    print tuple(startingList)

#Problem 3
def constrainedMatchPair(firstMatch, secondMatch, length):
    listMatch = []
    for indexFirstMatch in range(0,len(firstMatch)):
        for indexSecondMatch in range(0,len(secondMatch)):
            if firstMatch[indexFirstMatch] + length + 1 == secondMatch[indexSecondMatch]:
                listMatch.append(firstMatch[indexFirstMatch])
    print tuple(listMatch)
    

#Problem 4
    def subStringMatchExactlyOneSub(target,key):
	"""
	This function takes two arguments: a target string and a key string. 
	
	It returns a tuple of all starting points of matches of the key to the target, such that at exactly one element of the key is incorrectly matched to the target.
	"""

	possible_answer = subStringMatchOneSub(key,target)
	answer = possible_answer
	perfect_matches = subStringMatchExact(target,key)
	to_remove_from_answer = ()

	#	this for loop identifies the positions in possible_answer that contain perfect matches.
	for i in range(0,len(possible_answer)):
		for j in range(0,len(perfect_matches)):
			if possible_answer[i] == perfect_matches[j]:
				#print "matches:", possible_answer[i]
				to_remove_from_answer += (i,)
				#print to_remove_from_answer

	# this for loop removes the items from the possible_answer tuple begin at the end and working forward. 
	for m in reversed(to_remove_from_answer):
		#print to_remove_from_answer[-m]
		#print m
		answer = answer[:m] + answer[m+1:]
		# print answer
	return answer
