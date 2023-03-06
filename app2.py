#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install streamlit


# In[2]:


import streamlit as st
import pandas as pd
import numpy as np


# In[ ]:


HairEye = pd.read_csv("HairEyeColor.csv")


# In[ ]:


st.title("Hair Eye Colour Database")


# In[ ]:


InputHair = st.sidebar.selectbox("Select Hair Colour", ("Brown", "Black", "Blond", "Red"))


# In[ ]:


HairEyeSelect = HairEye[HairEye["Hair"] == InputHair]


# In[ ]:


st.dataframe(HairEyeSelect)

