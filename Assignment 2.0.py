#!/usr/bin/env python
# coding: utf-8

# In[6]:


input_string = input("Enter a list numbers separated by comma ")

#Asks User to input numbers and seperate by comma
print("\n")
a = input_string.split(",")
#Printing users list
print("user list is ", a)
#Converting list to integers
for i in range(0, len(a)): 
    a[i] = int(a[i]) 
# Calculating the sum of input list elements
sum1 = 0
for num in a:
    sum1 = sum1 + (num)
# Calculating min and max
max1 = max(a) 
min1 = min(a)

# Calculating the mean
mean1 = sum1/len(a)

# Calculating Variance
n=len(a)
deviations = [(x - mean1)**2 for x in a]
sum2 = 0
for num in deviations:
    sum2 = sum2 + (num)
    
var1 = sum2/n

#calculating standard deviation

import math

std_dev = math.sqrt(var1)

#Prints assignment answers
print(a)
print("Sum = ", sum1)
print ("Max =", max1)
print ("Min =", min1)
print ("Range =",min1,"-",max1)
print ("Mean =",mean1)
print ("Variance =", var1)
print ("Standard Deviation", std_dev)


# In[ ]:




