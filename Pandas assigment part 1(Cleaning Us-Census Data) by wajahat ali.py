#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing libarary
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import re


# In[17]:


# loading data by using glob  & loop & concatenation all csv files
files = glob("states*")
us_census = pd.concat((pd.read_csv(file) for file in files ),ignore_index=True)
del us_census["Unnamed: 0"]
us_census.head()


# In[3]:


# look .dtypes and .columns
d_types=us_census.dtypes
print("Data types of us_census : \n",d_types)
print('___________________________________')
col= us_census.columns
print("Column of us_census : \n",col)


# In[4]:


# task 4 : look at the Data head Frame dtypes
#so that you can understand why some of these dtypes are objects
#instead of integers or floats.
us_census.head(2).dtypes


# In[5]:


# Use regex to turn the Income column into a format 
# that is ready for conversion into a numerical type
us_census["Income"]=us_census["Income"].replace("\$"," ",regex=True)
us_census['Income'] = us_census['Income'].astype("float")
print("After conversion the Data type of income columns is  : ",us_census['Income'].dtypes)


# In[6]:


#Look at the GenderPop column
#going to separate this into two columns, the Men column, and the Women column.
us_census['GenderPop'][0]


# In[7]:


# Split the column into those two new columns 
#using str.split and separating out columns in to male and female.
# Convert both of the columns into numerical datatypes.

split_gender = us_census['GenderPop'].str.split('_', expand=True)
us_census["female"]=split_gender[1].str.extract('(\d+)',expand=True)
us_census["female"]=pd.to_numeric(us_census["female"])
us_census["Male"]=split_gender[0].str.extract('(\d+)',expand=True)
us_census["Male"]=pd.to_numeric(us_census["Male"])


# In[8]:


us_census.dtypes


# In[9]:


# Use matplotlib to make a scatterplot!
x=us_census["Income"]
y=us_census["female"]
plt.scatter(x,y)
plt.xlabel("Income")
plt.ylabel("female")
plt.show()


# In[10]:


#Did you get an error? These monstrous csv files probably have nan values in them! 
#Print out your column with the number of women per state to see.
female_na_values = us_census["female"][us_census["female"].isnull()]
print(female_na_values)


# In[11]:


# We can fill in those nans by using pandas’ .fillna() function.
#You have the TotalPop per state, and you have the Men per state. 
#As an estimate for the nan values in the Women column,
#you could use the TotalPop of that state minus the Men for that state.

total_pop=us_census["TotalPop"]-us_census["Male"]
us_census['female']=us_census['female'].fillna(value= total_pop)


# In[12]:


# We forgot to check for duplicates! Use .duplicated() on your census DataFrame to see if we have duplicate rows in there.
# Drop those duplicates using the .drop_duplicates() function.
duplicated_row = us_census[us_census.duplicated()]
us_census.drop_duplicates(keep='first',inplace=True)


# In[13]:


# Make the scatterplot again. Now, it should be perfect! 
# Your job is secure, for now.


plt.scatter(x,y)
plt.xlabel("Income")
plt.ylabel("female")
plt.show()


# In[14]:


us_census.dtypes


# In[15]:


# Try to make a histogram for each one!
# You will have to get the columns into numerical format, 
# and those percentage signs will have to go.
#Don’t forget to fill the nan values with something that makes sense!
#You probably dropped the duplicate rows when making your last graph,
#but it couldn’t hurt to check for duplicates again.


# In[16]:


us_census = us_census.replace('%*','',regex=True)
us_census[["Hispanic","White","Black","Native","Asian","Pacific"]] =us_census[["Hispanic","White","Black","Native","Asian","Pacific"]].apply(pd.to_numeric)
us_census[["Hispanic","White","Black","Native","Asian","Pacific"]].fillna(0)
histogram_display =us_census[["Hispanic","White","Black","Native","Asian","Pacific"]].hist(rwidth=0.87)
us_census[["Hispanic","White","Black","Native","Asian","Pacific"]].apply(lambda x :x.drop_duplicates(keep=False,inplace=True))

