def fsum(*n):
    s=0
    for a in n:
        s+=a
    return s
a=input('input multi data:')
b='fsum(%s)'%a
print('sum =',eval(b))