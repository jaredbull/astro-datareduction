#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from scipy.optimize import curve_fit
from astropy.io.fits import getval, getdata
from ccdproc import ImageFileCollection, combine


# In[11]:


# creating master bias

bias_dir = glob('E:/work/calib_06222023/apogee_bias/*fit')
bias_data = [getdata(i) for i in bias_dir]
bias_median = np.median(bias_data,axis=0).astype('float')


# In[2]:


# calculating noise variance as a function of mean counts

flat1_dir = glob('E:/work/calib_06222023/apogee_flat/*1.fit')
flat2_dir = glob('E:/work/calib_06222023/apogee_flat/*2.fit')

var = []
flat_mean = []

for i in range(len(flat1_dir)):
    flat1 = getdata(flat1_dir[i])
    flat1 = flat1.astype('float')
    flat_mean.append(flat1.mean())
    
    flat2 = getdata(flat2_dir[i])
    flat2 = flat2.astype('float')
    
    flat_sub = flat1 - flat2
    var.append(np.var(flat_sub) / 2)


# In[8]:


# the reciprocal of the slope gives the conversion factor, g, in electrons/ADU

var_sliced = var.copy()
flatmean_sliced = flat_mean.copy()

for x in range(3):
    i = flatmean_sliced.index(max(flatmean_sliced))
    var_sliced.remove(var_sliced[i])
    flatmean_sliced.remove(flatmean_sliced[i])

def func(x,a,b):
    y = a * x + b
    return y

fit1 = curve_fit(func, xdata=flatmean_sliced, ydata=var_sliced)[0]
x_true = np.linspace(np.min(flat_mean),np.max(flat_mean),100)

plt.scatter(flat_mean,var)
plt.plot(x_true,func(x_true,*fit1))


# In[ ]:


# inspect header info of folder of images

dark_collection = ImageFileCollection('E:/work/calib_06222023/apogee_dark/',glob_include='*.fit')
dark_collection.summary


# In[12]:


# generating list of exposure times for set of images
# use directory of first image in each exposure set to ensure each time is only added once

exp_time = []
dark_dir = glob('E:/work/calib_06222023/apogee_dark/*001.fit')
for i in dark_dir:
    exp_time.append(getval(i,'exptime'))

# list directory of all darks and place each set of exposures into separate lists
# apply method to stack each group of exposures for sets that have extra images

dark_dir = glob('E:/work/calib_06222023/apogee_dark/*.fit')

dark_combined = []

for x in exp_time:
    dark_list = []
    for y in dark_dir:
        if getval(y,'exptime') == x:
            dark_list.append(getdata(y).astype('float'))
        else:
            continue
    dark_combined.append(np.median(dark_list,axis=0) - bias_median)

# calculating mean dark counts for each exposure time    

dark_mean = []

for i in dark_combined:
    dark_mean.append(i.mean())


# In[13]:


# plotting dark current

def func(x,a,b):
    y = a * x + b
    return y

fit2 = curve_fit(func,exp_time,dark_mean)[0]

xfit = np.linspace(min(exp_time),max(exp_time),100)

plt.scatter(exp_time,dark_mean)
plt.plot(xfit,func(xfit,*fit2))
plt.xlabel('Exposure Time (s)')
plt.ylabel('Mean Dark Counts (ADU)')


# In[15]:


# multiplying the slope of this fit (in ADU/s) by the conversion factor, g, gives the typical dark current
# this value can be compared to the value provided in the CCDs spec sheet

print(fit2[0]*(1/fit1[0]))


# In[17]:


# same process for SBIG ccd

bias_dir = glob('E:/work/calib_06222023/sbig_bias/*fit')
bias_data = [getdata(i) for i in bias_dir]
bias_median = np.median(bias_data,axis=0).astype('float')

flat1_dir = glob('E:/work/calib_06222023/sbig_flat/*1.fit')
flat2_dir = glob('E:/work/calib_06222023/sbig_flat/*2.fit')

var = []
flat_mean = []

for i in range(len(flat1_dir)):
    flat1 = getdata(flat1_dir[i])
    flat1 = flat1.astype('float')
    flat_mean.append(flat1.mean())
    
    flat2 = getdata(flat2_dir[i])
    flat2 = flat2.astype('float')
    
    flat_sub = flat1 - flat2
    var.append(np.var(flat_sub) / 2)
    
var_sliced = var.copy()
flatmean_sliced = flat_mean.copy()

for x in range(3):
    i = flatmean_sliced.index(max(flatmean_sliced))
    var_sliced.remove(var_sliced[i])
    flatmean_sliced.remove(flatmean_sliced[i])

def func(x,a,b):
    y = a * x + b
    return y

fit1 = curve_fit(func, xdata=flatmean_sliced, ydata=var_sliced)[0]
x_true = np.linspace(np.min(flat_mean),np.max(flat_mean),100)

plt.scatter(flat_mean,var)
plt.plot(x_true,func(x_true,*fit1))


# In[18]:


exp_time = []
dark_dir = glob('E:/work/calib_06222023/sbig_dark_06222023/*001.fit')
for i in dark_dir:
    exp_time.append(getval(i,'exptime'))
    
dark_dir = glob('E:/work/calib_06222023/sbig_dark_06222023/*.fit')

dark_combined = []

for x in exp_time:
    dark_list = []
    for y in dark_dir:
        if getval(y,'exptime') == x:
            dark_list.append(getdata(y).astype('float'))
        else:
            continue
    dark_combined.append(np.median(dark_list,axis=0) - bias_median)
    
dark_mean = []

for i in dark_combined:
    dark_mean.append(i.mean())

def func(x,a,b):
    y = a * x + b
    return y

fit2 = curve_fit(func,exp_time,dark_mean)[0]

xfit = np.linspace(min(exp_time),max(exp_time),100)

plt.scatter(exp_time,dark_mean)
plt.plot(xfit,func(xfit,*fit2))
plt.xlabel('Exposure Time (s)')
plt.ylabel('Mean Dark Counts (ADU)')


# In[19]:


print(fit2[0]*(1/fit1[0]))

