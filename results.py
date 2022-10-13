import random
import string
import json 
import matplotlib.pyplot as plt

RT_XORSHIFT = ["rtXorShift_30%","rtXorShift_50%","rtXorShift_70%","rtXorShift_100%"]
RT_ENDHASH = ["rtEndHash_30%","rtEndHash_50%","rtEndHash_70%","rtEndHash_100%"]
RT_CHARINHASH= ["rtcharinhash_30%", "rtcharinhash_50%","rtcharinhash_70%", "rtcharinhash_100%"]

def createdictdata(filename,full=""):
    datadict = {}
    for element in filename:
        datadict[full + element] = {}
    return datadict

def get_data(filename, datadict, passwords, x=[],y=[], full=0):
    if full:
        full = "Full_"
        fu = "F"
    else:
        full = ""
        fu = ""
    for element in filename:
        rows=[]
        with(open(full + "RT_tables\\" + fu + element + ".txt",'r')) as f:
            for line in f:
                line= line.split()
                k = [x.strip() for x in line]
                rows.extend(k)
            
        datadict[fu +element]["length"] = len(rows)
        words =  set(rows)
        datadict[fu +element]["unique"] = len(words)
        datadict[fu +element]["collisions_rate"] = (1-(datadict[fu +element]["unique"]/ float(datadict[fu +element]["length"]))) * 100
        datadict[fu +element]["coverage"] = (len(words) / 62**4)*100
        y.append( datadict[fu +element]["coverage"])
        count = 0
        for password in passwords:
            if password in words:
                count +=1
        datadict[fu +element]["passwords_cracked"] = count /1000
        x.append(datadict[fu +element]["passwords_cracked"])
        
# get random password of length 4 with letters and digits
characters = string.ascii_letters + string.digits
passwords=set()
while len(passwords) < 100000:
    passwords.add(''.join(random.choice(characters) for i in range(4)))

data_full_rt_xorshift = createdictdata(RT_XORSHIFT, "F")
data_rt_xorshift = createdictdata(RT_XORSHIFT)
x_xorshift = []
y_xorshift = []
get_data(RT_XORSHIFT, data_full_rt_xorshift, passwords, x_xorshift,y_xorshift,"Full_")
get_data(RT_XORSHIFT, data_rt_xorshift, passwords)

data_rt_endhash = createdictdata(RT_ENDHASH)
data_full_rt_endhash = createdictdata(RT_ENDHASH, "F")
x_endhash = []
y_endhash = []
get_data(RT_ENDHASH, data_full_rt_endhash, passwords,x_endhash, y_endhash, "Full_")
get_data(RT_ENDHASH, data_rt_endhash, passwords)

data_rt_charinhash = createdictdata(RT_CHARINHASH)
data_full_rt_charinhash = createdictdata(RT_CHARINHASH, "F")
x_charinhash = []
y_charinhash = []
get_data(RT_CHARINHASH, data_full_rt_charinhash, passwords, x_charinhash,y_charinhash, "Full_")
get_data(RT_CHARINHASH, data_rt_charinhash, passwords)

plt.plot(x_xorshift, y_xorshift, label = "using xorshift reduction")
plt.plot(x_endhash, y_endhash, label = "using modulo on end of hash")
plt.plot(x_charinhash, y_charinhash, label = "choosing some chars from hash to generate the pwd")
  
# naming the x axis
plt.xlabel('x - percentage of passwords cracked in a set of 100 000 passwords')
# naming the y axis
plt.ylabel('y - percentage of possible passwords generated')
# giving a title to my graph
plt.title('percentage of passwords cracked plotted as a function of the percentage of possible password generated')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show() 
    