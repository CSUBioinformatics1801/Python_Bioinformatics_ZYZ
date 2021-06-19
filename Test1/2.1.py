import sys
reload(sys)
sys.setdefaultencoding('utf8')
import json
import time
path='test.txt'
a= open(path).readlines()
# print a
print type(a)
arr01=[]
for x in a:
    #print x
    # print type(x)
    y=json.loads(x)
    for z in y:
        if z =='tz':
            # if y[z]:
              print  str(z)+'=>'+str(y[z])
              arr01.append(y[z])
    print '--------------------------------'
print arr01
def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x]=1
    return counts
aa= get_counts(arr01)
print aa
print type(aa)
for k in aa:
    print k+'=>'+str(aa[k])