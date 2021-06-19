import requests,re
def html_re():
    response=requests.get(url).text
    id=re.findall('data-chunk-ids="(.*?)>',response,re.S)
    ids=id[0].split(',')
    return ids

def html_title():
    content=[]
    for i in url1:
        html1=requests.get(i)
        html1=html1.text
        title=re.findall('<title>(.*?) - PubMed</title>',html1)
        content.append(title)
    return content

if __name__ == "__main__":
    content=input('key word input:')
    url='https://pubmed.ncbi.nlm.nih.gov/?term='+content+'&sort=date'
    ids=html_re()
    url1=['https://pubmed.ncbi.nlm.nih.gov/'+i+'/' for i in ids]
    title=html_title()
    print(title)