import csv
counter = 0
tstamps =[]
tstamps2=[]

with open ('C:\\Users\\Paul\\Documents\\Spring 2014\\DSV_Data_Files\\HW_3\\bios.csv','r') as doc:
    for line in csv.DictReader(doc):
        tstamps2.append(line["signup_date"])
        tstamps.append(line["signup_date"][:10])
        if counter == 20:
            break
        counter +=1

print tstamps
print ""
#print tstamps2