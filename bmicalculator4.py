#!/usr/bin/env python
# coding: utf-8

# # Body Mass Index (BMI) Calculator Simulation Code

# #### Include all necessary python libratirs to the code simulator

# In[21]:


import os
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# #### Define Global Constants to contain the Range related values pertaining to the BMI

# In[22]:


maxima_1 = 18.4
minima_2 = 18.5
maxima_2 = 24.9
minima_3 = 25
maxima_3 = 29.9
minima_4 = 30
maxima_4 = 34.9
minima_5 = 35
maxima_5 = 39.9
minima_6 = 40


# #### This Block will initiate the dataframe, test the type and content of the dataframe

# In[23]:


bmi_dta = pd.read_csv("BMI_Data.csv")
dataframedim = len(bmi_dta) # Save the dimension of the dataframe in the global variable dataframedim
dataframedim # Test that some value is passaed to the dataframe


# #### This Block would check the statistics of the created dataframe post data load as follows

# In[24]:


bmi_dta.info()


# #### This Block will display the contents of the dataframe independently as of its latest state

# In[25]:


bmi_dta.head()


# #### This Block will add the Custom columns HeightM & HeightM^2 to calculate height in meters and get it squared

# In[26]:


# HeightM: Calculated field to convert HeightCm values to meters
# HeightM^2: Calculated field to perform the square of the height in meters
# BMI: Calculated field that calculates the BMI based on BMI formula rpovided in the document "BMI Calculator Challenge v6.pdf"
# Next step is to round of the calculated BMI to 2 decimal places
# Explore the contents of the dataframe after adding these calculated fields


# In[27]:


if len(bmi_dta) == dataframedim:
    bmi_dta["HeightM"] = bmi_dta["HeightCm"]/100
    bmi_dta["HeightM^2"] = bmi_dta["HeightM"]*bmi_dta["HeightM"]
    bmi_dta["BMI"] = bmi_dta["WeightKg"]/bmi_dta["HeightM^2"]
    bmi_dta["BMI"] = bmi_dta["BMI"].round(2)
    print("<<-----------Following is the drafted content of the dataframe post computation------------>>\n") 
bmi_dta # Explore the newly added columns


# #### This Block calculates the BMI Category & Health Risk of the patient depending on their BMI by adding these columns

# In[31]:


bmi_dta.loc[(bmi_dta["BMI"]>=maxima_1), "BMI_CATEGORY"] = "Underweight"
bmi_dta.loc[(bmi_dta["BMI"]>=maxima_1), "Health_Risk"] = "Malnutrition risk"
bmi_dta.loc[(bmi_dta["BMI"]>=minima_2) & (bmi_dta["BMI"]<=maxima_2), "BMI_CATEGORY"] = "Normal weight"
bmi_dta.loc[(bmi_dta["BMI"]>=minima_2) & (bmi_dta["BMI"]<=maxima_2), "Health_Risk"] = "Low risk"
bmi_dta.loc[(bmi_dta["BMI"]>=minima_3) & (bmi_dta["BMI"]<=maxima_3), "BMI_CATEGORY"] = "Overweight"
bmi_dta.loc[(bmi_dta["BMI"]>=minima_3) & (bmi_dta["BMI"]<=maxima_3), "Health_Risk"] = "Enhanced risk"
bmi_dta.loc[(bmi_dta["BMI"]>=minima_4) & (bmi_dta["BMI"]<=maxima_4), "BMI_CATEGORY"] = "Moderately obese"
bmi_dta.loc[(bmi_dta["BMI"]>=minima_4) & (bmi_dta["BMI"]<=maxima_4), "Health_Risk"] = "Medium risk"
bmi_dta.loc[(bmi_dta["BMI"]>=minima_5) & (bmi_dta["BMI"]<=maxima_5), "BMI_CATEGORY"] = "Severely obese"
bmi_dta.loc[(bmi_dta["BMI"]>=minima_5) & (bmi_dta["BMI"]<=maxima_5), "Health_Risk"] = "High risk"
bmi_dta.loc[(bmi_dta["BMI"]>=minima_6), "BMI_CATEGORY"] = "Very severely obese"
bmi_dta.loc[(bmi_dta["BMI"]>=minima_6), "Health_Risk"] = "Very high risk"
print("<<-----------Following is the drafted content of the dataframe post computation------------>>\n") 
print("\n") 
print("\n")
bmi_dta    


# #### This Block will calculate the total number of overweight people

# In[36]:


bmi_dta.groupby("BMI_CATEGORY")["BMI"].count().round(2).sort_values()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




