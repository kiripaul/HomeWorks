import csv
import json
import datetime
import time
import matplotlib.dates as dates
import matplotlib,matplotlib.pyplot as plt
import unicodedata
from collections import Counter

tstamps =[]
tstamps_formatted=[]
gender=[]
ages=[]
user_message_dates=[]
counter = 0
mean_list={}

def Graph_SignUp_Date(ts_formatted):
    dates_counted = Counter(tstamps_formatted)
    # sorted lists [ (key1,val1), (key2,val2), ... ]
    # must sort BEFORE we break the (k,v)-pairs apart!
    dates_sorted = sorted(dates_counted.items())
    # [(key1,val1), (key2,val2), ... ] --> (key1,key2,...), (val1,val2,...)
    dates_sort, ndates = zip(*dates_sorted)    
    # use plot_date() not plot()
    plt.plot_date(dates_sort, ndates, 'c-') # blue line
    
    # annotate the plot:
    plt.xlabel("Time", fontsize=18)
    plt.ylabel("Number of SignUps", fontsize=18)
    plt.title("SignUp Volume", fontsize=18)
    
    # This is a little small in this notebook, so here's a way
    # to control the size of the figure:
    plt.gcf().set_size_inches(12,8) # gcf = "get current figure"
    # Here's a trick to style the x-labels
    plt.gcf().autofmt_xdate() # takes some googling to discover these
    plt.show()

def Graph_Gender(gender):
    gender_counted = Counter(gender)
    gender_sorted = sorted(gender_counted.items())
    # [(key1,val1), (key2,val2), ... ] --> (key1,key2,...), (val1,val2,...)
    gender_identification, gender_value = zip(*gender_sorted)
    #converting gender value and id to list
    gender_value = list(gender_value)
    gender_identification = list(gender_identification)
    #converting to float
    for i in range(len(gender_value)):
        gender_value[i] = float(gender_value[i]) 
    #Summing the unknown gender answers
    unknown_gender = gender_value[0]+gender_value[3]+gender_value[4]+gender_value[5]+gender_value[6]
    gender_value[0]=unknown_gender
    #removing the un-summed gender values
    for i in range(4):
        gender_value.pop(3)

    gender_identification.pop(0)#need to remove first value
    for i in range(4):
        gender_identification.pop(2)
           
    gender_identification.insert(0,0)
    gender_identification[1] = 1
    gender_identification[2] = 2
    
    for i in range(3):
        gender_identification[i] = int(gender_identification[i])

    Labels = ["Unknown","Female","Male"]
    plt.bar(gender_identification, gender_value, align="center") # blue line
    plt.xticks(range(len(gender_value)),Labels)
    
    # annotate the plot:
    plt.xlabel("Gender Identification", fontsize=18)
    plt.ylabel("Gender Count", fontsize=18)
    plt.title("Distribution of User Genders", fontsize=18)
    
    # This is a little small in this notebook, so here's a way
    # to control the size of the figure:
    plt.gcf().set_size_inches(12,8) # gcf = "get current figure"
    plt.show()
    
    
def Graph_Age(age):
    age_counted = Counter(age)
    age_sorted = sorted(age_counted.items())
    # [(key1,val1), (key2,val2), ... ] --> (key1,key2,...), (val1,val2,...)
    age, age_count = zip(*age_sorted)
    
    plt.hold(True)
    plt.bar(age, age_count, align="center")
    
    # annotate the plot:
    plt.xlabel("Ages of Users", fontsize=18)
    plt.ylabel("Number of Users", fontsize=18)
    plt.title("Distribution of User Ages", fontsize=18)
    
    # This is a little small in this notebook, so here's a way
    # to control the size of the figure:
    plt.gcf().set_size_inches(12,8) # gcf = "get current figure"
    plt.show()

def Fix_Time(mTime):
    #converting mTime to datetime data type   
    if (type(mTime)== float):
        mTime= time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(mTime))
    
    mTime=datetime.datetime.strptime(mTime,"%Y-%m-%d %H:%M:%S").date()
    return mTime
    
def Graph_Usage(message_dates):
    messages_counted = Counter(message_dates)
    messages_sorted = sorted(messages_counted.items())
    
    # [(key1,val1), (key2,val2), ... ] --> (key1,key2,...), (val1,val2,...)
    dates, date_count = zip(*messages_sorted)
    
    plt.plot_date(dates,date_count,"bo")
    # annotate the plot:
    plt.xlabel("Dates", fontsize=18)
    plt.ylabel("Number of Posts on that Date", fontsize=18)
    plt.title("Distribution of User Usage", fontsize=18)
    
    # This is a little small in this notebook, so here's a way
    # to control the size of the figure:
    plt.gcf().set_size_inches(12,8) # gcf = "get current figure"
    plt.gcf().autofmt_xdate() # takes some googling to discover these
    plt.show()

def Main():    
    with open ('C:\\Users\\Paul\\Documents\\Spring 2014\\DSV_Data_Files\\HW_3\\bios.csv','r') as doc:
        for line in csv.DictReader(doc):
            #print type(line)
            date = line["signup_date"][:19]
            gender.append(line["gender"])
            age = int(line["age"])
            if age >= 8 and age <= 80:
                ages.append(age)
            tstamps.append(date) #grabbing dates when signedup
            dt = dates.datestr2num(date)
            tstamps_formatted.append(dt)
            
        #Graph_SignUp_Date(tstamps_formatted)
        #Graph_Gender(gender)
        Graph_Age(ages)
'''
    for line in open('C:\\Users\\Paul\\Documents\\Spring 2014\\DSV_Data_Files\\HW_3\\messages.json.txt','r'):
        user_message = json.loads(line.strip())
        mTime=user_message["message_time"]
        yTime = Fix_Time(mTime)
        user_message_dates.append(yTime)
    
    Graph_Usage(user_message_dates)
''' 

Main()
    
    
    

