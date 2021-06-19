a=input('input a group of strings(more than 4):')
b=tuple(a)
print('tuple',a)
print('First 2:',b[:2])
print('Last 2:',b[-2:])
c=[]
for i in b:
    if i not in c:
        print(i,':%s times'%b.count(i))
        c.append(i)
print("list c:",c)