import json
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
import matplotlib



with open("data.json","r") as f:
    data = json.loads(f.read())


#Creating list of account names that resulted in errors
errors = [x for x in data if not type(data[x]) == float]



#Initializing date dictionary
dates = {}

#Converting each users unix time to a date in the format YYYY-MM, which is used as a key for the dictionary: dates
for user in data:
    if user not in errors:
        date = datetime.fromtimestamp(data[user]).strftime('%Y-%m')
        if date not in dates:
            dates[date] = []
        dates[date].append(user)


#Adding empty months that did not have any accounts
for y in range(2005,2019):
    for m in range(1,13):
        if len(str(m)) == 1:
            newDate = "{}-0{}".format(y,m)
        else:
            newDate = "{}-{}".format(y,m)

        if newDate not in dates:
            dates[newDate] = []



#Remain is a list of the number of accounts remaining after the said month
#Making sure to start with the total number of accounts minus the 404's           
remain = [len(data)-len(errors)]

for a in sorted(dates):
    #Subtracting the numbers of accounts created during that month
    remain.append(remain[-1] - len(dates[a]))



#Converting datetime as strings to a datetime object
x = [datetime.strptime(x, '%Y-%m') for x in sorted(dates)]

#Adding one more month to x because started with one more in remain list, this matches dimensions.
x.append(datetime.strptime(sorted(dates)[-1], '%Y-%m')+timedelta(days=31))

#================================================================
#Graphing

fig, ax = plt.subplots()

ax.plot(x,remain, color=(41/255.,120/255.,131/255.))

#Setting Text
ax.set_title("The Availability of Three-Character Usernames on Reddit", fontname="Verdana")
ax.set_xlabel("Time", fontname="Verdana")
ax.set_ylabel("Number of Accounts Remaining", fontname="Verdana")

#Setting graph properties 
ax.set_ylim(-100,50000)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

#Saving the graph
plt.savefig("graph_no_grid.png",dpi = 600)
plt.close()
































