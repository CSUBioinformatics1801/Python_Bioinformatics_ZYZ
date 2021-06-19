import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
data=pd.read_table("实践8\\GSE5583.txt",header=0,index_col=0)
print("Previous 5:\n",data.head())
number_of_genes=len(data.index)
print("Gene Number:",number_of_genes)
# normalization
data2=np.log2(data+0.0001)
print("Previous 5:\n",data2.head())
# diff P
from scipy import stats
pvalue=[]
for i in range(0,number_of_genes):
    ttest=stats.ttest_ind(data2.iloc[i,0:3],data2.iloc[i,3:6])
    pvalue.append(ttest[1])
# draw P values graph
wt=data2.loc[:,'WT.GSM130365':'WT.GSM130367'].mean(axis=1)
ko=data2.loc[:,'KO.GSM130368':'KO.GSM130370'].mean(axis=1)
fold=ko-wt
plt.hist(-np.log(pvalue))
plt.title("Histogram of P-value")
plt.show()
# draw diff analysis graph
gene_array=np.asarray(pvalue)
result=pd.DataFrame({'pvalue':gene_array,'FoldChange':fold})
result['log(pvalue)']=-np.log10(result['pvalue'])
# select standard
# 1> abs(diff)>1
# 2> P<0.05
result['sig']='normal'
result['size']=np.abs(result['FoldChange'])/10
result.loc[(result.FoldChange>1)&(result.pvalue<0.05),'sig']='up'
result.loc[(result.FoldChange<-1)&(result.pvalue<0.05),'sig']='down'
# draw volcano graph
ax=sns.scatterplot(x="FoldChange",y="log(pvalue)",hue='sig',hue_order=('down','normal','up'),palette=("#377EB8","grey","#E41A1C"),data=result)
ax.set_ylabel('-log(pvalue)',fontweight='bold')
ax.set_xlabel('FoldChange',fontweight='bold')
plt.show()
# draw hotmap
fold_cutoff=1
pvalue_cutoff=0.05
filtered_ids=[]
for i in range(0,number_of_genes):
    if(abs(fold[i])>=fold_cutoff) and (pvalue[i]<=pvalue_cutoff):
        filtered_ids.append(i)
filtered=data2.iloc[filtered_ids,:]
print("Number of DE genes:")
print(len(filtered.index))
sns.clustermap(filtered,cmap='RdYlGn_r',standard_scale=0)
plt.show()
