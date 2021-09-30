#!/usr/bin/env python
# coding: utf-8

# # SPEED DATING PROJECT

# ## IMPORT LIBRARIES

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# ## READ THE DATASET

# In[2]:


sd = pd.read_csv("Speed Dating Data.csv", encoding="ISO-8859-1")


# In[3]:


pd.set_option("max_columns", None)
sd.describe()


# pd.set_option("max_columns", None)
# sd.head(15)

# In[5]:


sd.shape


# In[6]:


sd.info(verbose=True, null_counts=True)


# In[7]:


pd.options.display.max_columns
sd.isnull().any()


# # Qui sont les participants ? 

# - Leur genre 

# In[4]:


repart_gender = sd["gender"].value_counts()
sd["gender"]=sd["gender"].replace([1, 0], ["Male", "Female"])
plt.figure()
plt.pie(repart_gender.values, labels=repart_gender.index,  
       autopct='%1.1f%%',
       )
plt.legend(bbox_to_anchor=(1.1, 1.05))
plt.show()


# - Leur âge

# In[6]:


fig=px.bar(data_frame=repart_age, x="age", y="id",  color="age")
fig.show()


# In[11]:


repart_age_gender = sd[['gender', 'age']].groupby('gender').mean().reset_index()
repart_age_gender


# - Leurs origines

# In[74]:


repart_race = sd["race"].value_counts()

sd["race"] = sd["race"].replace([1, 2, 3, 4, 5, 6],
                                ["Black/African American",
                                 "European/Caucasian-American",
                                 "Latino/Hispanic American",
                                 "Asian/Pacific Islander/Asian-American",
                                 "Native American",
                                 "Other"]
                                 )
plt.figure()
plt.pie(repart_race.values, labels=repart_race.index,  
       autopct='%1.1f%%',
       )
plt.legend(bbox_to_anchor=(1.1, 1.05))
plt.show()


# - Leur étude

# In[72]:


repart_study = sd["field_cd"].value_counts()

sd["field_cd"] = sd["field_cd"].replace([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
                                        ["Law", 
                                            "Math",
                                            "Social Science, Psychologist",
                                            "Medical Science, Pharmaceuticals, and Bio Tech",
                                            "Engineering",
                                            "English/Creative Writing/ Journalism",
                                            "History/Religion/Philosophy ",
                                            "Business/Econ/Finance ",
                                            "Education, Academia ",
                                            "Biological Sciences/Chemistry/Physics",
                                            "Social Work ",
                                            "Undergrad/undecided ",
                                            "Political Science/International Affairs ",
                                            "Film",
                                            "Fine Arts/Arts Administration",
                                            "Languages",
                                            "Architecture",
                                            "Other"]
                                          )

plt.figure()
plt.pie(repart_study.values, labels=repart_study.index,  
       autopct='%1.1f%%',
       )
plt.legend(bbox_to_anchor=(1.1, 1.05))
plt.show()


# - Leur but

# In[20]:


sd["goal"] = sd["goal"].replace([1, 2, 3, 4, 5, 6],
                                ["Seemed like a fun night out", 
                                 "To meet new people",
                                 "To get a date",
                                 "Looking for a serious relationship",
                                 "To say I did it",
                                 "Other"],
                                
                                          )

plt.figure()
plt.pie(repart_goal.values, labels=repart_goal.index,  
       autopct='%1.1f%%',
       )
plt.legend(bbox_to_anchor=(1.1, 1.05))
plt.show()


# # Corélation entre les variables et le second rdv 

# - Les centres d'intérets

# In[28]:


int_corr_by_match = sd.groupby("match")["int_corr"].mean().reset_index()
display(int_corr_by_match.head())
print()

fig = px.bar(data_frame=int_corr_by_match, x="match", y="int_corr", color="int_corr")
fig.show()


# In[30]:


race_by_match = sd.groupby("match")["samerace"].mean().reset_index()

fig = px.bar(data_frame=race_by_match, x="match", y="samerace", color="match")
fig.show()

