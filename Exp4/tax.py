# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:28:42 2020

@author: pc
"""
def taxRate(base):
    if base < 0:
        tax = 0
    elif base <= 1500:
        tax = base * 0.03
    elif base > 1500 and base <= 4500:
        tax = base * 0.1 - 105
    elif base > 4500 and base <= 9000:
        tax = base * 0.2 - 555
    elif base > 9000 and base <= 35000:
        tax = base * 0.25 - 1005
    elif base > 35000 and base <= 55000:
        tax = base * 0.3 - 2755
    elif base > 55000 and base <= 80000:
        tax = base * 0.35 - 5505
    elif base > 80000:
        tax = base * 0.45 - 13505

    #print('Tax of salary is : %d' % tax)

    return tax

def salaryAfterTax(salaryBeforeTax):

    #免征点3500 ,个人五险一金比率，养老8%，医疗2%，失业0.2%，公积金12%
    threshold = 3500
    oldAgeRating = 0.08
    medicalRating = 0.02
    unemployRating = 0.002
    housingFundRating = 0.12

    # 2016年社平工资7706，五险一金上限是社评三倍工资
    averageSalary = 7706
    tripleAverageSalary = 3 * averageSalary

    if salaryBeforeTax < tripleAverageSalary:
        totalInsurance = salaryBeforeTax * (oldAgeRating + medicalRating + unemployRating + housingFundRating)
        housingFund = salaryBeforeTax * housingFundRating
    else:
        totalInsurance = tripleAverageSalary * (
            oldAgeRating + medicalRating + unemployRating + housingFundRating)
        housingFund = tripleAverageSalary * housingFundRating   #公积金封顶
        #housingFund = salaryBeforeTax * housingFundRating     #公司给补超额公积金部分

    # 纳税额
    payment = salaryBeforeTax - totalInsurance - threshold
    tax = taxRate(payment)

    # 税后工资
    salaryAfterTax = salaryBeforeTax - totalInsurance - tax
    actualIncome = salaryAfterTax + housingFund * 2

    print('Housing Fund is : %d' % housingFund)
    print('Total insurance is : %d ' % totalInsurance)
    print('Tax of salary is : %d' % tax)
    print('Salary after tax is : %d' % salaryAfterTax)
    print('Actual income including housing fund is : %d ' % actualIncome)
    print('Actual income Percent is : %.2f %%' % float(actualIncome * 100 / salaryBeforeTax))

    return salaryAfterTax

if __name__ == '__main__':
    salary = int(input('Please input your Salary before tax:'))
    salaryAfterTax(salary)