#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[9]:


bmi_dta = pd.read_csv("BMI_Data.csv")
dataframedim = len(bmi_dta) # Save the dimension of the dataframe in the global variable dataframedim
dataframedim # Test that some value is passaed to the dataframe


# In[10]:


if len(bmi_dta) == dataframedim:
    bmi_dta["HeightM"] = bmi_dta["HeightCm"]/100
    bmi_dta["HeightM^2"] = bmi_dta["HeightM"]*bmi_dta["HeightM"]
    bmi_dta["BMI"] = bmi_dta["WeightKg"]/bmi_dta["HeightM^2"]
    bmi_dta["BMI"] = bmi_dta["BMI"].round(2)
    print("<<-----------Following is the drafted content of the dataframe post computation------------>>\n") 
bmi_dta # Explore the newly added columns


# In[11]:


if bmi_dta["BMI"] <= 18.4:
    bmi_dta["BMI_Category"] = "Underweight"
    bmI_dta["Health_Risk"] = "Malnutrition risk"
if bmi_dta["BMI"] <= 24.9:
    bmi_dta["BMI_Category"] = "Normal weight"
    bmI_dta["Health_Risk"] = "Low risk"
if bmi_dta["BMI"] <= 29.9:
    bmi_dta["BMI_Category"] = "Overweight"
    bmI_dta["Health_Risk"] = "Enhanced risk"
if bmi_dta["BMI"] <= 34.9:
    bmi_dta["BMI_Category"] = "Moderately obese"
    bmI_dta["Health_Risk"] = "Medium risk"
if bmi_dta["BMI"] <= 39.9:
    bmi_dta["BMI_Category"] = "Severely obese"
    bmI_dta["Health_Risk"] = "High risk"
if bmi_dta["BMI"] >= 40:
    bmi_dta["BMI_Category"] = "Very severely obese"
    bmI_dta["Health_Risk"] = "Very high risk"
print("<<-----------Following is the drafted content of the dataframe post computation------------>>\n") 
print("\n") 
print("\n")
bmi_dta
print("Next Steps.....\n") 
print("=================================================================================================\n") 
    


# In[ ]:





# In[13]:


bmi_dta


# In[14]:


bmi_dta[bmi_dta['BMI'] <= 18.4]


# In[15]:


bmi_dta[bmi_dta['BMI'] <= 18.4]


# In[28]:


filter1 = bmi_dta["BMI"] >=18.5


# In[29]:


filter2 = bmi_dta["BMI"] <=24.9


# In[33]:


bmi_dta.where(filter1 & filter2)


# In[35]:


bmi_dta[bmi_dta["BMI"].between(18.5,24.9,inclusive = True)] ##### Use this condition to complete the project


# In[36]:


if bmi_dta["BMI"].between(18.5,24.9,inclusive = True):
    bmi_dta["BMI_Category"] = "Normal weight"
    bmI_dta["Health_Risk"] = "Low risk"


# In[55]:


set2 = bmi_dta[(bmi_dta["BMI"]>=18.5) & (bmi_dta["BMI"]<=24.9)]


# In[57]:


set2


# # This is the Solution Code START

# In[67]:


bmi_dta["BMI_CATEGORY"] = ""


# In[68]:


bmi_dta["Health_Risk"] = ""


# In[69]:


bmi_dta


# In[72]:


bmi_dta.loc[(bmi_dta["BMI"]>=18.5) & (bmi_dta["BMI"]<=24.9), "BMI_CATEGORY"] = "Normal weight"


# In[70]:


bmi_dta.loc[(bmi_dta["BMI"]>=18.5) & (bmi_dta["BMI"]<=24.9), "Health_Risk"] = "Low risk"


# In[73]:


bmi_dta


# In[ ]:


## Dynamic code


# In[76]:


minima_1 = 25


# In[77]:


maxima_1 = 29.9


# In[82]:


bmi_dta.loc[(bmi_dta["BMI"]>=minima_1) & (bmi_dta["BMI"]<=maxima_1), "BMI_CATEGORY"] = "Overweight"


# In[83]:


bmi_dta.loc[(bmi_dta["BMI"]>=minima_1) & (bmi_dta["BMI"]<=maxima_1), "Health_Risk"] = "Enhanced risk"


# In[84]:


bmi_dta


# In[ ]:





# In[ ]:





# # This is the solution code END

# In[40]:


bmi_dta[bmi_dta['BMI'] <= 29.9]


# In[ ]:





# In[18]:


bmi_dta[bmi_dta['BMI'] <= 34.9]


# In[19]:


bmi_dta[bmi_dta['BMI'] <= 39.9]


# In[20]:


bmi_dta[bmi_dta['BMI'] >= 40]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




