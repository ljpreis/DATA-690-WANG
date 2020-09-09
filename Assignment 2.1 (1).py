#!/usr/bin/env python
# coding: utf-8

# In[5]:



## Define a function that is a while loop which asks for an integer and gives error when integer is not entered
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput 
       break 
    
## Create a list that is empty and use a while loop to call the integer function until we get 10 integers
input_string = [] 
maxLengthList = 10
while len(input_string) < maxLengthList:
    item = inputNumber("Please enter a Number")
    input_string.append(item)
print("user list is")
print(input_string)

for i in range(0, len(input_string)): 
    input_string[i] = int(input_string[i]) 
# Calculating the sum of input list elements
a = input_string
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





# In[ ]:





# In[ ]:




