#!/usr/bin/env python
# coding: utf-8

# In[93]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[94]:


df=pd.read_excel('credit_card.xls')
df


# In[95]:


df[df['Age']<18]


# In[96]:


df1=pd.read_excel('credit_2.xlsx')
df1


# In[97]:


def age(age):
    if age<18:
        return 18
    else:
        return age


# In[98]:


df['Age']=df['Age'].apply(age)


# In[99]:


df=df.drop('Sl No:',axis=1)


# In[100]:


df1=df1.drop('Sl No:',axis=1)


# In[101]:


df2=df1.groupby('Costomer').sum()
df2=df2.reset_index()


# In[102]:


df2.sort_values('Amount.1',ascending=False).head(10)


# In[103]:


df3=pd.merge(df,df2,how='inner',left_on='Customer',right_on='Costomer')
df3


# In[104]:


df3.info()


# In[105]:


df3['Amount'][0]


# In[106]:


df3.groupby('Age').mean().sort_values('Amount',ascending=False)


# In[107]:


df3.groupby('Segment').mean().sort_values('Amount',ascending=False)


# In[114]:


df3['overspent']=df3['Limit']-df3['Amount']


# In[116]:


df3['overrepayment']=df3['Amount.1']-df3['Amount']


# In[117]:


df3


# In[119]:


def tax(spent):
    if spent<0:
        return -2
    else:
        return 0


# In[120]:


def subs(spent):
    if spent>0:
        return 2
    else:
        return 0


# In[122]:


df3['tax']=df3['overspent'].apply(tax)


# In[123]:


df3['subs']=df3['overrepayment'].apply(subs)


# In[124]:


df3


# In[129]:


df3['total']=(df3['tax']+df3['subs'])*(df3['Limit'])/100


# In[130]:


df3


# In[133]:


df3.groupby('Segment').mean()


# In[134]:


df3.groupby('Segment').mean()['total'].sum()


# In[135]:


df1.groupby('Type').sum()


# In[136]:


df3['Intrest']=2.9*(-df3['overrepayment'])/100


# In[137]:


def intrest(k):
    if k>0:
        return k
    if k<0:
        return 0


# In[138]:


df3['Intrest']=df3['Intrest'].apply(intrest)


# In[139]:


df3


# In[ ]:




