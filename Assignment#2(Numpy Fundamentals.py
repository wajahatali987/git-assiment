#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# 

# In[4]:


import numpy as np
arr=np.array([0,1,2,3,4,5,6,7,8,9]).reshape(2,5)
arr


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[5]:


a=np.arange(0,10)
b=np.ones(10)
c=np.hsplit(a,2)
d=np.hsplit(b,2)
np.vstack((c,d))


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[6]:


a=np.arange(0,10)
b=np.ones(10)
c=np.hsplit(a,2)
d=np.hsplit(b,2)
np.hstack((c,d))


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[8]:


arr=np.array([(0,1,2,3,4),(5,6,7,8,9)])
arr.ravel()


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[10]:


a=np.arange(0,15)
b=a.reshape(3,5)
c=b.ravel()
c


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[11]:


a=np.arange(0,15)
a.reshape(5,3)


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[12]:


a=np.arange(0,25).reshape(5,5)
a**2


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[14]:


a=np.arange(0,30).reshape(5,6)
a.mean()


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[15]:


np.std(a)


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[16]:


np.median(a)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[17]:


np.transpose(a)


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[18]:


a=np.arange(0,16).reshape(4,4)
np.trace(a)


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[19]:


np.linalg.det(a)


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[20]:


np.percentile(a,[5,95])


# ## Question:15

# ### How to find if a given array has any null values?

# In[ ]:


a==0

