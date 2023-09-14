import math
import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
a=0
b=0
c=0
d=0
e=0
f=0
y=0

df=[a,b,c,d,e,f]
df0=pd.DataFrame(data=df, columns=["Trial"])
aq=0


for x in range(100):
    
    a = math.floor(49*(random.random())+1)
    
    b = math.floor(49*(random.random())+1)
   
    c = math.floor(49*(random.random())+1)
    
    d = math.floor(49*(random.random())+1)

    e = math.floor(49*(random.random())+1)
    
    f = math.floor(49*(random.random())+1)

    df0["Trial"] = [a,b,c,d,e,f]

    while len(set(df0["Trial"])) < 6:

        a = math.floor(49*(random.random())+1)
    
        b = math.floor(49*(random.random())+1)
   
        c = math.floor(49*(random.random())+1)
    
        d = math.floor(49*(random.random())+1)

        e = math.floor(49*(random.random())+1)
    
        f = math.floor(49*(random.random())+1)
        
        df0["Trial"] = [a,b,c,d,e,f]
    
    aq += 1
    aess = str(aq)

    dfc = df0["Trial"].copy()
    df0.insert(aq,"Trial "+ aess,dfc) 

print(df0)

o=0
data=[]
for i in range(50) :
    o += 1
    data.append(o)

rd=[]
z = 0
# print(data)

df01 = df0.drop(columns = ["Trial"])
print(df01)

liste = df01.to_numpy()
listf = np.concatenate(liste)
listg = listf.tolist()
# print(listg)

for i1 in data :
    for i2 in listg : 
        if i2 == i1 :
            z += 1
    rd.append(z)
    z=0

# print(rd)

df1 = pd.DataFrame(data=rd, index=data, columns=["Count"])

df11 = df1.sort_values(by="Count", ascending=False)
print(df11.head(6))

        
