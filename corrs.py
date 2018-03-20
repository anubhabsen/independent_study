import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pickle
import time

df = pd.read_csv('corrdata.csv')

print(df.iloc[0, 0])
df.drop(['Subject number:'], axis = 1, inplace = True)
print(df.columns.values)
fig = plt.figure()
corrmat = df.corr()
print(corrmat.values)
plt.matshow(corrmat, fig.number)

fig.savefig('rho.png')

pval = np.zeros([df.shape[1],df.shape[1]])
for i in range(df.shape[1]): # rows are the number of rows in the matrix.
    for j in range(df.shape[1]):
        JonI = pd.ols(y=df.icol(i), x=df.icol(j), intercept=True)
        pval[i,j] = JonI.f_stat['p-value']

print(type(pval))
print(pval)
print(pval.shape)

fig = plt.figure()
plt.matshow(pval, fig.number)
fig.savefig('pmat.png')

pickle.dump([corrmat.values, pval], open('mats.pkl', 'wb'))
np.savetxt('outcorrs.csv', corrmat.values, delimiter=',')
np.savetxt('outpvals.csv', pval, delimiter=',')