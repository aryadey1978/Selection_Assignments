#!/usr/bin/env python
# coding: utf-8

# # Body Mass Index (BMI) Calculator Simulation Code

# ## Build

# #### Include all necessary python libratirs to the code simulator

# In[56]:


import os
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import mimetypes
from email.message import EmailMessage


# In[ ]:





# #### Define Global Constants to contain the Range related values pertaining to the BMI

# In[57]:


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

# In[58]:


bmi_dta = pd.read_csv("BMI_Data.csv")
dataframedim = len(bmi_dta) # Save the dimension of the dataframe in the global variable dataframedim


# #### This Block would check the statistics of the newly created dataframe post data load as follows

# In[59]:


bmi_dta.info()


# #### This Block will display the contents of the dataframe independently as of its latest state

# In[60]:


bmi_dta.head()


# #### This Block will add the Custom columns HeightM & HeightM^2 to calculate height in meters and get it squared

# In[61]:


# HeightM: Calculated field to convert HeightCm values to meters
# HeightM^2: Calculated field to perform the square of the height in meters
# BMI: Calculated field that calculates the BMI based on BMI formula rpovided in the document "BMI Calculator Challenge v6.pdf"
# Next step is to round of the calculated BMI to 2 decimal places
# Explore the contents of the dataframe after adding these calculated fields


# In[62]:


if len(bmi_dta) == dataframedim:
    bmi_dta["HeightM"] = bmi_dta["HeightCm"]/100
    bmi_dta["HeightM^2"] = bmi_dta["HeightM"]*bmi_dta["HeightM"]
    bmi_dta["BMI"] = bmi_dta["WeightKg"]/bmi_dta["HeightM^2"]
    bmi_dta["BMI"] = bmi_dta["BMI"].round(2)
    print("<<-----------Following is the drafted content of the dataframe post computation------------>>\n") 
bmi_dta # Explore the newly added columns


# #### This Block calculates the BMI Category & Health Risk of the patient depending on their BMI by adding these columns

# In[63]:


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

# In[64]:


bmi_dta.groupby("BMI_CATEGORY")["BMI"].count().round(2).sort_values()


# #### This Block will email the contents of dataframe bmi_dta via an excel to dey.arya@gmail.com & aryade@yahoo.com

# In[65]:


bmi_dta.to_excel (r"C:\Users\User\Desktop\Vamstar\export_bmi_dta.xlsx", index = False, header=True) # Sending the excel to C:\Users\User


# In[66]:


# The following piece of code will attach 'export_bmi_dta.xlsx' from C:\Users\User 
# from dey.arya@gmail.com and send it to aryade@yahoo.com


# In[67]:


from_email_addr = "dey.arya@gmail.com"
to_email_addr = "aryade@yahoo.com"
msg = MIMEMultipart()
msg['From'] = from_email_addr
msg['To'] = to_email_addr
msg['Subject'] = "Body Mass Index Report"
body = "Body Mass Index Report for today is attached with this email. Please review it....."
msg.attach(MIMEText(body, 'plain'))
filename = "export_bmi_dta.xlsx"
attachment = open(r"C:\Users\User\Desktop\Vamstar\export_bmi_dta.xlsx", "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_email_addr, "Hello_Saskatoon1978@")
text = msg.as_string()
server.sendmail(from_email_addr, to_email_addr, text)
server.quit()


# ## Unit Testing

# #### Test Case 1: Prove that the object loaded with data is a dataframe and data loaded with was proper without NULLs

# In[68]:


print("Following is the object that has been created with its custom statistics:\n")
bmi_dta.info()


# #### Test Case 2: Check that there are 6 rows in the dataframe and no more

# In[69]:


print("The total number of rows in the dataframe are:", len(bmi_dta))


# #### Test Case 3: Check the content of the dataframe which should match with "BMI_Calculator.xlsx"

# In[70]:


# In this test the content of the dataframe will be exploded first
# The Excel based "BMI_Calculator.xlsx" based out of "BMI_Data.csv" (BMI_Data.csv has been created by the JSON data provided) 
# will be imported into python via bmi_calc_excel_dta dataframe
# The content of bmi_dta & bmi_calc_excel_dta will be mirror images to each other


# In[71]:


bmi_dta # Explode the content of the python BMI Calculator dtaframe


# In[72]:


# Import the excel data into python
bmi_calc_excel_dta = pd.read_excel('BMI_Calculator_1.xlsx', index_col=0)  


# In[73]:


bmi_calc_excel_dta.reset_index() # Explode the content of second dataframe


# In[74]:


bmi_calc_excel_dta["BMI"] = bmi_calc_excel_dta["BMI"].round(2) # Modify the BMI data upto 2 decimal places


# In[75]:


bmi_calc_excel_dta.reset_index() # Explode the contents of BMI_Calculator.xslx dataframe 
# Data is matching


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




