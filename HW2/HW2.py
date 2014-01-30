import json
import gzip
from string import punctuation
from  __builtin__ import any as nick_name

def Load_Tweets():
    counter = 0
    for line in gzip.open('C:\\Users\\Paul\\Documents\\Spring 2014\\Data_Science_Visualization\\HomeWorks\\HW2\\HW02_twitterData.json.txt.gz','r'):
        if counter >=5:
            break
        tweet = json.loads(line.strip())
        #print tweet["created_at"], type(tweet["text"]), tweet["text"]
        
        #removing punctuation and separating tweet into list of words
        clean_tweet = Sanitize_Tweet(tweet["text"])
        
        #checking to see who is mentioned
        #if check_value = 0, obama ; check_value = 1, romney; check_value= 2, both
        check_value = Sort_Out_Candidates(clean_tweet, tweet["created_at"])#checking to see which candidate the tweet is about
        if check_value == 0:
            print "ay"
        elif check_value == 1:
            print "ya"
        else:
            print "na"
        
        #print tweet["text"]
        #print check_value
        #print clean_tweet
        counter +=1

def Sanitize_Tweet(tweet):
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
    
    obama_names = ["obama","bama","barry","b.o","barrack","barack","bear","renegade","obomber","bammy","brak","divider"]
    romney_names = ["mitt","romney","mittens","mormon","mitney","mit","waffle","binder","nobama","romnuts","javelin"]
    both_flag = [0,0] # if 1, then only romney, if 2 then both romeny and obama
    for name in romney_names:
        romney_nickname = nick_name(name in x for x in clean_tweet)
        if romney_nickname is True:
            check_value = 1
            both_flag[0] = 1
    
    for name in obama_names:
        obama_nickname = nick_name(name in x for x in clean_tweet)
        if obama_nickname is True:
            check_value = 0
            both_flag[1] = 1
                        
    if both_flag[0]==1 and both_flag[1]==1:
        check_value = 2
            
    return check_value