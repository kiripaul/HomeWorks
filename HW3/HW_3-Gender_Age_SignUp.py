import csv
import matplotlib.dates as dates
import matplotlib.pyplot as plt
from collections import Counter
import numpy as N

tstamps =[]
tstamps_formatted=[]
gender=[]

def Graph_SignUp_Date(ts_formatted):
    dates_counted = Counter(tstamps_formatted)
    # sorted lists [ (key1,val1), (key2,val2), ... ]
    # must sort BEFORE we break the (k,v)-pairs apart!
    dates_sorted = sorted(dates_counted.items())
    #print dates_counted
    #print ""
    #print dates_sorted
    
    # [(key1,val1), (key2,val2), ... ] --> (key1,key2,...), (val1,val2,...)
    dates_sort, ndates = zip(*dates_sorted)
    
    # replace the python date lists with matplotlib dates:
    #dates_sort = matplotlib.dates.date2num(dates_sort)
    
    plt.hold(True)
    
    # use plot_date() not plot()
    plt.plot_date(dates_sort, ndates, 'b-') # blue line
    
    # annotate the plot:
    plt.xlabel("Time", fontsize=18)
    plt.ylabel("Number of SignUps", fontsize=18)
    plt.title("SignUp Volume", fontsize=18)
    
    # This is a little small in this notebook, so here's a way
    # to control the size of the figure:
    plt.gcf().set_size_inches(12,8) # gcf = "get current figure"
    '''
    z=N.polyfit(dates_sort,ndates,1)
    p=N.poly1d(z)
    plt.plot(dates_sort,p(dates_sort),'r--') #add trendline to plot
    '''
    # Here's a trick to style the x-labels
    plt.gcf().autofmt_xdate() # takes some googling to discover these
    plt.show()

def Graph_Gender(gender):
    gender_counted = Counter(gender)
    print gender_counted

with open ('C:\\Users\\Paul\\Documents\\Spring 2014\\DSV_Data_Files\\HW_3\\bios.csv','r') as doc:
    for line in csv.DictReader(doc):
        #date = line["signup_date"][:10]
        date = line["signup_date"][:19]
        gender.append(line["gender"])
        #print line["signup_date"]
        tstamps.append(date) #grabbing dates when signedup
        dt = dates.datestr2num(date)
        tstamps_formatted.append(dt)
        #print gender
        
    #Graph_SignUp_Date(tstamps_formatted)
    Graph_Gender(gender)




