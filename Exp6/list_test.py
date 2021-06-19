a=input('input multinums splitted ori_listy ",":')
ori_list=a.split(',')
n=0
for c in ori_list:
    ori_list[n]=int(c)
    n+=1
print("origin list:",ori_list)
x=eval(input('input a num:'))
x_index=ori_list.index(x)
if 0<x_index<len(ori_list):
    print('max adjcent num:',ori_list[x_index-1],ori_list[x_index+1])
if x in ori_list:
    print(x,"'s index of the list is",ori_list.index(x))
    ori_list.remove(x)
    print("Delete %s successfully!"%x)
else:
    ori_list.append(x)
    print("%s has ori_listeen added"%x)
ori_list.sort()
print("Sorted:",ori_list)
