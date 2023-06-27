import numpy as np
import matplotlib.pyplot as plt
from glob import glob
from scipy.optimize import curve_fit
from astropy.io.fits import getval, getdata
from ccdproc import ImageFileCollection, combine


# In[22]:


flat_collection = ImageFileCollection('E:/work/calib_06222023/apogee_dark/',glob_include='*.fit')


# In[23]:


flat_collection.summary


# In[ ]:


# creating master bias


# In[4]:


# generating list of exposure times for set of images
# use directory of first image in each exposure set to ensure each time is only added once

exp_time = []
dark_dir1 = glob('E:/work/calib_06222023/apogee_dark/*001.fit')
for i in dark_dir1:
    exp_time.append(getval(i,'exptime'))


# In[34]:


# list directory of all darks and place each set of exposures into separate lists

dark_dir = glob('E:/work/calib_06222023/apogee_dark/*.fit')

for x in exp_time:
    dark_list = []
    for y in dark_dir:
        if getval(y,'exptime') == x:
            dark_list.append(y)
        else:
            continue
    print(dark_list)


# In[33]:


# ensure order of groups within list match up with order of exposure times

exp_time


# In[3]:


# creating master bias

bias_dir = glob('E:/work/calib_06222023/apogee_bias/*fit')
bias_data = [getdata(i) for i in bias_dir]
bias_median = np.median(bias_data,axis=0)


# In[12]:


# apply method to stack each group of exposures for sets that have extra images

dark_dir = glob('E:/work/calib_06222023/apogee_dark/*.fit')

dark_combined = []

for x in exp_time:
    dark_list = []
    for y in dark_dir:
        if getval(y,'exptime') == x:
            dark_list.append(getdata(y))
        else:
            continue
    dark_combined.append(np.median(dark_list,axis=0) - bias_median)


# In[13]:


# calculating mean dark counts for each exposure time

dark_mean = []

for i in dark_combined:
    dark_mean.append(i.mean())


# In[18]:


# fitting a line to the data

def func(x,a,b):
    y = a * x + b
    return y

fit = curve_fit(func,exp_time,dark_mean)[0]


# In[19]:


xfit = np.linspace(min(exp_time),max(exp_time),100)

plt.scatter(exp_time,dark_mean)
plt.plot(xfit,func(xfit,*fit))
plt.title('Apogee Dark Current')
plt.xlabel('Exposure Time (s)')
plt.ylabel('Mean Dark Counts (ADU)')

