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

plt.plot(xnew, yc_smooth,label='HM')
plt.scatter(x, yc,)
plt.plot(xnew, y1_smooth, label='10 mL/L')
plt.scatter(x,y1)
plt.plot(xnew, y2_smooth, label='20 mL/L')
plt.scatter(x,y2)
plt.plot(xnew, y3_smooth, label='30 mL/L')
plt.scatter(x,y3)

plt.xlabel('Days', fontsize=12)
plt.ylabel('Population density (x10$^4$ cells/mL)', fontsize=12)
plt.legend(fancybox=True, framealpha=0)

plt.savefig('growth.png', dpi=800)
