###################################
#  By: Gustavo E. Olivos-Ramirez  #
#      gustavo.olivos@upch.pe     #
#      Lima-Peru                  #
###################################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.datasets import *
from scipy.stats import pearsonr

font = {'family' : 'DejaVu Sans',
        'weight' : 'bold',
        'size'   : 9}
plt.rc('font', **font)

fig = plt.figure()

data=input('Enter your data in csv: ')
df = pd.read_csv(data)

#Descriptive statistics
instance_count, attr_count = df.shape
descript=df.describe()

print("\nDescriptive statistics")
print(descript)

#Correlation
corr_matrix=df.corr(method='pearson')
pval = df.corr(method=lambda x, y: pearsonr(x, y)[1]) - np.eye(*corr_matrix.shape)
p = pval.applymap(lambda x: ''.join(['*' for t in [0.01,0.05,0.1] if x<=t]))
corelation = corr_matrix.round(2).astype(str) + p

print("\nCORRELATION TABLE")
print(corelation)

#Important correlations
attrs = corr_matrix.iloc[:-1,:-1] # all except target
# only important correlations and not auto-correlations
threshold = 0.6
# {('LSTAT', 'TAX'): 0.543993, ('INDUS', 'RAD'): 0.595129, ...
important_corrs = (attrs[abs(attrs) > threshold][attrs != 1.0]).unstack().dropna().to_dict()
#unique correlations
unique_important_corrs = pd.DataFrame(list(set([(tuple(sorted(key)), important_corrs[key])
    for key in important_corrs])), columns=['attribute pair', 'correlation'])
# sorted by absolute value
unique_important_corrs = unique_important_corrs.iloc[
    abs(unique_important_corrs['correlation']).argsort()[::-1]]

print("\nIMPORTANT CORRELATIONS")
print(unique_important_corrs)

mask = np.zeros_like(corr_matrix, dtype=np.bool)
mask[np.triu_indices_from(mask)]= True

f, ax = plt.subplots(figsize=(5,4))
f.subplots_adjust(bottom=0.2, left=0.25)

heatmap = sb.heatmap(corr_matrix,
                      #mask = mask,
                      square = True,
                      linewidths = .5,
                      cmap = 'coolwarm',
                      cbar_kws = dict(use_gridspec=False,location="right"),
                      vmin = -1,
                      vmax = 1,
                      annot = True,
                      annot_kws = {'size': 9})

#add the column names as labels
ax.set_yticklabels(corr_matrix.columns, rotation = 0)
ax.set_xticklabels(corr_matrix.columns)

sb.set_style({'xtick.bottom': True}, {'ytick.left': True})
#fig.set_size_inches(6,6)
plt.savefig("corr.png", format='png', dpi=300, transparent=True)
print("\n^Correlation graph has been generated^")
