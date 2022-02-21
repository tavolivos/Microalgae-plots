import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.patches import Circle
from matplotlib_scalebar.scalebar import ScaleBar
import pandas as pd
%matplotlib inline

font = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 9}
plt.rc('font', **font)

fig = plt.figure()

# load dataset
df = pd.read_csv("pe_control.csv")

#control
ax1 = plt.subplot2grid((10,4), (0,0), rowspan=2, colspan=2)

x=df['dia']
y1=df['1c']
y2=df['2c']
y3=df['4c']
y4=df['8c']

ax1.bar(x,y1, label='1-cell')
ax1.bar(x, y2 ,bottom=y1,label='2-cells')
ax1.bar(x, y3 ,bottom=y1+y2,label='4-cells')
ax1.bar(x, y4 ,bottom=y1+y2+y3,label='8-cells')
ax1.set_xlim()
ax1.set_ylim(0,100)
ax1.set_xlabel('Days', weight='bold')
ax1.set_ylabel('%', weight='bold')
ax1.set_xticks(x)
ax1.axes.get_xaxis().set_visible(False)
ax1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.6), ncol=2, frameon=False)

#treatment 1
ax2 = plt.subplot2grid((10,4), (2,0), rowspan=2, colspan=2)

df = pd.read_csv("pe_treatment1.csv")

x=df['dia']
y1=df['1c']
y2=df['2c']
y3=df['4c']
y4=df['8c']

ax2.bar(x,y1)
ax2.bar(x, y2 ,bottom=y1,label='y2')
ax2.bar(x, y3 ,bottom=y1+y2,label='y3')
ax2.bar(x, y4 ,bottom=y1+y2+y3,label='y4')
ax2.set_xlim()
ax2.set_ylim(0,100)
ax2.set_xlabel('Days', weight='bold')
ax2.set_ylabel('%', weight='bold')
ax2.set_xticks(x)
ax2.axes.get_xaxis().set_visible(False)

#treatment 2
ax3 = plt.subplot2grid((10,4), (4,0), rowspan=2, colspan=2)

df = pd.read_csv("pe_treatment2.csv")

x=df['dia']
y1=df['1c']
y2=df['2c']
y3=df['4c']
y4=df['8c']

ax3.bar(x,y1)
ax3.bar(x, y2 ,bottom=y1,label='y2')
ax3.bar(x, y3 ,bottom=y1+y2,label='y3')
ax3.bar(x, y4 ,bottom=y1+y2+y3,label='y4')
ax3.set_xlim()
ax3.set_ylim(0,100)
ax3.set_xlabel('Days', weight='bold')
ax3.set_ylabel('%', weight='bold')
ax3.set_xticks(x)
ax3.axes.get_xaxis().set_visible(False)

#treatment 3
ax4 = plt.subplot2grid((10,4), (6,0), rowspan=2, colspan=2)

df = pd.read_csv("pe_treatment3.csv")

x=df['dia']
y1=df['1c']
y2=df['2c']
y3=df['4c']
y4=df['8c']

ax4.bar(x,y1)
ax4.bar(x, y2 ,bottom=y1,label='y2')
ax4.bar(x, y3 ,bottom=y1+y2,label='y3')
ax4.bar(x, y4 ,bottom=y1+y2+y3,label='y4')
ax4.set_xlim()
ax4.set_ylim(0,100)
ax4.set_xlabel('Days', weight='bold')
ax4.set_ylabel('%', weight='bold')
ax4.set_xticks(x)
ax4.axes.get_xaxis().set_visible(False)

#treatment 4
ax5 = plt.subplot2grid((10,4), (8,0), rowspan=2, colspan=2)

df = pd.read_csv("pe_treatment4.csv")

x=df['dia']
y1=df['1c']
y2=df['2c']
y3=df['4c']
y4=df['8c']

ax5.bar(x,y1,)
ax5.bar(x, y2 ,bottom=y1,label='y2')
ax5.bar(x, y3 ,bottom=y1+y2,label='y3')
ax5.bar(x, y4 ,bottom=y1+y2+y3,label='y4')
ax5.set_xlim()
ax5.set_ylim(0,100)
ax5.set_xlabel('Days', weight='bold')
ax5.set_ylabel('%', weight='bold')
ax5.set_xticks(x)

# Supplot

ax6 = plt.subplot2grid((10,4), (0,2),rowspan=5, colspan=2)  
img1=mpimg.imread('/home/zapata/Desktop/lodo/8cenobios-modified.png')
imgplot = ax6.imshow(img1)
ax6.axis('off')

scalebar1 = ScaleBar(0.50, 'um', box_alpha=0,location='lower center')
ax6.add_artist(scalebar1)

ax7 = plt.subplot2grid((10,4), (5,2),rowspan=5, colspan=2)
img2=mpimg.imread('/home/zapata/Desktop/lodo/1cenobio-modified.png')
imgplot = ax7.imshow(img2)
ax7.axis('off')

scalebar2 = ScaleBar(0.50, 'um', box_alpha=0,location='lower center')
ax7.add_artist(scalebar2)


axes = fig.get_axes()
texts = ['A', 'B', 'C', 'D', 'E']
texts2 = ['','','','','','F', 'G']
for a,l in zip(axes, texts):
    a.annotate(l, xy=(-0.25, 1.1), xycoords="axes fraction", fontsize=10, weight = 'bold')
for a,l in zip(axes, texts2):
    a.annotate(l, xy=(0.12,1.05), xycoords="axes fraction", fontsize=10, weight = 'bold')



#fig.tight_layout()
fig.set_size_inches(6,6)

plt.subplots_adjust(hspace= 0.3)
plt.subplots_adjust(wspace= 0.1)
fig.savefig("pe3.png", dpi=800)
plt.show()
