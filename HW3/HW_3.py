import json
import pprint
from string import punctuation

enormous_corpus =[]
message_corpus = []
exclude_set = set(punctuation)

def Load_Messages():
    counter = 0
    for line in open('C:\\Users\\Paul\\Documents\\Spring 2014\\DSV_Data_Files\\HW_3\\messages.json.txt','r'):
        user_message = json.loads(line.strip())
        message_corpus.append(user_message["message"])
        
    return message_corpus
    
'''
        if counter == 1000:
            break
        else:
            #print user_message["sender"],user_message["message"]
            #print user_message["message_time"]
            #print user_message
            #pp = pprint.PrettyPrinter(5)
            #pp.pprint(user_message)
            #print user_message.keys()
            #print user_message["message_id"], user_message["message_time"], user_message["num_recipients"]
            #if "sender" in user_message:
                #print "We have a sender"
            #print ""
            enormous_corpus.append(user_message)
            enormous_corpus_text = "".join(user_message["message"])
            corpus_words = enormous_corpus_text.strip().split()
            #print enormous_corpus_text
            #print corpus_words
            #print counter
            counter +=1
    
        enormous_corpus.append(user_message)
        enormous_corpus_text = "".join(user_message["message"])
        corpus_words = enormous_corpus_text.strip().split()        
        word2count = { w:0 for w in set(corpus_words) }
        for word in corpus_words:
            word2count[ word ] += 1
### ################################################################### ###
### MUCH FASTER than looping over the entire book for every unique word ###
### ################################################################### ###
 
# Now sort the words by their counts like we did in LEC02:
    count_word = sorted([ (word2count[w],w) for w in word2count ], reverse=True)
 
# Get the top 100 words and print them and their counts:
    top_words = [ w for c,w in count_word ][:100]
 
    for word in top_words:
        print word, word2count[word]
'''            
def Word_Count(corpus):
        enormous_corpus_text = "".join(user_message["message"])
        corpus_words = enormous_corpus_text.strip().split()        
        word2count = { w:0 for w in set(corpus_words) }
        for word in corpus_words:
            word2count[ word ] += 1
        
def Main():
    messages = Load_Messages()
    Word_Count(messages)