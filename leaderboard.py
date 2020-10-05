import sys
import numpy as np
import pandas as pd

sys.path.append('..//scoreware-site//util//runner//')
import runnerutils

data=pd.read_csv('results/2020-10-04 2020 HMRRC VIRTUAL 5K XC SERIES Hudson Mohawk Road Runners Club.csv')
                        #  2020-09-14 2020 HMRRC VIRTUAL 5K XC SERIES Hudson Mohawk Road Runners Club
def timeToSeconds(time):
    temp=time.split('.') 
    temp=temp[0].split(':')
    print(len(temp))
    try:
        if (len(temp)==2):
            return 60*int(temp[0])+int(temp[1])
        elif (len(temp)==1):
            return 60*int(temp[0])
    except:
        return 100000
    
data['seconds']=data['Time'].apply(lambda x: timeToSeconds(x))
#data=data.drop('Event registration date',axis=1)
data=data.drop('e-Mail', axis=1)

data=data.sort_values(by='seconds')
data.Gender=data.Gender.apply(lambda x: x.lower())
data.Gender=data.Gender.apply(lambda x: x[0])
data=data.drop('seconds',axis=1)

data=data.reset_index(drop=True)

data.index+=1

print(data)

markdown=data.to_markdown()
fname='leaderboard.md'
out_file=open(fname, "w")
out_file.write(markdown)
out_file.close()

csvname='leaderboard.csv'
data.to_csv(csvname)
    




