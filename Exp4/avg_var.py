import numpy
with open('实践4\\data.txt', 'r') as f:
    list_temp=list(map(float, f.readlines()))
    print('Std = ',numpy.std(list_temp),'average=',numpy.mean(list_temp))