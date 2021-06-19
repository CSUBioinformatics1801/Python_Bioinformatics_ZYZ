import os
with open(os.getcwd()+'\\练习1\\stinfo.txt', 'r',encoding='utf-8') as f:
    # print(f.read())
    temp_list=f.readlines()
    print(temp_list)
    outputlist=[]
    for i in range(len(temp_list)):
        outputlist.append(temp_list[i][2:-1].split(','))
        outputlist[i].append(int(outputlist[i][1])+int(outputlist[i][2])+int(outputlist[i][3]))
    outputlist.sort(key=lambda x:(x[4],x[0]))
    outputlist.reverse()
    print(outputlist)
f.close()