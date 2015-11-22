# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"
playerList = ["Player 1", "Player 2"]


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

def is_word_valid(word, wordlist): #to check if the word has meanning
    validWord = True
    if word in wordlist: #check if the word is meanningful
        validWord = True
    else:
        validWord = False
    return validWord

def is_word_begin_valid(word, wordlist): #to check if the word is the beginning part of any meanning ful word.
    # wordlistCheck = wordlist[:] #have a copy of a wordlist to check
    # for i in range(len(word)):
    #     for wordMember in wordlistCheck: #loop through each member of the wordlistCheck
    #         if word[i] != wordMember[i]: #if the first element in word == first element in member of wordlistCheck
    #             wordlistCheck.remove(wordMember) # wordlistcheck will remove it
    #         else:
    #             continue
    # if len(wordlistCheck) > 0: # after all, if there is no elements in wordlistChecl, then the word is not the beginning of any
    #     return True # part in a meanningful word
    # else:
    #     return False
    for word in wordlist:
        if word.startswith(word):
            return False
    return True

def is_single_letter(letter):
    return letter in string.ascii_letters


def play_round(playerList, fragment):
    while len(playerList) > 1:
        for playerName in playerList:
            print playerName, "turn."
            inputWord = raw_input("In put the letter: ")
            while is_single_letter(inputWord) == False:
                inputWord = raw_input("Your letter is invalid. Please try again: ")
            fragment += inputWord
            print "Current Fragment: ", fragment
            if len(fragment)>3: 
                if is_word_valid(fragment, wordlist):
                    print "Player ", playerName, " loses because you have entered a meanningful word having more than 3 letters."
                    playerList.remove(playerName)
                    break
            if is_word_begin_valid(fragment, wordlist):
                print "Player ", playerName, " loses because you have entered a fragment that is not a part of any words."
                playerList.remove(playerName)
                break


def playgame():
    fragment = ''
    play_round(playerList,fragment)
    print playerList[0],'won the game, congratulations!'                           
 

playgame()






















# TO DO: your code begins here!