import json
import gzip
from string import punctuation

def Load_Tweets():
    counter = 0
    for line in gzip.open('C:\\Users\\Paul\\Documents\\Spring 2014\\Data_Science_Visualization\\HomeWorks\\HW2\\HW02_twitterData.json.txt.gz','r'):
        if counter >=20:
            break
        tweet = json.loads(line.strip())
        #print tweet["created_at"], type(tweet["text"]), tweet["text"]
        clean_tweet = Sanitize_Tweet(tweet["text"])
        #both_candidates = Grab_Obmney(clean_tweet)
        #obama_corpus = Grab_Obama(clean_tweet)
        #romney_corpus = Grab_Romney(clean_tweet)
        print tweet["text"]
        print clean_tweet
        counter +=1

def Sanitize_Tweet(tweet):
    '''
    Input: Singular Tweet
    Output: Singular Tweet
    '''
    exclude = set(punctuation) # Keep a set of "bad" characters.
    tweet_noPunct = [ char for char in tweet if char not in exclude ]
    # Now we have a list of LETTERS, *join* them back together to get words:
    tweet_words_noPunct = "".join(tweet_noPunct)
    # (http://docs.python.org/2/library/stdtypes.html#str.join)
    
    # Split this big string into a list of words:
    tweet_to_list = tweet_words_noPunct.strip().split()
    
    # Convert to lower-case letters:
    tweet_to_list = [word.lower() for word in tweet_to_list]
    return tweet_to_list
    
def Grab_Obama(clean_tweet):
    print "Hello World"
    
def Grab_Romney(clean_tweet):
    print "This sucks"
    
def Grab_Obmney(clean_tweet):
    print "Fuccccck!"