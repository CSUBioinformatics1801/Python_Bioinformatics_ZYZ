# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:10:08 2020

@author: pc
"""
# =============================================================================
# a,b=eval(input("key in 2 numbers as a,b:"))
# print(a,'+',b,'=',a+b)
# print(a,'-',b,'=',a-b)
# print(a,'*',b,'=',a*b)
# print(a,'/',b,'=',round(a/b,2))
# =============================================================================
# =============================================================================
# a=eval(input('input a int less than 255'))
# print('binary:{08b}'.format(a))
# =============================================================================
# =============================================================================
# insulin_seq="MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN"
# for amino_acid in "ACDEFGHIKLMNPQRSTVWTY":
#     number=insulin_seq.count(amino_acid)
#     print(amino_acid,number)
# =============================================================================
# =============================================================================
# a=eval(input("Input a int between 0,255:"))
# print(bin(a)+'\n'+hex(a)+'\n'+oct(a))
# =============================================================================
# =============================================================================
# a="a b c d e"
# print(a)
# print(a.replace(' ','\n'))
# =============================================================================
# =============================================================================
# a='123456789'
# n=len(a)
# m=2
# while m<=n:
#     print(' '*(21-m),end='')
#     print('{}{}'.format(a[:m], a[m-2::-1]))
#     m+=1
# =============================================================================
# =============================================================================
# n=5;m=6
# while n>=1:
#     print('{}{}'.format(''*m,'*'*(2*n-1)))
#     n-=1
#     m+=1
# =============================================================================
# =============================================================================
# temp='rfh4289ogiqwhg21r9w8hg[0843hB4Gm20mrdiewruwuf2inut24n89n34803'
# macchar=max(list(temp))
# print(macchar)
# templist=[]
# for i in range(len(temp)):
#     if temp[i]==macchar:
#             templist.append(str(i))
# print(templist)
# =============================================================================
# =============================================================================
# a=input('Input a word:')
# print('{:*^30}'.format(a))
# =============================================================================
# =============================================================================
# ATP=3.5;ADP=1.8;Pi=5.0;R=0.00831;T=298;ΔG0=-30.5;
# import math
# print('ΔG=%.2f kcal/mol'%float((ΔG0+R*T*math.log(ADP*Pi/ATP))/4.184))
# =============================================================================
import requests
import re
from bs4 import BeautifulSoup
sch_gene_name=input('Input a homo gene name you wanna search:')
sch_url='https://www.ncbi.nlm.nih.gov/gene?term=(homo%5BOrganism%5D)%20AND%20'+sch_gene_name+'%5BGene%20Name%5D#reference-sequences'
print('Searching...\nThis may take few centuries...')
res = requests.get(sch_url)
res.encoding='gbk'
soup = BeautifulSoup(res.text,"html.parser")
match_pts_url = re.findall(r'/protein/NP_[0-9]+.[0-9]?',res.text)
print('matched protein number: ')
print(len(match_pts_url))
pt_name=[]
for i in range(len(match_pts_url)):
    pt_name.append(re.search(r'NP_\S+', match_pts_url[i]).group())
print(pt_name)
print('Start downloading protein sequences')
for t in range(len(match_pts_url)):
    print('Searching protein sequences...protein name= '+pt_name[i])
    pt_sch_url='https://www.ncbi.nlm.nih.gov'+match_pts_url[t]
    pt_res = requests.get(pt_sch_url)
    pt_res.encoding='gbk'
    match_pts = re.findall(r'<span class="ff_line" id="'+pt_name[i]+'_[0-9]+">\S+</span>',pt_res.text)
    #print(match_pts)
    match_pts=(re.search(r'(?<=<meta name="ncbi_uidlist" content=")[0-9]+(?=" />)',pt_res.text)).group()
    pt_sch_url_re='https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id='+match_pts+'&db=protein&report=genpept&conwithfeat=on&show-cdd=on&retmode=html&withmarkup=on&tool=portal&log$=seqview&maxdownloadsize=1000000'
    pt_res_re = requests.get(pt_sch_url_re)
    pt_res_re.encoding='gbk'
    match_ptseqs=re.findall(r'<span class="ff_line" id="\S+_\S+">[a-z\s]+(?=</span>)', pt_res_re.text)
    match_ptseqs_new=[]
    for i in range(len(match_ptseqs)):
        latarrow=match_ptseqs[i].find('>')
        match_ptseqs_new.append(match_ptseqs[i][latarrow+1:])
    seq_content="".join(match_ptseqs_new)
    seq_content=seq_content.replace(' ','')
    seq_content=seq_content.upper()
    print(seq_content)
    for amino_acid in "ACDEFGHIKLMNPQRSTVWTY":
        number=seq_content.count(amino_acid)
        print(amino_acid,number)
