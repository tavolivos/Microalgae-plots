import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 9}
plt.rc('font', **font)

fig,ax = plt.subplots(figsize=(5,2.5))
fig.subplots_adjust(bottom=0.15, left=0.15)


## the data
N = 5
menMeans = [17.19, 59.42, 33.01, 29.25, 25.66]
menStd =   [3.97, 6.16, 1.37, 1.83, 3.42]

## necessary variables
ind = np.arange(N)                # the x locations for the groups
width = 0.5                    # the width of the bars

## the bars
rects2 = ax.bar(ind+width, menMeans, width,
                    color='#fcff42',
                    yerr=menStd,
                    error_kw=dict(elinewidth=1,ecolor='black'),capsize=3)

# axes and labels
ax.set_xlim(-width,len(ind)+width)
ax.set_ylim(0,100)
ax.set_ylabel('Lipid content (%)', fontweight='bold')
ax.set_xlabel('Treatment', fontweight='bold', fontsize=9)

xTickMarks = ["HM", "20%", "40%", "60%", "80%"]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=0, fontsize=9)

#statistics labels
n = [0.5,1.5,2.5,3.5,4.5]
m = [22,66,35,32,30]

labels = ['a','b','c','c','c']
for i in range(len(labels)):
    plt.annotate(str(labels[i]), xy=(n[i],m[i]), ha='center', va='bottom')

plt.show()
fig.savefig("lipid3.png", format='png', dpi=850, transparent=True)
