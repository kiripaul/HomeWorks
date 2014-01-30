import json
import gzip
from string import punctuation
from  __builtin__ import any as nick_name

def Load_Tweets():
    counter = 0
    for line in gzip.open('C:\\Users\\Paul\\Documents\\Spring 2014\\Data_Science_Visualization\\HomeWorks\\HW2\\HW02_twitterData.json.txt.gz','r'):
        if counter >=1:
            break
        tweet = json.loads(line.strip())
        #print tweet["created_at"], type(tweet["text"]), tweet["text"]
        
        #removing punctuation and separating tweet into list of words
        clean_tweet = Sanitize_Tweet(tweet["text"])
        
        #checking to see who is mentioned
        #if check_value = 0, obama ; check_value = 1, romney; check_value= 2, both
        check_value = Sort_Out_Candidates(clean_tweet, tweet["created_at"])
        #print check_value
        #print tweet["text"]
        print clean_tweet
        counter +=1

def Sanitize_Tweet(tweet):
    '''
    Input: Singular Tweet
    Output: Singular Tweet
    '''
    exclude = set(punctuation) # Keep a set of "bad" characters.
    
    tweet_noPunct = [ char for char in tweet if char not in exclude ]#removing any punctuation from the tweet
    
    # Now we have a list of LETTERS, *join* them back together to get words:
    tweet_words_noPunct = "".join(tweet_noPunct)
    
    # Split this big string into a list of words:
    tweet_to_list = tweet_words_noPunct.strip().split()
    
    # Convert to lower-case letters:
    tweet_to_list = [word.lower() for word in tweet_to_list]
    return tweet_to_list
    
def Sort_Out_Candidates(clean_tweet, created_at_date):
    # 0 : One of Obama's nicknames was found in tweet
    # 1 : One of Romney's nicknames was found in tweet
    # 2 : Both of their nickname were found in tweet
    
    obama_names = ["obama","bama","barry","b.o","barrack","barack","bear","renegade","obomber"]
    #romney_names = ["mitt","romney","mittens","mormon"]
    for name in obama_names:
        obama_nickname = nick_name(name in x for x in clean_tweet)
        print name
        print obama_nickname
        
    if obama_nickname is True:
        check_value = 0