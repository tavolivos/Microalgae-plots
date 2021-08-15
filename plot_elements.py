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

fig,ax = plt.subplots(figsize=(20,6))

labels = ['0','0','0.01', '1', '100','10000']

elemento = df['elemento']
concentracion = df['concentracion']

isns.set_context(mode='paper', fontfamily='sans-serif', fontweight='bold', rc=None)
sns.set(style="dark", font_scale=2)

rc('font', weight='bold')

g = sns.barplot(elemento, concentracion, alpha=1, data=df, 
            order=df.sort_values('concentracion',ascending = False).elemento)
g.set_yscale("log")
#g.axhline(1, color='red')
ax.set_ylabel('Quantity (ppm)', fontsize=22)
ax.set_xlabel('Element', fontsize=22)
plt.xticks(fontsize=16)
plt.yticks(fontsize=12)
plt.ylim(0,np.exp(10))

#ax.set_xticklabels(labels)
plt.xlim(-1,32)
for bar in g.patches:
    g.annotate(format(bar.get_height(), '.2f'),
               (bar.get_x() + bar.get_width() / 2,
                bar.get_height()+ 6.1*bar.get_height()), ha='center', va='center',
               size=16, xytext=(0, 8), textcoords='offset points',
              rotation=90)
sns.despine()
fig.tight_layout()
fig.savefig("elements.png", format='png', dpi=800, transparent=True)
plt.show()
