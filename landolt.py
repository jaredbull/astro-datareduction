#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[7]:


# copy set of standard stars from database into a .txt file before running script
# default delimiter is whitespace, keep this in mind when extracting desired columns from .txt
    
V_BminusV = np.loadtxt('E:/work/landolt_104.txt',dtype='float',usecols=(9,10))


# In[8]:


# checking that array contains desired values

V_BminusV


# In[9]:


# inspecting array shape to ensure proper indexing

V_BminusV.shape


# In[16]:


# plotting V as a function of B-V for set of standard stars

plt.scatter(V_BminusV[:,1],V_BminusV[:,0])
plt.gca().invert_yaxis()
plt.xlabel('B-V')
plt.ylabel('V')


# In[17]:


# same process for other sets of stars taken from database

V_BminusV = np.loadtxt('E:/work/landolt_110.txt',dtype='float',usecols=(9,10))
plt.scatter(V_BminusV[:,1],V_BminusV[:,0])
plt.gca().invert_yaxis()
plt.xlabel('B-V')
plt.ylabel('V')

