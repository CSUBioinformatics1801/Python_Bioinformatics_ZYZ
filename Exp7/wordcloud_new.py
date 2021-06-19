import jieba
import jieba.posseg as pseg
import wordcloud
import tkinter
from PIL import Image,ImageTk
str=open('红楼梦.txt','rb').read()
wlist=pseg.lcut(str)
wtimes={}
cstr=[];sw=[]
for a in wlist:
    if a.flag=='nr':
        wtimes[a.word]=wtimes.get(a.word,0)+1
        cstr.append(a.word)
    else:sw.append(a.word)
wlist=list(wtimes.keys())
wlist.sort(key=lambda x:wtimes[x],reverse=True)
for a in wlist[:10]:
    print(a,wtimes[a],sep='\t')
text=' '.join(cstr)
cloud=wordcloud.WordCloud(font_path='D:\\Remain\\7.python及其生物信息学应用\\实践\\实践7\\simsun.ttc',background_color='white',
                          stopwords=sw,collocations=False,width=640,height=480).generate(text)
file=cloud.to_file('herocloud.png')
root=tkinter.Tk()
img=Image.open('herocloud.png')
pic=ImageTk.PhotoImage(img)
imgLabel=tkinter.Label(root,image=pic)
imgLabel.pack()
root.mainloop()

