#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


# In[206]:


NHL = pd.read_excel('Desktop/Python/NHL_Attendance.xlsx', index_col=None, header=0)
NHL.head()


# In[210]:


NHL.shape


# In[212]:


NHL.columns = NHL.columns.str.upper().str.replace(' ','_')
NHL.head()


# In[213]:


fig, ax = plt.subplots()
ax.scatter(NHL['HOME_ATTENDANCE'], NHL['ROAD_ATTENDANCE'])


# In[214]:


NHL.groupby('TEAM').mean().sort_values('RANK',ascending=False)[:10].plot.bar()


# In[215]:


import matplotlib.pyplot as plt
import seaborn as sns 

color_order = ['xkcd:cerulean', 'xkcd:ocean',
                'xkcd:black','xkcd:royal purple',
                'xkcd:royal purple', 'xkcd:navy blue',
                'xkcd:powder blue', 'xkcd:light maroon', 
                'xkcd:lightish blue','xkcd:navy']

data = sns.barplot(x=NHL['TEAM'][:15],
            y=NHL['TOTAL_ATTENDANCE'],
            palette=color_order).set_title('Total Attendence x Top 10 Teams')

plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='medium'  
)


# In[216]:


N = 5
HomeAttendance = (NHL['HOME_ATTENDANCE'][0], NHL['HOME_ATTENDANCE'][1], NHL['HOME_ATTENDANCE'][2], NHL['HOME_ATTENDANCE'][3], NHL['HOME_ATTENDANCE'][4])
AwayAttendance = (NHL['ROAD_ATTENDANCE'][0], NHL['ROAD_ATTENDANCE'][1], NHL['ROAD_ATTENDANCE'][2], NHL['ROAD_ATTENDANCE'][3], NHL['ROAD_ATTENDANCE'][4])
ind = np.arange(N)    
width = 0.35       

p1 = plt.bar(ind, HomeAttendance, width, yerr=HomeAttendance)
p2 = plt.bar(ind, AwayAttendance, width,
             bottom=HomeAttendance, yerr=AwayAttendance)

plt.ylabel('Total Attendence')
plt.title('Total Attenence x  Home & Away')
plt.xticks(ind, (NHL['TEAM'][0], NHL['TEAM'][1], NHL['TEAM'][2], NHL['TEAM'][3], NHL['TEAM'][4]))
plt.yticks(np.arange(100000, 2000000, 250000))
plt.legend((p1[0], p2[0]), ('Home', 'Away'))

plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='medium'  
)

plt.show()


# In[ ]:




