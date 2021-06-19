import matplotlib.pyplot as plt
import numpy as np
def randrange(n,vmin,vmax):
    return (vmax-vmin)*np.random.rand(n)+vmin
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
n=180
for c,m,zlow,zhigh in [('r','o',-50,-25),('b','^',-30,-5)]:
    xs=randrange(n,23,32)
    ys=randrange(n,0,100)
    zs=randrange(n,zlow,zhigh)
    ax.scatter(xs,ys,zs,c=c,marker=m)
ax.set_xlabel('X label')
ax.set_ylabel('Y label')
ax.set_zlabel('Z label')
plt.savefig('scatter test1.png',dpi=600)
plt.show()