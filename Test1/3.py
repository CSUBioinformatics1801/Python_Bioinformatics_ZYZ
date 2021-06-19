sheet1={"orange":12.5,"dragonfruit":15.8,"pear":4.5}
sheet2={"apple":5.5,"banana":4.8,"pear":4.5,"watermelon":5.6}
result_set=(set( sheet2.keys() ) | set( sheet1.keys() ))
# print(result_set)
result_sheet={}
for i in result_set:
    # print(str(i))
    value=''
    if(str(i) in sheet1.keys()):
        value=sheet1[str(i)]
    elif (str(i) in sheet2.keys()):
        value=sheet2[str(i)]
    temp={str(i):value}
    result_sheet.update(temp)
print(result_sheet)
print('input a product name:')
a=input()
print(result_sheet[a])