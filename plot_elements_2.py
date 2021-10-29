import numpy as np
import pandas as pd
import seaborn as sns
import seaborn_image as isns
import matplotlib.pyplot as plt
from matplotlib import rc,rcParams

df = pd.read_csv('data_metales.csv').replace("SiO2",'SiO$_2$')

fig,ax = plt.subplots(figsize=(20,6))

labels = ['0','0','0.01', '1', '100','10000']

elemento = df['elemento']
concentracion = df['concentracion']

isns.set_context(mode='paper', fontfamily='sans-serif', fontweight='bold', rc=None)
sns.set(style="ticks", font_scale=2)

rc('font', weight='bold')


def colors_from_values(values, palette_name):
    # normalize the values to range [0, 1]
    normalized = (values - min(values)) / (max(values) - min(values))
    # convert to indices
    indices = np.round(normalized * (len(values) - 1)).astype(np.int32)
    # use the indices to get the colors
    palette = sns.color_palette(palette_name, len(values))
    return np.array(palette).take(indices, axis=0)

g = sns.barplot(elemento, concentracion, alpha=1, data=df, 
            order=df.sort_values('concentracion',ascending = False).elemento,
               palette="OrRd_r")

g.set_yscale("log")
#g.axhline(1, color='red')
ax.set_ylabel('Quantity (ppm)', fontsize=24)
ax.set_xlabel('Element', fontsize=24)
plt.xticks(fontsize=18)
plt.yticks(fontsize=14)
plt.ylim(0.001,np.exp(10))

#ax.set_xticklabels(labels)
plt.xlim(-1,32)
for bar in g.patches:
    g.annotate(format(bar.get_height(), '.2f'),
               (bar.get_x() + bar.get_width() / 2,
                bar.get_height()+ 6.1*bar.get_height()), ha='center', va='center',
               size=17, xytext=(0, 8), textcoords='offset points',
              rotation=90)
sns.despine()
fig.tight_layout()
fig.savefig("elements.png", format='png', dpi=800, transparent=True)
plt.show()
