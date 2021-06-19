a=[]
tmp_str=input()
a=tmp_str.split(',')
avg=0.0
for i in a:
    avg+=float(i)/len(a)
print(avg)