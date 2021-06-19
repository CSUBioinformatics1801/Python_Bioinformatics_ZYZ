# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:57:51 2020

@author: pc
"""
# =============================================================================
# n=0
# print('output 10 TENƎ⊥ num bigger than 100:')
# for a in range(200,1000):
#     if a//100==a%10:
#         print(a,end=" ")
#         n+=1
#     if n==30:
#         break
# =============================================================================
# =============================================================================
# while True:
#     a=eval(input("input a int(end with -1):"))
#     if type(a)!=type(1):
#         print('Data Type False, input again')
#     else:
#         if a==-1:
#             break
# =============================================================================
# =============================================================================
# import random
# i=random.randint(0, 10)
# for j in range(1,7):
#     num=int(input('input a int the '+str(j)+'th time:'))
#     if num<i:
#         print('too small')
#     elif num>i:
#         print('too big')
#     else:
#         if(num==i):
#             print('For the '+str(j)+'th time you\'ve Done, it\'s '+ str(i))
#             break
#         if(j==7):
#             print('stupid enough to guess '+str(i))
#             break
# =============================================================================
# =============================================================================
# x=1;y=1;
# while y<=5:
#     x*=y
#     y+=2
# print(x)
# =============================================================================
# =============================================================================
# import os
# # print(os.getcwd())
# codon_table = {
#     'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'CGU':'R', 'CGC':'R',   
#     'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 'UCU':'S', 'UCC':'S',
#     'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S', 'AUU':'I', 'AUC':'I',
#     'AUA':'I', 'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L',
#     'CUG':'L', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', 'GUU':'V',
#     'GUC':'V', 'GUA':'V', 'GUG':'V', 'ACU':'T', 'ACC':'T', 'ACA':'T',
#     'ACG':'T', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'AAU':'N',
#     'AAC':'N', 'GAU':'D', 'GAC':'D', 'UGU':'C', 'UGC':'C', 'CAA':'Q',
#     'CAG':'Q', 'GAA':'E', 'GAG':'E', 'CAU':'H', 'CAC':'H', 'AAA':'K',
#     'AAG':'K', 'UUU':'F', 'UUC':'F', 'UAU':'Y', 'UAC':'Y', 'AUG':'M',
#     'UGG':'W',
#     'UAG':'STOP', 'UGA':'STOP', 'UAA':'STOP'
#     }     #读取密码子表
# 
# rna = ''
# for line in open('A06662-RNA.fasta'): #读取RNA序列文件
#     if not line.startswith('>'): 
#         rna = rna + line.strip()
# rna=rna.replace('T','U')
# print(rna)
# #UGGGACCAGUCAGCAGAGGCAGCGUGUGUGCGCGUGCGUGUGCGUGUGUGUGCGUGUGUGUGUGUACGCUUGCAUUUGUGUCGGGUGGGUAAGGAGAUAGAGAUGGGCGGGCAGUAGGCCCAGGUCCCGAAGGCCUUGAACCCACUGGUUUGGAGUCUCCUAAGGGCAAUGGGGGCCAUUGAGAAGUCUGAACAGGGCUGUGUCUGAAUGUGAGGUCUAGAAGGAUCCUCCAGAGAAGCCAGCUCUAAAGCUUUUGCAAUCAUCUGGUGAGAGAACCCAGCAAGGAUGGACAGGCAGAAUGGAAUAGAGAUGAGUUGGCAGCUGAAGUGGACAGGAUUUGGUACUAGCCUGGUUGUGGGGAGCAAGCAGAGGAGAAUCUGGGACUCUGGUGGUCUGGCCUGGGGCAGACGGGGGUGUCUCAGGGGCUGGGAGGGAUGAGAGUAGGAUGAUACAUGGUGGUGUCUGGCAGGAGGCGGGCAAGGAUGACUAUGUGAAGGCACUGCCCGGGCAACUGAAGCCUUUUGAGACCCUGCUGUCCCAGAACCAGGGAGGCAAGACCUUCAUUGUGGGAGACCAGGUGAGCAUCUGGCC
# 
# for frame in range(3):
#     prot = '' 
#     print('Reading frame ' + str(frame + 1))
#     for i in range(frame, len(rna), 3):
#         codon = rna[i:(i + 3)]
#         if codon in codon_table:
#             if codon_table[codon] == 'STOP':
#                 prot = prot + '*'
#             else: 
#                 prot = prot + codon_table[codon]
#         else:
#             prot = prot + '-'   
#     
#     i = 0
#     while i < len(prot):
#         print(prot[i:i + 48])
#         i = i + 48
# # Reading frame 1
# # WDQSAEAACVRVRVRVCACVCVRLHLCRVGKEIEMGGQ*AQVPKALNP
# # LVWSLLRAMGAIEKSEQGCV*M*GLEGSSREASSKAFAIIW*ENPARM
# # DRQNGIEMSWQLKWTGFGTSLVVGSKQRRIWDSGGLAWGRRGCLRGWE
# # G*E*DDTWWCLAGGGQG*LCEGTARATEAF*DPAVPEPGRQDLHCGRP
# # GEHLA
# # Reading frame 2
# # GTSQQRQRVCACVCVCVRVCVYACICVGWVRR*RWAGSRPRSRRP*TH
# # WFGVS*GQWGPLRSLNRAVSECEV*KDPPEKPALKLLQSSGERTQQGW
# # TGRME*R*VGS*SGQDLVLAWLWGASRGESGTLVVWPGADGGVSGAGR
# # DESRMIHGGVWQEAGKDDYVKALPGQLKPFETLLSQNQGGKTFIVGDQ
# # VSIW-
# # Reading frame 3
# # GPVSRGSVCARACACVCVCVCTLAFVSGG*GDRDGRAVGPGPEGLEPT
# # GLESPKGNGGH*EV*TGLCLNVRSRRILQRSQL*SFCNHLVREPSKDG
# # QAEWNRDELAAEVDRIWY*PGCGEQAEENLGLWWSGLGQTGVSQGLGG
# # MRVG*YMVVSGRRRARMTM*RHCPGN*SLLRPCCPRTREARPSLWETR
# # *ASG-
# =============================================================================
# =============================================================================
# 
# import requests
# import re
# import os
# from bs4 import BeautifulSoup
# 
# #get mRNA list
# sch_gene_name=input('Input a homo gene name you wanna search:')
# sch_url='https://www.ncbi.nlm.nih.gov/gene?term=(homo%5BOrganism%5D)%20AND%20'+sch_gene_name+'%5BGene%20Name%5D#reference-sequences'
# print('Searching...\nThis may take few centuries...')
# res = requests.get(sch_url)
# res.encoding='gbk'
# soup = BeautifulSoup(res.text,"html.parser")
# match_mRNAs_url = re.findall(r'/nuccore/NM_[0-9]+.[0-9]?',res.text)
# print('matched mRNA number: ')
# print(len(match_mRNAs_url))
# mRNA_name=[]
# for i in range(len(match_mRNAs_url)):
#     mRNA_name.append(re.search(r'NM_\S+', match_mRNAs_url[i]).group())
# print(mRNA_name)
# mRNA_uid=[]
# 
# codon_table = {
#     'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'CGU':'R', 'CGC':'R',   
#     'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 'UCU':'S', 'UCC':'S',
#     'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S', 'AUU':'I', 'AUC':'I',
#     'AUA':'I', 'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L',
#     'CUG':'L', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', 'GUU':'V',
#     'GUC':'V', 'GUA':'V', 'GUG':'V', 'ACU':'T', 'ACC':'T', 'ACA':'T',
#     'ACG':'T', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'AAU':'N',
#     'AAC':'N', 'GAU':'D', 'GAC':'D', 'UGU':'C', 'UGC':'C', 'CAA':'Q',
#     'CAG':'Q', 'GAA':'E', 'GAG':'E', 'CAU':'H', 'CAC':'H', 'AAA':'K',
#     'AAG':'K', 'UUU':'F', 'UUC':'F', 'UAU':'Y', 'UAC':'Y', 'AUG':'M',
#     'UGG':'W',
#     'UAG':'STOP', 'UGA':'STOP', 'UAA':'STOP'
#     }     
# 
# #downloading mRNA fasta
# print('Start downloading mRNA sequences')
# for t in range(len(match_mRNAs_url)):
#     print('Searching protein sequences...protein name= '+mRNA_name[t])
#     mRNA_sch_url='https://www.ncbi.nlm.nih.gov'+match_mRNAs_url[t]
#     mRNA_res = requests.get(mRNA_sch_url)
#     mRNA_res.encoding='gbk'
#     match_mRNAs = re.findall(r'<span class="ff_line" id="'+mRNA_name[t]+'_[0-9]+">\S+</span>',mRNA_res.text)
#     match_mRNAs=(re.search(r'(?<=<meta name="ncbi_uidlist" content=")[0-9]+(?=" />)',mRNA_res.text)).group()
#     mRNA_uid.append(match_mRNAs)
#     mRNA_sch_url='https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?tool=portal&save=file&log$=seqview&db=nuccore&report=fasta&id='+mRNA_uid[t]+'&conwithfeat=on&withparts=on&hide-cdd=on'
#     mRNA_fasta = requests.get(mRNA_sch_url).text
#     
#     #storing mRNA sequences
#     fh = open(os.getcwd()+'\\'+mRNA_name[t]+'.fasta', 'w', encoding='utf-8')
#     fh.write(mRNA_fasta)
#     fh.close()
#     mRNA_seq=''
#     mRNA_trans_predict=[]
#     
#     #predict translated sequences and store it
#     for line in open(os.getcwd()+'\\'+mRNA_name[t]+'.fasta'): 
#         if not line.startswith('>'): 
#                 mRNA_seq = mRNA_seq + line.strip()
#     mRNA_seq=mRNA_seq.replace('T', 'U')
#     for frame in range(3):
#         prot = '' 
#         for i in range(frame, len(mRNA_seq), 3):
#             codon = mRNA_seq[i:(i + 3)]
#             if codon in codon_table:
#                 if codon_table[codon] == 'STOP':
#                     prot = prot + '*'
#                 else: 
#                     prot = prot + codon_table[codon]
#             else:
#                 prot = prot + '-'
#         fp=open(os.getcwd()+'\\'+mRNA_name[t]+'pt_pdct.txt', 'a')
#         if(fp.writable()):
#             fp.write('\nReading frame ' + str(frame + 1)+'\n'+prot)
#         fp.close()
# =============================================================================
