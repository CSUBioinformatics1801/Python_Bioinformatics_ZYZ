import jieba
import jieba.posseg as ps
test_str='蛋白质或核苷酸三维结构存储在PDB文件中'
# jieba.add_word('核苷酸三维结构')
# seg_list = jieba.cut(test_str, cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
# seg_list = jieba.cut(test_str, cut_all=True)
# print("Default Mode: " + "/ ".join(seg_list))  # 全模式
# seg_list = jieba.lcut(test_str, cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
# seg_list = jieba.lcut(test_str, cut_all=True)
# print("Default Mode: " + "/ ".join(seg_list))  # 全模式
r=ps.lcut(test_str)
print(r)
