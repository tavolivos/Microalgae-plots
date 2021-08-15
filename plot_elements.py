###################################
#  By: Gustavo E. Olivos-Ramirez  #
#      gustavo.olivos@upch.pe     #
#      Lima-Peru                  #
###################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv('data_metales.csv').replace("SiO2",'SiO$_2$')

fig,ax = plt.subplots(figsize=(15,5))

labels = ['0','0','0.01', '1', '100','10000']

elemento = df['elemento']
concentracion = df['concentracion']

#sns.set(style="white")
g = sns.barplot(elemento, concentracion, alpha=1, data=df,
            order=df.sort_values('concentracion',ascending = False).elemento)
g.set_yscale("log")
#g.axhline(1, color='red')
ax.set_ylabel('Quantity (ppm)', fontsize=14)
ax.set_xlabel('Element', fontsize=14)
plt.ylim(0,np.exp(10))

#ax.set_xticklabels(labels)
plt.xlim(-1,32)
for bar in g.patches:
    g.annotate(format(bar.get_height(), '.2f'),
               (bar.get_x() + bar.get_width() / 2,
                bar.get_height()+ 2.4*bar.get_height()), ha='center', va='center',
               size=12, xytext=(0, 8), textcoords='offset points',
              rotation=90)
sns.despine()
fig.savefig("elements.png", format='png', dpi=800, transparent=True)
plt.show()

