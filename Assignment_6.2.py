# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 20:13:24 2018

@author: vamshi
"""

import pandas as pd
import matplotlib.pyplot as plt
url=r'https://raw.githubusercontent.com/Geoyi/Cleaning-Titanic-Data/master/titanic_original.csv'
titanic = pd.read_csv(url,skip_blank_lines=True)

'''1. Create a pie chart presenting the male/female proportion'''

count=titanic['sex'].value_counts()
colors = ['blue', 'orange']
f, (ax1, ax2) = plt.subplots(1, 2)
ax1.pie(count.values.tolist(), labels=count.index.values.tolist(), colors=colors,startangle=90,
        autopct='%.1f%%')
ax1.set_title('Male/Female proportion')

'''2. Create a scatterplot with the Fare paid and the Age, 
differ the plot color by gender'''

colors = {'male':'blue', 'female':'orange'}
ax2.scatter(titanic.fare,titanic.age,c=titanic['sex'].iloc[:-1].apply(lambda x: 
    colors[x]))
ax2.set_xlabel('Fare')
ax2.set_ylabel('Age')
ax2.set_title('Fare paid and the Age')