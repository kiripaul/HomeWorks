from sets import Set
from collections import Counter
import random
import urllib
from string import punctuation

def jaccard(s1,s2):
    return len(s1.intersection(s2))/float(len(s1.union(s2)))

def Main_Jaccard():
    print "This is S1:"
    s1=Set([1,2,3,4])
    print s1
    print ""
    print "This is S2:"
    s2=Set([2,3,5,7])
    print s2
    print ""
    print "This is S3:"
    s3=Set([2,4,6])
    print s3
    print ""

    
    val1 = jaccard(s1,s2)
    val2 = jaccard(s1,s3)
    val3 = jaccard(s2,s3)

    print "This is the Jaccard Value of S1,S2:"
    print val1
    print ""

    print "This is the Jaccard Value of S1,S3:"
    print val2
    print ""
    print "This is the Jaccard Value of S2,S3:"
    print val3
    print ""
    print "=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-="
    
    return ()

def coin_flip(p):
    if p == 0.5:
        #print "H or T; 50% Chance"
        Coin_Side = "H or T"
    elif p > 0.5:
        #print "Probability: "+ "H " + str((p))
        Coin_Side = "H"
    else:
        #print "Probability: "+"T " + str((p))
        Coin_Side = "T"
    return Coin_Side

def Main_Coin():
    #Coin flip with random probability
    x= random.seed()
    p = random.random()
    HorT= coin_flip(p)
    print str(HorT)
    return ()

def Main_Coin2():
    #Coin flip with probability chosen from [0.2, 0.4, 0.6, 0.8]
    x= random.seed()
    flip_History=range(1000)
    Probs = [0.2,0.4,0.6,0.8]
    Count = 0
    Run_Stats = []
    for i in range(1000):
        ranInt = random.randint(0,len(Probs)-1)
        p = Probs[ranInt]
        HorT = coin_flip(p)      
        #print str(i)+ " " + str(HorT) + " Probability: " + str(p)
        flip_History[i] = HorT

    s = "".join(flip_History)
    s = s.split("T")
    Run_Stats = [len(hRun) for hRun in s if hRun]
    RunStats = Counter(Run_Stats)
    
    #print flip_History
    #print s
    print Run_Stats
    print RunStats
    return ()

def words_of_book():
    """Download `A tale of two cities` from Project Gutenberg. Return a list of
    words. Punctuation has been removed and upper-case letters have been
    replaced with lower-case.
    """
    
    url = "http://www.gutenberg.org/files/98/98.txt"
    raw = urllib.urlopen(url).read() # Download book into one long string.
    #raw.close()
    
    raw = raw[750:] # The first 750 or so characters are not part of the book.
    
    # Loop over every character in the string, keep it only if it is NOT
    # punctuation:
    exclude = set(punctuation) # Keep a set of "bad" characters.
    list_letters_noPunct = [ char for char in raw if char not in exclude ]
    
    # Now we have a list of LETTERS, *join* them back together to get words:
    text_noPunct = "".join(list_letters_noPunct)
    # (http://docs.python.org/2/library/stdtypes.html#str.join)
    
    # Split this big string into a list of words:
    list_words = text_noPunct.strip().split()
    
    # Convert to lower-case letters:
    list_words = [ word.lower() for word in list_words ]
    
    return list_words

def Main_WordCount():
    lWords = words_of_book()
    #print Counter(lWords)
    top_onehundred = Counter(lWords).most_common(100)
    print top_onehundred
    return ()

#Main_Jaccard()
#Main_Coin()
#Main_Coin2()
Main_WordCount()
