#!/usr/bin/env python
# coding: utf-8

# In[87]:


##import random and make 10 lists with a nested for loop

import random
import copy

number=10
length=10

lists_master = []
for i in range(number):
    sub_list = []
    for j in range(length):
        sub_list.append(random.randint(0, 9))
    lists_master.append(sub_list)
print(lists_master)


# In[88]:


##print lists in nic square seperated by space
for i in range (number):
   print(*lists_master[i], sep = " ")


# In[89]:


##Make a copy that does not affect the origional
lists_master2 = copy.deepcopy(lists_master)
print(lists_master2)


# In[90]:


##Convert odd numbers to @ symbol
for i in range (number):
    lists_master2[i] = (["@" if x % 2 != 0 else x for x in lists_master2[i]])



# In[91]:


## print nice list
for i in range (number):
   print(*lists_master2[i], sep = " ")


# In[92]:


##make copy that does not affect origional
lists_master3 = copy.deepcopy(lists_master)
print(lists_master3)


# In[93]:


##Add sum to end of row
for i in range (number):
    sum1=(sum(lists_master3[i]))
    lists_master3[i].append(sum1)


# In[94]:


##Print nicely
for i in range (number):
   print(*lists_master3[i], sep = " ")


# In[ ]:




