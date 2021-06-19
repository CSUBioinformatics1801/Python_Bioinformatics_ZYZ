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
    pattern=re.compile("[ST]Q")
    match=pattern.search(seq_content)
    if match:
        print('%10s'%(seq_content[match.start()-4:match.end()+4]))
        print('%6s'%match.group())
    else:
        print('No match')