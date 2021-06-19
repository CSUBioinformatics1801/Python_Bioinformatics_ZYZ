gene_names=['Control','Sora','5AZ','3TH','H61']
lumino=[520000,690000,230000,150000,310000]
ds=dict(zip(gene_names,lumino))
print('zip:',ds)
tmp_g_n=input("input a gene name:")
if tmp_g_n in ds:
    print(tmp_g_n,'lumino:',ds.get(tmp_g_n))
else:
    print('not in dic!')
    