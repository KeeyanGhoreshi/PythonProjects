'''
Created on Apr 8, 2017

@author: Keeyan
'''

import re

def merge(l1,l2):
    orig = []
    while len(l1) != 0 and len(l2) !=0:
        if(l1[0] < l2[0]):
            orig.append(l1[0])
            l1.remove(l1[0])
        else:
            orig.append(l2[0])
            l2.remove(l2[0])
            
    if(len(l1)==0):
        orig += l2
    else:
        orig+= l1
    return orig
 
def MergeSort(aOrig):
    length = len(aOrig)
    if length <= 1:
        return aOrig
        
    a1 = aOrig[:length/2]
    a2 = aOrig[length/2:]    
    return merge(MergeSort(a1),MergeSort(a2))
    
    
def dateRevert(dateArray):
    m = []
    s = "/"
    for date in dateArray:
        a = s.join(str(date).split("."))
        m.append(a)
    return m
def dateSort(dateArray):
    m = []
    for date in dateArray:
        a = date.split("/")
        if(len(a) ==2):
            m.append(float(a[0]) + float(a[1])/100)
    return dateRevert(MergeSort(m))

if __name__ == "__main__":
    print (dateSort(["4/5","5/4","4/31","5/23"]))  
    
        