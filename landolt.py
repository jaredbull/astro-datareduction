#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from astropy import units as u
from astropy.coordinates import SkyCoord


# In[3]:


# copy set of standard stars from database into a .txt file before running script
# default delimiter is whitespace, keep this in mind when extracting desired columns from .txt
# pandas would likely work better in general for this
    
V_BminusV = np.loadtxt('E:/work/landolt_104.txt',dtype='float',usecols=(9,10))


# In[8]:


# checking that array contains desired values

V_BminusV


# In[9]:


# inspecting array shape to ensure proper indexing

V_BminusV.shape


# In[4]:


# plotting V as a function of B-V for set of standard stars

plt.scatter(V_BminusV[:,1],V_BminusV[:,0])
plt.gca().invert_yaxis()
plt.xlabel('B-V')
plt.ylabel('V')


# In[5]:


# same process for other sets of stars taken from database

V_BminusV = np.loadtxt('E:/work/landolt_110.txt',dtype='float',usecols=(9,10))
plt.scatter(V_BminusV[:,1],V_BminusV[:,0])
plt.gca().invert_yaxis()
plt.xlabel('B-V')
plt.ylabel('V')


# In[2]:


# reading in data for RA and DEC for all stars
# 'pd.read_table()' works best for this case since columns are separated by tabbed spaces

landolt_radec = pd.read_table('E:/work/landolt_110.txt',header=None,usecols=[0,2,3])
landolt_radec


# In[7]:


# making lists of RA and DEC for all stars in set

RA = landolt_radec[2]
DEC = landolt_radec[3]
c = SkyCoord(RA,DEC,unit=(u.hourangle, u.deg))
c


# In[26]:


plt.scatter(c.ra.degree,c.dec.degree)
plt.gca().invert_xaxis()
plt.grid()
plt.xlabel('RA (Deg)')
plt.ylabel('DEC (Deg)')

