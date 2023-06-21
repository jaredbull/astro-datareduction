#!/usr/bin/env python
# coding: utf-8

# In[4]:


# removing 2 largest values from list1 and associated values from list2

# ex. removing x largest values from unordered list of variances and removing associated mean counts from second list 
# since both lists are not ordered from lowest to highest exposure time, index of max value from variance list must be found
# and removed from both lists, iterated x times

# this process is useful for when lists are not ordered from highest to lowest, lowest to highests, or etc., where index slicing
# cannot be used

mylist1 = [1, 4, 0, 3, 2]
mylist2 = [5, 2, 9, 1, 0]

for x in range(2):
    i = mylist1.index(max(mylist1))
    mylist1.remove(mylist1[i])
    mylist2.remove(mylist2[i])
    
print(mylist1)
print()
print(mylist2)

