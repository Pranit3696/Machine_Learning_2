#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.patches as mpatches
import seaborn as sns


# In[11]:


cd C:\Users\prani\Desktop\GlobalTerrorism


# In[18]:


df =pd.read_csv("globalterrorismdb_0718dist.csv",encoding = "latin1")
df = pd.DataFrame(df)
print("Data has been successfully imported")
df.head()


# In[19]:


df.head()


# In[20]:


df.info()


# In[21]:


df.shape


# In[22]:


df.columns


# In[23]:


for i in df.columns:
    print(i,end=",")


# # Cleaning the Data

# In[24]:


df = df[["iyear","imonth","iday","country_txt","region_txt","provstate","city"
         ,"latitude","longitude","summary","attacktype1_txt","targtype1_txt","gname"
         ,"motive","weaptype1_txt","nkill","nwound","addnotes"]]
df.head()


# In[25]:


df.rename(columns = {"iyear":"Year","imonth":"Month","iday":"Day","country_txt":"Country","region_txt":"Region",
                     "provstate":"Province/State","city":"City","latitude":"Latitude","longitude":"Longitude","location":"Location","summary":"Summary","attacktype1_txt":"Attack Type",
                    "targtype1_txt":"Targe Type","gname":"Group Name","motive":"Motive","weaptype1_txt":"Weapon Type","nkill":"Killed","nwound":"Wounded","addnotes":"Add Notes"},inplace=True)


# In[26]:


df.head()


# In[27]:


df.info()


# In[29]:


df.shape


# In[31]:


df.isnull().sum()


# In[34]:


df["Killed"]=df["Killed"].fillna(0)
df["Wounded"]=df["Wounded"].fillna(0)
df["Casualty"]=df["Killed"]+df["Wounded"]


# In[35]:


df.describe()


# Observation:

# 1.)The data consists of terrorist activities ranging from the year:1970 to 2017
# 
# 2.)Maximum number of people killed in an event were :1570
# 
# 3.)Maximum number of people wounded in an event were:8191
# 
# 4.)Maximum number of total casualities in an event were :9574

# # Visualizing the data

# ## 1. Year wise Attacks
# 

# In[38]:


attacks = df["Year"].value_counts(dropna = False).sort_index().to_frame().reset_index().rename(columns={"index":"Year","Year":"Attacks"}).set_index("Year")
attacks.head()


# In[39]:


attacks.plot(kind="bar",color="cornflowerblue",figsize=(15,6),fontsize=13)
plt.title("Timeline of Attacks",fontsize=15)
plt.xlabel("Years",fontsize=15)
plt.ylabel("Number of Attacks",fontsize = 15)
plt.show()


# 1.)Most number of Attacks(16903) in 2014
# 
# 2.)Least number of Attacks(471) in 1971
# 

# In[40]:


yc = df[["Year","Casualty"]].groupby("Year").sum()
yc.head()


# In[41]:


yc.plot(kind = "bar",color="cornflowerblue",figsize =(15,6))
plt.title("Year wise Casualties",fontsize = 13)


# In[43]:


yk = df[["Year","Killed"]].groupby("Year").sum()
yk.head()


# 4.Wounded in each Region

# In[44]:


yw=df[["Year","Wounded"]].groupby("Year").sum()
yw.head()


# In[48]:


fig = plt.figure()
ax0=fig.add_subplot(2,1,1)
ax1=fig.add_subplot(2,1,2)
#killed

yk.plot(kind="bar",color="cornflowerblue",figsize=(15,15),ax=ax0)
ax0.set_title("People killed in each Year")
ax0.set_xlabel("Years")
ax0.set_ylabel("Number of People Killed")

#Wounded

yw.plot(kind="bar",color="cornflowerblue",figsize=(15,15),ax=ax1)
ax1.set_title("People wounded in each Year")
ax1.set_xlabel("Years")
ax1.set_ylabel("Number of People Wounded")

plt.show()


# #  Region wise Attacks
# 

# 1.) Distribution of Terrorist Attacks over Regions from 1970-2017
# 

# In[50]:


reg=pd.crosstab(df.Year,df.Region)
reg.head()


# In[51]:


reg.plot(kind="area",stacked=False,alpha=0.5,figsize=(20,10))
plt.title("Region wise attacks",fontsize =20)
plt.xlabel("Years",fontsize=20)
plt.ylabel("Number of Attacks",fontsize=20)
plt.show()


# Total Terrorist Attacks in each Region from 1970-2017

# In[52]:


regt = reg.transpose()
regt["Total"]=regt.sum(axis = 1)
ra=regt["Total"].sort_values(ascending = False)
ra


# In[53]:


ra.plot(kind='bar',figsize=(15,6))
plt.title("Total Number of Attacks in each Region from 1970-2017")
plt.xlabel("Region")
plt.ylabel("Number of Attacks")
plt.show()


# In[55]:


rc = df[["Region","Casualty"]].groupby("Region").sum().sort_values(by="Casualty",ascending=False)
rc


# 4.Killed in each Region

# In[56]:


rk = df[["Region","Killed"]].groupby("Region").sum().sort_values(by="Killed",ascending=False)
rk


# # Country Wise Attacks -Top 10

# In[57]:


ct = df["Country"].value_counts().head(10)
ct


# In[59]:


ct.plot(kind="bar",color="cornflowerblue",figsize=(15,6))
plt.title("Country wise Attacks",fontsize = 13)
plt.xlabel("Countries",fontsize=13)
plt.xticks(fontsize=12)
plt.ylabel("Number of Attacks",fontsize=13)
plt.show()


# 2. Total Casualties(Killed + Wounded) in each Country

# In[60]:


cnc = df[["Country","Casualty"]].groupby("Country").sum().sort_values(by="Casualty",ascending=False)
cnc.head(10)


# In[62]:


cnc[:10].plot(kind="bar",color="cornflowerblue",figsize=(15,6))
plt.title("Country wise Casualties",fontsize =13)
plt.xlabel("Countries",fontsize =13)
plt.xticks(fontsize = 12)
plt.ylabel("Number of Casualties",fontsize=13)
plt.show()


# # Humanity Affected (World-wide) by Terrorist Attacks from 1970 to 2017

# 1.Total Casualties(Killed + Wounded) due to Terrorist Attacks

# Casualties due to terrorist attacks

# In[69]:


casualty=df.loc[:,"Casualty"].sum()
print("Total number of Casualties due to Terrorist attacks from 1970 to 2017 across the world :\n",casualty)


# Kills due to terrorist attacks

# In[70]:


Kill=df.loc[:,"Killed"].sum()
print("Total number of Kills due to Terrorist attacks from 1970 to 2017 across the world :\n",Kill)


# In[ ]:





# # Observation 

# 1.)Most number of Attacks(16903) in 2014
# 
# 2.)Least number of Attacks(471) in 1971
# 
# 
# 
