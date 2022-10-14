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

        count = 0
        for password in passwords:
            if password in words:
                count +=1
        datadict[fu +element]["passwords_cracked"] = count /1000
        
        # Collisions rate // total passwords generated
        """x.append( datadict[fu +element]["collisions_rate"])
        y.append(datadict[fu +element]["length"])"""
        
        #unique passwords // time to generate
        """x.append(datadict[fu +element]["unique"])"""
        
        #unique passwords // password generated
        """x.append( datadict[fu +element]["unique"])
        y.append(datadict[fu +element]["length"])"""
        
        #password cracked // coverage
        y.append( datadict[fu +element]["coverage"])
        x.append(datadict[fu +element]["passwords_cracked"])
        
# get random password of length 4 with letters and digits
characters = string.ascii_letters + string.digits
passwords=set()
while len(passwords) < 100000:
    passwords.add(''.join(random.choice(characters) for i in range(4)))

#Creating Dictionary containing de data needed
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

#Dumping data in Json
"""
full_data = { "FullRT": {"endhash": data_full_rt_endhash, "xorshift": data_full_rt_xorshift, "charinhash": data_full_rt_charinhash}, "RT": {"endhash": data_rt_endhash, "xorshift": data_rt_xorshift, "charinhash": data_rt_charinhash}}
dataj = json.dumps(full_data
with open('results_collisions.json', "w") as f:
    f.write(dataj)
"""

#Creating plot unique passwords // total passwords
"""plt.plot(x_xorshift, y_xorshift, label = "using xorshift reduction")
plt.plot(x_endhash, y_endhash, label = "using modulo on end of hash")
plt.plot(x_charinhash, y_charinhash, label = "choosing some chars from hash to generate the pwd")
  
# naming the x axis
plt.xlabel('x - unique passwords generated')
# naming the y axis
plt.ylabel('y - total passwords generated')
# giving a title to my graph
plt.title('unique passwords generated plotted in function of the total passwords generated ')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()"""

#Creating plot unique passwords // time
"""plt.plot(x_xorshift, [42,72,95,141], label = "using xorshift reduction")
plt.plot(x_endhash, [26,47,66,94], label = "using modulo on end of hash")
plt.plot(x_charinhash, [24,41,55,80], label = "choosing some chars from hash to generate the pwd")
  
# naming the x axis
plt.xlabel('x - unique passwords generated')
# naming the y axis
plt.ylabel('y - time needed to generate')
# giving a title to my graph
plt.title('unique passwords generated plotted in function of the time needed to generate')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()"""

#Creating plot collisions rate // passwords generated
"""plt.plot(x_xorshift, y_xorshift, label = "using xorshift reduction")
plt.plot(x_endhash, y_endhash, label = "using modulo on end of hash")
plt.plot(x_charinhash, y_charinhash, label = "choosing some chars from hash to generate the pwd")
  
# naming the x axis
plt.xlabel('x - collisions rate')
# naming the y axis
plt.ylabel('y - passwords generated')
# giving a title to my graph
plt.title('collisions rate plotted in function of the amount of passwords created')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()
"""

#Creating plot passwords cracked // coverage (without collisions)
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

 
    