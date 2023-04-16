# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 12:27:48 2022

@author: harsh
"""


import random
import math

eqn=input("enter equation\n")

Ltemp1=eqn.split('=')

LHS=Ltemp1[0]
RHS='0'
if len(Ltemp1)==2:
    RHS=Ltemp1[1]



LHStemp=LHS.split('+')
RHStemp=RHS.split('+')

L2=[]
L1=[]

for i in LHStemp:
    L2= i.split('-')
    
    if len(L2)==2:
        L1.append(L2[0])
        L1.append('-'+L2[1])
    elif len(L2)>2:
        L1.append(L2[0])
        for i in range(len(L2)-1):
            L1.append('-'+L2[i+1])
    else:
        L1+=L2
    
for i in RHStemp:
    L2=i.split('-')
    
    if len(L2)==2:
        if L2[0]:
            L1.append('-'+L2[0])
        L1.append(L2[1])
    elif len(L2)>2:
        L1.append('-'+L2[0])
        for i in range(len(L2)-1):
            L1.append(L2[i+1])
    else:
        L1.append('-'+L2[0])
#print(L1)

L3=[]
L4=[]
L5=[]
for i in L1:
    L3=i.split('x^')
    if len(L3)==2:
        if L3[0]:
            if L3[0]!='-':
                L4.append(float(L3[0]))
            else:
                L4.append(-1.0)
        else:
            L4.append(1.0)
        L5.append(int(L3[1]))
    elif 'x' in i:
        L3=i.split('x')
        if L3[0]:
            if L3[0]!='-':
                L4.append(float(i.split('x')[0]))
            else:
                L4.append(-1.0)
        else:
            L4.append(1.0)
        L5.append(1)
    else:
        L4.append(float(i))
        L5.append(0)
        
#print(L4)
#print(L5)

L6=[]
L7=[]

for i in range(len(L5)):
    for j in range(i+1,len(L5)):
        if L5[i]==L5[j]:
            L6.append((L4[i]+L4[j]))
            L7.append(L5[i])

for i in range(len(L5)):
    if L5[i] not in L7:
        L6.append(L4[i])
        L7.append(L5[i])

#print(L6)
#print(L7)


degree=max(L7)


poly=[0]*(degree+1)

for z in range(len(L7)):
    poly[degree-L7[z]]=L6[z]

#print("degree of polynomial is ",len(poly)-1,'\n')



y=len(poly)-1



def func(poly,x0):
        global f
        global df
        f=poly[-1]
        df=0
        y=len(poly)-1
        while y>0:
            df+=y*poly[-y-1]*x0**(y-1)
            y-=1
            f+=poly[-y-2]*x0**(y+1)
            
            
for i in range(len(poly)-1):
    x0=x0=random.random()+(random.random())*1j
    for i in range(75):
        func(poly,x0)
        x0-=f/df
        if f==0:
            break
        
    x0=round(x0.real,5)+round(x0.imag,5)*1j
    print(x0)
    
    if -0.001<x0.imag<0.001:
        j=0
        k=len(poly)
        for i in range(k-1):
            j+=poly[i]
            poly+=[j]
            j*=x0
        poly=poly[k:]
        
    else:
        print(x0.real-x0.imag*1j)
        j=0
        k=len(poly)
        for i in range(k-1):
            j+=poly[i]
            poly+=[j]
            j*=x0
        poly=poly[k:]
        j=0
        k=len(poly)
        for i in range(k-1):
            j+=poly[i]
            poly+=[j]
            j*=(x0.real-x0.imag*1j)
        poly=poly[k:]
        
    if len(poly)<=1:
        break













