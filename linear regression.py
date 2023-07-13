#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model


# In[17]:


df = pd.read_csv('framingham.csv')
df


# In[18]:


sns.lmplot(x='BMI', y='currentSmoker', data=df,aspect=2, height=6)
plt.xlabel('Boby Mass Index$(kg/m^2)$: as Independent variable')
plt.ylabel('currentSmoker: as Dependent variable')
plt.title('currentSmoker Vs BMI');


# In[19]:


sns.lmplot(x='BMI', y='cigsPerDay', data=df,aspect=2, height=6)
plt.xlabel('Boby Mass Index$(kg/m^2)$: as Independent variable')
plt.ylabel('cigsPerDay: as Dependent variable')
plt.title('cigsPerDay Vs BMI');


# In[27]:


sns.lmplot(x='BMI', y='BPMeds', data=df,aspect=2, height=6)
plt.xlabel('Boby Mass Index$(kg/m^2)$: as Independent variable')
plt.ylabel('BPMeds: as Dependent variable')
plt.title('BPMeds Vs BMI');


# In[29]:


sns.lmplot(x='BMI', y='prevalentStroke', data=df,aspect=2, height=6)
plt.xlabel('Boby Mass Index$(kg/m^2)$: as Independent variable')
plt.ylabel('prevalentstroke: as Dependent variable')
plt.title('prevalentstroke Vs BMI');


# In[31]:


sns.lmplot(x='BMI', y='prevalentHyp', data=df,aspect=2, height=6)
plt.xlabel('Boby Mass Index$(kg/m^2)$: as Independent variable')
plt.ylabel('prevalentHyp: as Dependent variable')
plt.title('prevalentHyp Vs BMI');


# In[32]:


sns.lmplot(x='BMI', y='diabetes', data=df,aspect=2, height=6)
plt.xlabel('Boby Mass Index$(kg/m^2)$: as Independent variable')
plt.ylabel('diabetes: as Dependent variable')
plt.title('diabetes Vs BMI');


# In[33]:


sns.lmplot(x='BMI', y='totChol', data=df,aspect=2, height=6)
plt.xlabel('Boby Mass Index$(kg/m^2)$: as Independent variable')
plt.ylabel('totChol: as Dependent variable')
plt.title('totChol Vs BMI');


# In[34]:


sns.lmplot(x='BMI', y='sysBP', data=df,aspect=2, height=6)
plt.xlabel('Boby Mass Index$(kg/m^2)$: as Independent variable')
plt.ylabel('sysBP: as Dependent variable')
plt.title('sysBP Vs BMI');


# In[38]:


sns.lmplot(x='BMI', y='BMI', data=df,aspect=2, height=6)
plt.xlabel('Boby Mass Index$(kg/m^2)$: as Independent variable')
plt.ylabel('BMI: as Dependent variable')
plt.title('BMI Vs BMI');


# In[39]:


sns.lmplot(x='BMI', y='heartRate', data=df,aspect=2, height=6)
plt.xlabel('Boby Mass Index$(kg/m^2)$: as Independent variable')
plt.ylabel('heartRate: as Dependent variable')
plt.title('heartRate Vs BMI');


# In[40]:


sns.lmplot(x='BMI', y='glucose', data=df,aspect=2, height=6)
plt.xlabel('Boby Mass Index$(kg/m^2)$: as Independent variable')
plt.ylabel('glucose: as Dependent variable')
plt.title('glucose Vs BMI');


# In[41]:


sns.lmplot(x='BMI', y='TenYearCHD', data=df,aspect=2, height=6)
plt.xlabel('Boby Mass Index$(kg/m^2)$: as Independent variable')
plt.ylabel('TenYearCHD: as Dependent variable')
plt.title('TenYearCHD Vs BMI');


# In[ ]:




