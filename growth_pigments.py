###################################
#  By: Gustavo E. Olivos-Ramirez  #
#      gustavo.olivos@upch.pe     #
#      Lima-Peru                  #
###################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
%matplotlib inline

font = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 16}
plt.rc('font', **font)


fig, (ax1, ax2) = plt.subplots(1,2)
fig.subplots_adjust(bottom=0.15, left=0.15)

df = pd.read_csv('growth.csv')

x = df['dia']

yc = df['tc']
xnew = np.linspace(x.min(), x.max(), 300)
interc = interp1d(x, yc, kind='quadratic')
yc_smooth = interc(xnew)

y1 = df['t1']
xnew = np.linspace(x.min(), x.max(), 300)
inter1 = interp1d(x, y1, kind='quadratic')
y1_smooth = inter1(xnew)

y2 = df['t2']
xnew = np.linspace(x.min(), x.max(), 300)
inter2 = interp1d(x, y2, kind='quadratic')
y2_smooth = inter2(xnew)

y3 = df['t3']
xnew = np.linspace(x.min(), x.max(), 300)
inter3 = interp1d(x, y3, kind='quadratic')
y3_smooth = inter3(xnew)

y4 = df['t4']
xnew = np.linspace(x.min(), x.max(), 300)
inter4 = interp1d(x, y4, kind='quadratic')
y4_smooth = inter4(xnew)

ax1.plot(xnew, yc_smooth,label='HM')
ax1.scatter(x, yc)
ax1.plot(xnew, y1_smooth, label='20% AES')
ax1.scatter(x,y1)
ax1.plot(xnew, y2_smooth, label='40% AES')
ax1.scatter(x,y2)
ax1.plot(xnew, y3_smooth, label='60% AES')
ax1.scatter(x,y3)
ax1.plot(xnew, y4_smooth, label='80% AES')
ax1.scatter(x,y4)

ax1.set_xlabel('Days', weight='bold')
ax1.set_ylabel('Population density\n (x10$^4$ cells/mL)', weight='bold')
ax1.legend(fancybox=True, framealpha=0)
ax1.set_xticks(x)

#plt.savefig('growth.png', dpi=800)

x = ['0','1','2','3','4','5','6','7']
y = ['0','0','0','0','0','0','0','0']
ax2.scatter(x,y, label='HM',s=800, 
            color=['#97955a','#597460','#9dac95','#b1b82e','#7aa601','#275c02','#1b5902','#0e3105'])

x = ['0','1','2','3','4','5','6','7']
y = ['20','20','20','20','20','20','20','20']
ax2.scatter(x,y, label='HM',s=800, 
            color=['#c3b548','#bccc9e','#b6c189','#b1b403','#7fa101','#9ca800','#94a601','#92a400'])

x = ['0','1','2','3','4','5','6','7']
y = ['40','40','40','40','40','40','40','40']
ax2.scatter(x,y, label='HM',s=800, 
            color=['#876e0a','#baba64','#a6a552','#a8a30b','#7a9302','#567300','#4f7800','#467201'])

x = ['0','1','2','3','4','5','6','7']
y = ['60','60','60','60','60','60','60','60']
ax2.scatter(x,y, label='HM',s=800, 
            color=['#534005','#989744','#79712b','#998407','#6c7307','#3b5401','#274801','#1f4900'])


x = ['0','1','2','3','4','5','6','7']
y = ['80','80','80','80','80','80','80','80']
ax2.scatter(x,y, label='HM',s=800, 
            color=['#1d140b','#2b2002','#44370d','#513704','#665b19','#755e00','#626201','#464700'])

ax2.set_xlim(-0.5,7.5)
ax2.set_ylim(-0.5,4.5)
ax2.set_xlabel('Days', weight='bold')
ax2.set_ylabel('AES %', weight='bold')
#ax2.savefig('density.png', dpi=850)

fig.set_size_inches(12,5)
plt.show()
fig.savefig("growth.png", dpi=800)
