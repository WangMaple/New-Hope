#!/usr/bin/env python
# coding: utf-8

# In[107]:


import numpy as np


# In[108]:


import pandas as pd


# In[109]:


from pandas import DataFrame as df


# In[110]:


sum(np.arange(2,100,2))


# In[ ]:





# In[111]:


data= {'姓名':['张飞','关羽','刘备','典韦','许褚'],'语文':[68,95,98,90,80],'数学':[65,76,86,88,90],'英语':[30,98,88,77,90]}


# In[112]:


df1=df(data)


# In[113]:


df1['total']=df1.sum(axis=1)


# In[114]:


df1.sort_values('total')


# In[115]:


df1.describe()


# In[ ]:





# In[147]:


complain= pd.read_csv('car_complain.csv')


# In[162]:


def f(x):
    x= x.replace('一汽大众','一汽-大众')
    return x

complain['brand']=complain['brand'].apply(f)


# In[163]:


complain_new= complain.drop('problem',axis=1).join(complain.problem.str.get_dummies(','))


# In[184]:


complain_new


# In[185]:


tags=complain_new.columns[7:]


# In[186]:


complain_count=complain_new.groupby(['brand'])[tags].agg(['sum'])


# In[188]:


complain_count.insert(0,'count','')


# In[190]:


complain_count['count']= complain_count.sum(axis=1)


# In[201]:


complain_count.sort_values('count', ascending= False)


# In[192]:


complain_count_carmodel=complain_new.groupby(['car_model'])[tags].agg(['sum'])


# In[193]:


complain_count_carmodel.insert(0,'count','')


# In[195]:


complain_count_carmodel['count']= complain_count_carmodel.sum(axis=1)


# In[200]:


complain_count_carmodel.sort_values('count',ascending = False)


# In[ ]:




