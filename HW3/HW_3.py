import json

def Load_Messages():
    counter = 0
    for line in open('C:\\Users\\Paul\\Documents\\Spring 2014\\DSV_Data_Files\\HW_3\\messages.json.txt','r'):
        user_message = json.loads(line.strip())
        if counter == 20:
            break
        else:
            #print user_message["sender"],user_message["message"]
            print user_message["message_time"]
            print ""
            counter +=1
            
Load_Messages()