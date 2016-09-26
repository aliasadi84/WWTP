
# coding: utf-8

# # import libraries

# In[90]:

import csv #to read csv file
import pandas as pd
from pandas import read_csv

import numpy as np
import urllib #to read online data
import datetime as dt #to process date format
import matplotlib.dates as mdates #to porcess date in mlt
from matplotlib import pyplot as plt
from matplotlib import style

import quandl #to do machinelearning
import sklearn

import operator #to sum two or more lists , item by item


# # import data

# ## data is located at:

# In[5]:

# C:\Users\alias\OneDrive for Business\Project\Detroit_Water_Aeration\second_data\aeration_one_sheet.csv


# ## reading dates

# In[91]:

date=[]
temp=[]
with open(r'C:\Users\alias\OneDrive for Business\Project\Detroit_Water_Aeration\second_data\aeration_one_sheet.csv') as csvfile:
    rawdata = csv.reader(csvfile, delimiter=',')
    for line in rawdata:
        date.append(str(line[0]))
        temp.append(str(line[1]))
#date
date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))
    #else:
        #date_dt.append(date[i])
len(date_dt)
#len(date)
temp_dt=[]

for i in range(len(date)):
    if i>=2 :
        if temp[i]=='':
            temp_dt.append(float(0.0))
        else:
            temp_dt.append(float(temp[i]))
    else:
        temp[i]=0.0
        #temp_dt.append(float(0.0))


# ## reading rest of data in a data-frame

# In[92]:

df_all = read_csv(r'C:\Users\alias\OneDrive for Business\Project\Detroit_Water_Aeration\second_data\aeration_one_sheet.csv', sep=',')
#print (df_all)
len(df_all['ref_date'])
df = df_all.ix[1:]
#df['PEAS1']
df.replace('<7', '7')
df_modif = df.replace(['ND', '<0.02', '<3', '<4', '<5', '<7', '<10', '<17', '<20', '#DIV/0!'], ['', '0.02', '3', '4', '5', '7', '10', '17', '20', ''])
len(df_modif['Deck 1 Flow'])
df_modif


# # Column names in the data-frame

# In[93]:

list(df_modif.columns.values)


# # changing string to float

# In[94]:

for col_name in list(df_modif.columns.values):
    if col_name != 'ref_date':
        df_modif[col_name] = pd.to_numeric(df_modif[col_name] , errors='ignore')


# # Filling the missing values

# ## replacing missing values with previous value

# In[33]:

#adding 2 series
ali=[]
for col_name in list(df_modif.columns.values):
    if col_name == 'PEAS1_OG':
        #print(col_name)
        for i in range(len(df_modif[col_name])+1):
            #print(i)
            
            if i>= 1:
                if df_modif[col_name][i] != '':
                    ali.append(float(df_modif[col_name][i]))
                else:
                    if i== 1:
                        ali.append(float(0.0))
                    else:
                        ali.append(float(df_modif[col_name][(i-1)]))

#df_modif['PEAS1_BOD-3']  
ali
#len(date_dt)
#len(ali)


# # ploting

# ## 1- input flow amount and charactristics

# In[6]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))
    #else:
        #date_dt.append(date[i])
print (len(date_dt))
print (len(temp_dt))
#plt.plot_date(date_dt, 0)
value=[]
for i in range(len(date_dt)):
    value.append(i)

fig=plt.figure()
ax1=plt.subplot2grid((2,2),(0,0))
ax2=plt.subplot2grid((2,2),(0,1))
ax3=plt.subplot2grid((2,2),(1,0))
ax4=plt.subplot2grid((2,2),(1,1))
ax1.scatter(date_dt, 4*df_modif['Influent Temp'], label='4*Influent Temp')
ax1.scatter(date_dt, df_modif['Deck 1 Flow'], label='Deck 1 Flow', color='#00ff00')
ax1.scatter(date_dt, df_modif['Deck 2 Flow'], label='Deck 2 Flow', color='#cd69c9')
ax1.scatter(date_dt, df_modif['Deck 3 Flow'], label='Deck 3 Flow', color='#ff8000')
ax1.scatter(date_dt, df_modif['Deck 4 Flow'], label='Deck 4 Flow', color='#417dd4')
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(30)
ax1.legend()
ax2.scatter(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax2.scatter(date_dt, df_modif['PEAS1_BOD-3'], label='PEAS1_BOD-3', color='#00ff00')
ax2.scatter(date_dt, df_modif['PEAS1_COD'], label='PEAS1_COD', color='#cd69c9')
ax2.scatter(date_dt, df_modif['PEAS1_OG'], label='PEAS1_OG', color='#ff8000')
ax2.scatter(date_dt, df_modif['PEAS1_TSS'], label='PEAS1_TSS', color='#417dd4')
ax2.scatter(date_dt, df_modif['PEAS1_VSS'], label='PEAS1_VSS', color='#fb9b9c')
for label in ax2.xaxis.get_ticklabels():
    label.set_rotation(30)
ax2.legend()
ax3.scatter(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax3.scatter(date_dt, df_modif['PEAS3_BOD-3'], label='PEAS3_BOD-3', color='#00ff00')
ax3.scatter(date_dt, df_modif['PEAS3_COD'], label='PEAS3_COD', color='#cd69c9')
ax3.scatter(date_dt, df_modif['PEAS3_OG'], label='PEAS3_OG', color='#ff8000')
ax3.scatter(date_dt, df_modif['PEAS3_TSS'], label='PEAS3_TSS', color='#417dd4')
ax3.scatter(date_dt, df_modif['PEAS3_VSS'], label='PEAS3_VSS', color='#fb9b9c')
for label in ax3.xaxis.get_ticklabels():
    label.set_rotation(30)
ax3.legend()
ax4.scatter(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax4.scatter(date_dt, df_modif['PEAS4_BOD-3'], label='PEAS4_BOD-3', color='#00ff00')
ax4.scatter(date_dt, df_modif['PEAS4_COD'], label='PEAS4_COD', color='#cd69c9')
ax4.scatter(date_dt, df_modif['PEAS4_OG'], label='PEAS4_OG', color='#ff8000')
ax4.scatter(date_dt, df_modif['PEAS4_TSS'], label='PEAS4_TSS', color='#417dd4')
ax4.scatter(date_dt, df_modif['PEAS4_VSS'], label='PEAS4_VSS', color='#fb9b9c')
for label in ax4.xaxis.get_ticklabels():
    label.set_rotation(30)
ax4.legend()
#ax1.title('scatter\nplot')
#ax1.xlabel('time')
#ax1.ylabel('y')
plt.legend()
plt.show()


# ## 2- input characteristics  comparison

# In[7]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))
    #else:
        #date_dt.append(date[i])
print (len(date_dt))
print (len(temp_dt))
#plt.plot_date(date_dt, 0)
value=[]
for i in range(len(date_dt)):
    value.append(i)
fig=plt.figure()
ax1=plt.subplot2grid((1, 4),(0,0))
ax2=plt.subplot2grid((1, 4),(0,1))
ax3=plt.subplot2grid((1, 4),(0,2))
ax4=plt.subplot2grid((1, 4),(0,3))
ax1.scatter(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax1.scatter(date_dt, df_modif['PEAS1_BOD-3'], label='PEAS1_BOD-3', color='#00ff00')
ax1.scatter(date_dt, df_modif['PEAS3_BOD-3'], label='PEAS3_BOD-3', color='#cd69c9')
ax1.scatter(date_dt, df_modif['PEAS4_BOD-3'], label='PEAS4_BOD-3', color='#ff8000')
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(30)
ax1.legend()
ax2.scatter(date_dt, .25*df_modif['Influent Temp'], label='Influent Temp')
ax2.scatter(date_dt, df_modif['PEAS1_OG'], label='PEAS1_OG', color='#00ff00')
ax2.scatter(date_dt, df_modif['PEAS3_OG'], label='PEAS3_OG', color='#cd69c9')
ax2.scatter(date_dt, df_modif['PEAS4_OG'], label='PEAS4_OG', color='#ff8000')
for label in ax2.xaxis.get_ticklabels():
    label.set_rotation(30)
ax2.legend()
ax3.scatter(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax3.scatter(date_dt, df_modif['PEAS1_TSS'], label='PEAS1_TSS', color='#00ff00')
ax3.scatter(date_dt, df_modif['PEAS3_TSS'], label='PEAS3_TSS', color='#cd69c9')
ax3.scatter(date_dt, df_modif['PEAS4_TSS'], label='PEAS4_TSS', color='#ff8000')
for label in ax3.xaxis.get_ticklabels():
    label.set_rotation(30)
ax3.legend()
ax4.scatter(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax4.scatter(date_dt, df_modif['PEAS1_VSS'], label='PEAS1_VSS', color='#00ff00')
ax4.scatter(date_dt, df_modif['PEAS3_VSS'], label='PEAS3_VSS', color='#cd69c9')
ax4.scatter(date_dt, df_modif['PEAS4_VSS'], label='PEAS4_VSS', color='#ff8000')
for label in ax4.xaxis.get_ticklabels():
    label.set_rotation(30)
ax4.legend()
#ax1.title('scatter\nplot')
#ax1.xlabel('time')
#ax1.ylabel('y')
plt.legend()
plt.show()


# ## 3- total influent plutants

# In[8]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))
    #else:
        #date_dt.append(date[i])
print (len(date_dt))
print (len(temp_dt))
#plt.plot_date(date_dt, 0)
value=[]
for i in range(len(date_dt)):
    value.append(i)
fig=plt.figure()
ax1=plt.subplot2grid((1, 1),(0,0))
ax1.scatter(date_dt, 10*df_modif['Influent Temp'], label='10*Influent Temp')
ax1.scatter(date_dt, 500*df_modif['Combined TP'], label='500*Combined TP', color='#00ff00')
ax1.scatter(date_dt, df_modif['Secondary Eff Flow (inc. SFE + Buffer)'], label='Secondary Eff Flow (inc. SFE + Buffer)', color='#cd69c9')
ax1.scatter(date_dt, map(operator.add, map(operator.add, df_modif['Deck 1 Flow'],  df_modif['Deck 2 Flow']),map(operator.add, df_modif['Deck 3 Flow'],  df_modif['Deck 4 Flow'])), label='Deck 1+2+3+4 Flow', color='#ff8000')
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(30)
ax1.legend()
#ax1.title('scatter\nplot')
#ax1.xlabel('time')
#ax1.ylabel('y')
plt.legend()
plt.show()


# ## 4- process specification vs. time

# In[15]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))
    #else:
        #date_dt.append(date[i])
#print (len(date_dt))
#print (len(temp_dt))
#plt.plot_date(date_dt, 0)
value=[]
for i in range(len(date_dt)):
    value.append(i)
fig=plt.figure()
ax1=plt.subplot2grid((1, 2),(0,0))
ax2=plt.subplot2grid((1, 2),(0,1))


ax1.scatter(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax1.scatter(date_dt, df_modif['C2E3_BOD-3'], label='C2E3_BOD-3', color='#00ff00')
ax1.scatter(date_dt, df_modif['C2E3_NH3'], label='C2E3_NH3', color='#cd69c9')
ax1.scatter(date_dt, df_modif['C2E3_OG'], label='C2E3_OG', color='#ff8000')
ax1.scatter(date_dt, df_modif['C2E3_SP'], label='C2E3_SP', color='#417dd4')
ax1.scatter(date_dt, df_modif['C2E3_TP'], label='C2E3_TP', color='#fb9b9c')
ax1.scatter(date_dt, df_modif['C2E3_TSS'], label='C2E3_TSS', color='#84f9ef')
#ax1.scatter(date_dt, df_modif['C2E3_TS'], label='C2E3_TS', color='#fff400')
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(30)
ax1.legend()

ax2.scatter(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax2.scatter(date_dt, df_modif['C2E4_BOD-3'], label='C2E4_BOD-3', color='#00ff00')
ax2.scatter(date_dt, df_modif['C2E4_NH3'], label='C2E4_NH3', color='#cd69c9')
ax2.scatter(date_dt, df_modif['C2E4_OG'], label='C2E4_OG', color='#ff8000')
ax2.scatter(date_dt, df_modif['C2E4_SP'], label='C2E4_SP', color='#417dd4')
ax2.scatter(date_dt, df_modif['C2E4_TP'], label='C2E4_TP', color='#fb9b9c')
ax2.scatter(date_dt, df_modif['C2E4_TSS'], label='C2E4_TSS', color='#84f9ef')
#ax2.scatter(date_dt, df_modif['C2E4_TS'], label='C2E4_TS', color='#fff400')
for label in ax2.xaxis.get_ticklabels():
    label.set_rotation(30)
ax2.legend()

#ax1.title('scatter\nplot')
#ax1.xlabel('time')
#ax1.ylabel('y')
plt.legend()
plt.show()


# ## 5- process specification in diffrent tanks

# In[29]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))

fig=plt.figure()
ax1=plt.subplot2grid((1, 1),(0,0))
#ax2=plt.subplot2grid((1, 1),(0,0))
#ax3=plt.subplot2grid((1, 1),(0,0))
#ax4=plt.subplot2grid((1, 1),(0,0))
#ax5=plt.subplot2grid((1, 1),(0,0))
#ax6=plt.subplot2grid((1, 1),(0,0))

#ax1.plot(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax1.plot(date_dt, df_modif['C2E3_BOD-3'], label='C2E3_BOD-3', color='#00ff00')
ax1.plot(date_dt, df_modif['C2E4_BOD-3'], label='C2E4_BOD-3', color='#cd69c9')
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(30)
ax1.legend()

#ax2.plot(date_dt, df_modif['C2E3_NH3'], label='C2E3_NH3', color='#00ff00')
#ax2.plot(date_dt, df_modif['C2E4_NH3'], label='C2E4_NH3', color='#cd69c9')
#for label in ax2.xaxis.get_ticklabels():
    #label.set_rotation(30)
#ax2.legend()

#ax3.plot(date_dt, df_modif['C2E3_OG'], label='C2E3_OG', color='#00ff00')
#ax3.plot(date_dt, df_modif['C2E4_OG'], label='C2E4_OG', color='#cd69c9')
#for label in ax3.xaxis.get_ticklabels():
    #label.set_rotation(30)
#ax3.legend()

#ax4.plot(date_dt, df_modif['C2E3_SP'], label='C2E3_SP', color='#00ff00')
#ax4.plot(date_dt, df_modif['C2E4_SP'], label='C2E4_SP', color='#cd69c9')
#for label in ax4.xaxis.get_ticklabels():
    #label.set_rotation(30)
#ax4.legend()

#ax5.plot(date_dt, df_modif['C2E3_TP'], label='C2E3_TP', color='#00ff00')
#ax5.plot(date_dt, df_modif['C2E4_TP'], label='C2E4_TP', color='#cd69c9')
#for label in ax5.xaxis.get_ticklabels():
    #label.set_rotation(30)
#ax5.legend()

#ax6.plot(date_dt, df_modif['C2E3_TSS'], label='C2E3_TSS', color='#00ff00')
#ax6.plot(date_dt, df_modif['C2E4_TSS'], label='C2E4_TSS', color='#cd69c9')
#for label in ax6.xaxis.get_ticklabels():
    #label.set_rotation(30)
#ax6.legend()

#ax1.scatter(date_dt, df_modif['C2E3_TS'], label='C2E3_TS', color='#fff400')
#ax1.scatter(date_dt, df_modif['C2E4_TS'], label='C2E3_TS', color='#cd69c9')
#for label in ax1.xaxis.get_ticklabels():
    #label.set_rotation(30)
#ax1.legend()


plt.legend()
plt.show()


# ## 6- recycle - buffer VS. time

# In[33]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))


fig=plt.figure()
ax1=plt.subplot2grid((1, 1),(0,0))

ax1.scatter(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax1.scatter(date_dt, df_modif['Recycle'], label='Recycle', color='#00ff00')
ax1.scatter(date_dt, df_modif['Buffer'], label='Buffer', color='#cd69c9')

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(30)
ax1.legend()

plt.legend()
plt.show()


# ## 7- Aeration parameters

# In[47]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))
    #else:
        #date_dt.append(date[i])


fig=plt.figure()
ax1=plt.subplot2grid((2,2),(0,0))
ax2=plt.subplot2grid((2,2),(0,1))
ax3=plt.subplot2grid((2,2),(1,0))
ax4=plt.subplot2grid((2,2),(1,1))
ax1.scatter(date_dt, df_modif['RAS-1 Flow'], label='RAS-1 Flow')
#ax1.scatter(date_dt, df_modif['RAS-1_TSS'], label='RAS-1_TSS', color='#00ff00')
#ax1.scatter(date_dt, df_modif['MLSS-1'], label='MLSS-1', color='#cd69c9')
#ax1.scatter(date_dt, df_modif['MLVSS-1'], label='MLVSS-1', color='#ff8000')
ax1.scatter(date_dt, df_modif['SVI-1'], label='SVI-1', color='#417dd4')
ax1.scatter(date_dt, df_modif['Deck 1 Temp'], label='Deck 1 Temp', color='#fb9b9c')
ax1.scatter(date_dt, df_modif['LBDO - 1'], label='LBDO - 1', color='#84f9ef')
ax1.scatter(date_dt, df_modif['O2 flow - 1'], label='O2 flow - 1', color='#fff400')
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(30)
ax1.legend()
ax2.scatter(date_dt, df_modif['RAS-2 Flow'], label='RAS-2 Flow')
#ax2.scatter(date_dt, df_modif['RAS-2_TSS'], label='RAS-2_TSS', color='#00ff00')
#ax2.scatter(date_dt, df_modif['MLSS-2'], label='MLSS-2', color='#cd69c9')
#ax2.scatter(date_dt, df_modif['MLVSS-2'], label='MLVSS-2', color='#ff8000')
ax2.scatter(date_dt, df_modif['SVI-2'], label='SVI-2', color='#417dd4')
ax2.scatter(date_dt, df_modif['Deck 2 Temp'], label='Deck 2 Temp', color='#fb9b9c')
ax2.scatter(date_dt, df_modif['LBDO - 2'], label='LBDO - 2', color='#84f9ef')
ax2.scatter(date_dt, df_modif['O2 flow - 2'], label='O2 flow - 2', color='#fff400')
for label in ax2.xaxis.get_ticklabels():
    label.set_rotation(30)
ax2.legend()
ax3.scatter(date_dt, df_modif['RAS-3 Flow'], label='RAS-3 Flow')
#ax3.scatter(date_dt, df_modif['RAS-3_TSS'], label='RAS-3_TSS', color='#00ff00')
#ax3.scatter(date_dt, df_modif['MLSS-3'], label='MLSS-3', color='#cd69c9')
#ax3.scatter(date_dt, df_modif['MLVSS-3'], label='MLVSS-3', color='#ff8000')
ax3.scatter(date_dt, df_modif['SVI-3'], label='SVI-3', color='#417dd4')
ax3.scatter(date_dt, df_modif['Deck 3 Temp'], label='Deck 3 Temp', color='#fb9b9c')
ax3.scatter(date_dt, df_modif['LBDO - 3'], label='LBDO - 3', color='#84f9ef')
ax3.scatter(date_dt, df_modif['O2 flow - 3'], label='O2 flow - 3', color='#fff400')
for label in ax3.xaxis.get_ticklabels():
    label.set_rotation(30)
ax3.legend()
ax4.scatter(date_dt, df_modif['RAS-4 Flow'], label='RAS-4 Flow')
#ax4.scatter(date_dt, df_modif['RAS-4_TSS'], label='RAS-4_TSS', color='#00ff00')
#ax4.scatter(date_dt, df_modif['MLSS-4'], label='MLSS-4', color='#cd69c9')
#ax4.scatter(date_dt, df_modif['MLVSS-4'], label='MLVSS-4', color='#ff8000')
ax4.scatter(date_dt, df_modif['SVI-4'], label='SVI-4', color='#417dd4')
ax4.scatter(date_dt, df_modif['Deck 4 Temp'], label='Deck 4 Temp', color='#fb9b9c')
ax4.scatter(date_dt, df_modif['LBDO - 4'], label='LBDO - 4', color='#84f9ef')
ax4.scatter(date_dt, df_modif['O2 flow - 4'], label='O2 flow - 4', color='#fff400')
for label in ax4.xaxis.get_ticklabels():
    label.set_rotation(30)
ax4.legend()
#ax1.title('scatter\nplot')
#ax1.xlabel('time')
#ax1.ylabel('y')
plt.legend()
plt.show()


# ## 8- Aeration process in diffrent tanks

# #### Flow

# In[52]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))

fig=plt.figure()
ax1=plt.subplot2grid((1, 1),(0,0))

ax1.plot(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax1.plot(date_dt, df_modif['RAS-1 Flow'], label='RAS-1 Flow', color='#00ff00')
ax1.plot(date_dt, df_modif['RAS-2 Flow'], label='RAS-2 Flow', color='#cd69c9')
ax1.plot(date_dt, df_modif['RAS-3 Flow'], label='RAS-3 Flow', color='#ff8000')
ax1.plot(date_dt, df_modif['RAS-4 Flow'], label='RAS-4 Flow', color='#417dd4')
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(30)
ax1.legend()

plt.legend()
plt.show()


# #### TSS

# In[ ]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))

fig=plt.figure()
ax2=plt.subplot2grid((1, 1),(0,0))

ax2.plot(date_dt, df_modif['RAS-1_TSS'], label='RAS-1_TSS', color='#00ff00')
ax2.plot(date_dt, df_modif['RAS-2_TSS'], label='RAS-2_TSS', color='#cd69c9')
ax2.plot(date_dt, df_modif['RAS-3_TSS'], label='RAS-3_TSS', color='#ff8000')
ax2.plot(date_dt, df_modif['RAS-4_TSS'], label='RAS-4_TSS', color='#417dd4')
for label in ax2.xaxis.get_ticklabels():
    label.set_rotation(30)
ax2.legend()

plt.legend()
plt.show()


# #### MLSS

# In[ ]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))

fig=plt.figure()
ax3=plt.subplot2grid((1, 1),(0,0))

ax3.plot(date_dt, df_modif['MLSS-1'], label='MLSS-1', color='#00ff00')
ax3.plot(date_dt, df_modif['MLSS-2'], label='MLSS-2', color='#cd69c9')
ax3.plot(date_dt, df_modif['MLSS-3'], label='MLSS-3', color='#ff8000')
ax3.plot(date_dt, df_modif['MLSS-4'], label='MLSS-4', color='#417dd4')
for label in ax3.xaxis.get_ticklabels():
    label.set_rotation(30)
ax3.legend()

plt.legend()
plt.show()


# #### MLVSS

# In[ ]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))

fig=plt.figure()
ax4=plt.subplot2grid((1, 1),(0,0))

ax4.plot(date_dt, df_modif['MLVSS-1'], label='MLVSS-1', color='#00ff00')
ax4.plot(date_dt, df_modif['MLVSS-2'], label='MLVSS-2', color='#cd69c9')
ax4.plot(date_dt, df_modif['MLVSS-3'], label='MLVSS-3', color='#ff8000')
ax4.plot(date_dt, df_modif['MLVSS-4'], label='MLVSS-4', color='#417dd4')
for label in ax4.xaxis.get_ticklabels():
    label.set_rotation(30)
ax4.legend()

plt.legend()
plt.show()


# #### SVI

# In[53]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))

fig=plt.figure()
ax5=plt.subplot2grid((1, 1),(0,0))

ax5.plot(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax5.plot(date_dt, df_modif['SVI-1'], label='SVI-1', color='#00ff00')
ax5.plot(date_dt, df_modif['SVI-2'], label='SVI-2', color='#cd69c9')
ax5.plot(date_dt, df_modif['SVI-3'], label='SVI-3', color='#ff8000')
ax5.plot(date_dt, df_modif['SVI-4'], label='SVI-4', color='#417dd4')
for label in ax5.xaxis.get_ticklabels():
    label.set_rotation(30)
ax5.legend()

plt.legend()
plt.show()


# #### TEMP

# In[54]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))

fig=plt.figure()
ax6=plt.subplot2grid((1, 1),(0,0))

ax6.plot(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax6.plot(date_dt, df_modif['Deck 1 Temp'], label='Deck 1 Temp', color='#00ff00')
ax6.plot(date_dt, df_modif['Deck 2 Temp'], label='Deck 2 Temp', color='#cd69c9')
ax6.plot(date_dt, df_modif['Deck 3 Temp'], label='Deck 3 Temp', color='#ff8000')
ax6.plot(date_dt, df_modif['Deck 4 Temp'], label='Deck 4 Temp', color='#417dd4')
for label in ax6.xaxis.get_ticklabels():
    label.set_rotation(30)
ax6.legend()

plt.legend()
plt.show()


# #### LBDO

# In[57]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))

fig=plt.figure()
ax7=plt.subplot2grid((1, 1),(0,0))

#ax7.plot(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax7.plot(date_dt, df_modif['LBDO - 1'], label='LBDO - 1', color='#fff400')
ax7.plot(date_dt, df_modif['LBDO - 2'], label='LBDO - 2', color='#cd69c9')
ax7.plot(date_dt, df_modif['LBDO - 3'], label='LBDO - 3', color='#ff8000')
ax7.plot(date_dt, df_modif['LBDO - 4'], label='LBDO - 4', color='#417dd4')
for label in ax7.xaxis.get_ticklabels():
    label.set_rotation(30)
ax7.legend()

plt.legend()
plt.show()


# #### O2 flow

# In[60]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))

fig=plt.figure()
ax8=plt.subplot2grid((1, 1),(0,0))

ax8.plot(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax8.scatter(date_dt, df_modif['O2 flow - 1'], label='O2 flow - 1', color='#fff400')
ax8.scatter(date_dt, df_modif['O2 flow - 2'], label='O2 flow - 2', color='#cd69c9')
ax8.scatter(date_dt, df_modif['O2 flow - 3'], label='O2 flow - 3', color='#ff8000')
ax8.scatter(date_dt, df_modif['O2 flow - 4'], label='O2 flow - 4', color='#417dd4')
for label in ax8.xaxis.get_ticklabels():
    label.set_rotation(30)
ax8.legend()

plt.legend()
plt.show()


# #### Pressure

# In[63]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))

fig=plt.figure()
ax9=plt.subplot2grid((1, 1),(0,0))

#ax9.plot(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax9.plot(date_dt, df_modif['Pressure - 1'], label='Pressure - 1', color='#fff400')
ax9.plot(date_dt, df_modif['Pressure - 2'], label='Pressure - 2', color='#cd69c9')
ax9.plot(date_dt, df_modif['Pressure - 3'], label='Pressure - 3', color='#ff8000')
ax9.plot(date_dt, df_modif['Pressure - 4'], label='Pressure - 4', color='#417dd4')
for label in ax9.xaxis.get_ticklabels():
    label.set_rotation(30)
ax9.legend()

plt.legend()
plt.show()


# #### Vent %

# In[64]:

date_dt=[]
for i in range(len(date)):
    if i>=2 :
        date_dt.append(dt.datetime.strptime(date[i], '%m/%d/%Y'))

fig=plt.figure()
ax10=plt.subplot2grid((1, 1),(0,0))

ax10.plot(date_dt, df_modif['Influent Temp'], label='Influent Temp')
ax10.scatter(date_dt, df_modif['Vent % - 1'], label='Vent % - 1', color='#fff400')
ax10.scatter(date_dt, df_modif['Vent % - 2'], label='Vent % - 2', color='#cd69c9')
ax10.scatter(date_dt, df_modif['Vent % - 3'], label='Vent % - 3', color='#ff8000')
ax10.scatter(date_dt, df_modif['Vent % - 4'], label='Vent % - 4', color='#417dd4')
for label in ax10.xaxis.get_ticklabels():
    label.set_rotation(30)
ax10.legend()

plt.legend()
plt.show()


# In[74]:

df_modif['RAS-1_TSS']


# In[114]:

import re

re.sub('[^\d\.]', '', df_modif['RAS-1_TSS'])
#s = s.replace(',', '')


# In[ ]:




# In[ ]:



