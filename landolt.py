#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import pandas as pd
import os
from glob import glob
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


# In[3]:


# reading in data for RA and DEC for all stars
# 'pd.read_table()' works best for this case since columns are separated by tabbed spaces

landolt_radec = pd.read_table('E:/work/landolt_110.txt',header=None,usecols=[0,2,3])
landolt_radec


# In[4]:


# making lists of RA and DEC for all stars in set

RA = landolt_radec[2]
DEC = landolt_radec[3]
c = SkyCoord(RA,DEC,unit=(u.hourangle, u.deg))
c


# In[9]:


FOV = np.sqrt(50)

plt.scatter(c.ra.degree,c.dec.degree)
r = Rectangle((c.ra.degree.mean() - FOV/2,c.dec.degree.mean() - FOV/2),width=FOV,height=FOV
          ,edgecolor='black',facecolor='none')
plt.gca().add_patch(r)
plt.gca().invert_xaxis()
plt.grid()
plt.xlabel('RA (Deg)')
plt.ylabel('DEC (Deg)')

# plotting multiple sets of landolt stars

%matplotlib qt # plots in interactive window
FOV = 1.41 # fov of apogee attached to celestron 6se (symmetic)
landolt_dir = glob('C:/Users/jbull/OneDrive/Documents/School/Apogee-SBIG/landolt/*.txt')
for i in landolt_dir:
    V_BminusV = pd.read_table(i,header=None,usecols=[0,4,5])
    
    landolt_radec = pd.read_table(i,header=None,usecols=[0,2,3])
    RA = landolt_radec[2]
    DEC = landolt_radec[3]
    c = SkyCoord(RA,DEC,unit=(u.hourangle, u.deg))
    
    fig,(ax1,ax2) = plt.subplots(nrows=1,ncols=2,figsize=(10,5))

    # plotting magnitude as a function of color
    ax1.scatter(V_BminusV[5],V_BminusV[4])
    ax1.invert_yaxis()
    ax1.grid()
    ax1.set_xlabel('B-V')
    ax1.set_ylabel('V')
    
    ax2.scatter(c.ra.degree,c.dec.degree)
    
    # plotting fov of apogee attached to celestron 6se
    # method for framing fovs is not optimized to include maximum # of targets
    r = Rectangle((c.ra.degree.mean() - FOV/2,c.dec.degree.mean() - FOV/2),width=FOV,height=FOV
          ,edgecolor='blue',facecolor='none',label='Apogee')
    
    # plotting fov of sbig attached to celestron 6se (non-symmetric)
    r2 = Rectangle((c.ra.degree.mean() - 0.69/2,c.dec.degree.mean() - 0.5165/2),width=0.69,height=0.5165
          ,edgecolor='red',facecolor='none',label='SBIG')
    
    ax2.add_patch(r)
    ax2.add_patch(r2)
    ax2.invert_xaxis()
    ax2.grid()
    ax2.set_xlabel('RA (Deg)')
    ax2.set_ylabel('DEC (Deg)')

    plt.suptitle(os.path.basename(i)) # sets title to filename rather than entire path
    plt.tight_layout()
    plt.legend()
    plt.waitforbuttonpress(timeout=-1) # setting to -1 removes timeout
    plt.close()
