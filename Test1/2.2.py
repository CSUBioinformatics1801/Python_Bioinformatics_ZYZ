listtmp=[('P',9.74),('G',9.79),('B',9.69),('A',9.85),('M',9.78),('L',9.86)]
listtmp.sort(key=lambda x:(x[1],x[0]))
listtmp.reverse()
for i in range(len(listtmp)):
    print('Rank:'+str(i+1)+' '+str(listtmp[i]))