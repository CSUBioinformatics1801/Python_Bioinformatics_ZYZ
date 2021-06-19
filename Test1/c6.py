f=open('data.csv','w')
a=[1,2,3],[4,5,6],[7,8,9]
for x in a:
    for y in [0,1]:
       f.write(str(x[y])
       f.write(',')
   f.write(str(x[2]))
   f.write('\n')
f.close()
