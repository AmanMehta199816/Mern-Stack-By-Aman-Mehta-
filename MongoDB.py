#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pymongo


# In[2]:


import pymongo


# In[3]:


client = pymongo.MongoClient("mongodb://localhost:27017/")


# In[4]:


database=client["mydatabase"]


# In[5]:


document={"name":"john","age":30}


# In[9]:


db = client["mydatabase"] 


# In[10]:


collection = db["mycollection"]


# In[11]:


insert_result = collection.insert_one(document)


# In[12]:


print("Inserted document ID:", insert_result.inserted_id)


# In[ ]:




