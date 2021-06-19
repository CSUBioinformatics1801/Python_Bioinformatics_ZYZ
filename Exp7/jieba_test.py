import jieba
# f=open('D:\\Remain\\7.python及其生物信息学应用\\实践\\实践7\\3-6实践材料.txt','rb')
# s=f.read()
# import jieba.analyse
# s='这些结果表明，舒尼替尼和RFA整合疗法是一种优于每种疗法的有效治疗策略，可显着抑制肿瘤生长并延长被治疗小鼠的寿命'
# jieba.add_word('整合疗法')
# jieba.add_word('治疗策略')
# r=jieba.lcut_for_search(s)
# print(r)
s='勤洗手，戴口罩有助于预防新冠病毒肺炎'
jieba.add_word('新冠病毒')
print('added')
r=jieba.lcut(s)
print(r)
print('deleted')
jieba.del_word('新冠病毒')
r=jieba.lcut(s)
print(r)
