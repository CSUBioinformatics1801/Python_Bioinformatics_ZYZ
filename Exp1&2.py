# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 10:12:30 2020

@author: pc
"""
# =============================================================================
# def translate_fachrenheit_temp(c_t):
#     return c_t*1.8+32
# 
# tmp=input("Input current temperature:")
# c_t=float(tmp)
# print(translate_fachrenheit_temp(c_t))
# =============================================================================

# =============================================================================
# tmp_str=input("Your Name,Ideal University:")
# temp_list=tmp_str.split(',')
# print("World is wide in enough,for "+temp_list[0]+" and "+temp_list[1]+".")
# =============================================================================

# =============================================================================
# from turtle import*
# pencolor("blue")
# fillcolor("green")
# begin_fill()
# i=0;
# while True:
#     forward(100)
#     if(i%2==0):
#         right(300)
#     else:
#           right(120)   
#     i+=1
#     if abs(pos())<1:
#         break
# end_fill()
# hideturtle()
# =============================================================================

# =============================================================================
# import math
# n=eval(input('radius input:'))
# print("surface="+ str(math.pow(n, 2)*math.pi))
# =============================================================================
# =============================================================================
# # coding=utf-8
#   
# import turtle
# from datetime import *
#   
# # 抬起画笔，向前运动一段距离放下
# def Skip(step):
#     turtle.penup()
#     turtle.forward(step)
#     turtle.pendown()
#   
# def mkHand(name, length):
#     # 注册Turtle形状，建立表针Turtle
#     turtle.reset()
#     Skip(-length * 0.1)
#     # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
#     turtle.begin_poly()
#     turtle.forward(length * 1.1)
#     # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
#     turtle.end_poly()
#     # 返回最后记录的多边形。
#     handForm = turtle.get_poly()
#     turtle.register_shape(name, handForm)
#   
# def Init():
#     global secHand, minHand, hurHand, printer
#     # 重置Turtle指向北
#     turtle.mode("logo")
#     # 建立三个表针Turtle并初始化
#     mkHand("secHand", 135)
#     mkHand("minHand", 125)
#     mkHand("hurHand", 90)
#     secHand = turtle.Turtle()
#     secHand.shape("secHand")
#     minHand = turtle.Turtle()
#     minHand.shape("minHand")
#     hurHand = turtle.Turtle()
#     hurHand.shape("hurHand")
#     
#     for hand in secHand, minHand, hurHand:
#         hand.shapesize(1, 1, 3)
#         hand.speed(0)
#     
#     # 建立输出文字Turtle
#     printer = turtle.Turtle()
#     # 隐藏画笔的turtle形状
#     printer.hideturtle()
#     printer.penup()
#      
# def SetupClock(radius):
#     # 建立表的外框
#     turtle.reset()
#     turtle.pensize(7)
#     for i in range(60):
#         Skip(radius)
#         if i % 5 == 0:
#             turtle.forward(20)
#             Skip(-radius - 20)
#             
#             Skip(radius + 20)
#             if i == 0:
#                 turtle.write(int(12), align="center", font=("Courier", 14, "bold"))
#             elif i == 30:
#                 Skip(25)
#                 turtle.write(int(i/5), align="center", font=("Courier", 14, "bold"))
#                 Skip(-25)
#             elif (i == 25 or i == 35):
#                 Skip(20)
#                 turtle.write(int(i/5), align="center", font=("Courier", 14, "bold"))
#                 Skip(-20)
#             else:
#                 turtle.write(int(i/5), align="center", font=("Courier", 14, "bold"))
#             Skip(-radius - 20)
#         else:
#             turtle.dot(5)
#             Skip(-radius)
#         turtle.right(6)
#          
# def Week(t):  
#     week = ["星期一", "星期二", "星期三",
#             "星期四", "星期五", "星期六", "星期日"]
#     return week[t.weekday()]
#   
# def Date(t):
#     y = t.year
#     m = t.month
#     d = t.day
#     return "%s %d%d" % (y, m, d)
#   
# def Tick():
#     # 绘制表针的动态显示
#     t = datetime.today()
#     second = t.second + t.microsecond * 0.000001
#     minute = t.minute + second / 60.0
#     hour = t.hour + minute / 60.0
#     secHand.setheading(6 * second)
#     minHand.setheading(6 * minute)
#     hurHand.setheading(30 * hour)
#      
#     turtle.tracer(False)
#     printer.forward(65)
#     printer.write(Week(t), align="center",
#                   font=("Courier", 14, "bold"))
#     printer.back(130)
#     printer.write(Date(t), align="center",
#                   font=("Courier", 14, "bold"))
#     printer.home()
#     turtle.tracer(True)
#   
#     # 100ms后继续调用tick
#     turtle.ontimer(Tick, 100)
#   
# def main():
#     # 打开/关闭龟动画，并为更新图纸设置延迟。
#     turtle.tracer(False)
#     Init()
#     SetupClock(160)
#     turtle.tracer(True)
#     Tick()
#     turtle.mainloop()
#   
# if __name__ == "__main__":
#     main()
# =============================================================================
# =============================================================================
# # coding=utf-8
# import turtle
# import time
# #pencolor=color1, fillcolor=color2
# turtle.speed(10)
# turtle.color("red", "yellow")
# turtle.begin_fill()
# for _ in range(50):
#     turtle.forward(200)
#     turtle.left(170)
# turtle.end_fill()
# turtle.mainloop()
# =============================================================================
# =============================================================================
# import turtle
# import time
# turtle.speed(10)
# # 设置初始位置  
# turtle.penup()  
# turtle.left(90)  
# turtle.fd(200)  
# turtle.pendown()  
# turtle.right(90)
# # 花蕊  
# turtle.fillcolor("red")  
# turtle.begin_fill()  
# turtle.circle(10,180)  
# turtle.circle(25,110)  
# turtle.left(50)  
# turtle.circle(60,45)  
# turtle.circle(20,170)  
# turtle.right(24)  
# turtle.fd(30)  
# turtle.left(10)  
# turtle.circle(30,110)  
# turtle.fd(20)  
# turtle.left(40)  
# turtle.circle(90,70)  
# turtle.circle(30,150)  
# turtle.right(30)  
# turtle.fd(15)  
# turtle.circle(80,90)  
# turtle.left(15)  
# turtle.fd(45)  
# turtle.right(165)  
# turtle.fd(20)  
# turtle.left(155)  
# turtle.circle(150,80)  
# turtle.left(50)  
# turtle.circle(150,90)  
# turtle.end_fill()  
# # 花瓣1  
# turtle.left(150)  
# turtle.circle(-90,70)  
# turtle.left(20)  
# turtle.circle(75,105)  
# turtle.setheading(60)  
# turtle.circle(80,98)  
# turtle.circle(-90,40)  
# # 花瓣2  
# turtle.left(180)  
# turtle.circle(90,40)  
# turtle.circle(-80,98)  
# turtle.setheading(-83)  
# # 叶子1  
# turtle.fd(30)  
# turtle.left(90)  
# turtle.fd(25)  
# turtle.left(45)  
# turtle.fillcolor("green")  
# turtle.begin_fill()  
# turtle.circle(-80,90)  
# turtle.right(90)  
# turtle.circle(-80,90)  
# turtle.end_fill()  
# turtle.right(135)  
# turtle.fd(60)  
# turtle.left(180)  
# turtle.fd(85)  
# turtle.left(90)  
# turtle.fd(80)  
# # 叶子2  
# turtle.right(90)  
# turtle.right(45)  
# turtle.fillcolor("green")  
# turtle.begin_fill()  
# turtle.circle(80,90)  
# turtle.left(90)  
# turtle.circle(80,90)  
# turtle.end_fill()  
# turtle.left(135)  
# turtle.fd(60)  
# turtle.left(180)  
# turtle.fd(60)  
# turtle.right(90)  
# turtle.circle(200,60) 
# =============================================================================
# =============================================================================
# a=int(input('first:'))
# b=int(input('second:'))
# print(a,end='')
# print('+',end='')
# print(b,end='')
# print('=',end='')
# print(a+b,end='')
# =============================================================================
# =============================================================================
# import turtle
# turtle.pencolor('blue')
# turtle.fillcolor("green")
# turtle.begin_fill()
# for _ in range(9):
#     turtle.forward(200)
#     turtle.left(120)
# turtle.end_fill()
# turtle.hideturtle()
# =============================================================================
# =============================================================================
# import turtle as t
# colorList = ["red","purple","skyblue","yellow","hotpink","green","blue","black","darkred"]
# t.pensize(3)
# t.speed(10)
# for i in range(1,10):
#     t.penup()
#     t.sety(-15*i) 
#     t.pendown()
#     t.pencolor(colorList[i-1])
#     t.circle(15*i)
# else:
#     t.hideturtle()
# t.done()
# =============================================================================
# =============================================================================
# import turtle
# turtle.speed(1)
# turtle.setup(650,350,200,200) #设置窗口大小和位置
# turtle.penup()							#将画笔抬起，以便从窗口中心移动并且不留下痕迹
# turtle.fd(-250)							#将画笔反向移动150个像素
# turtle.pendown()						#将画笔放下
# turtle.pensize(20)					#设置画笔粗细
# turtle.pencolor("grey")				#设置画笔颜色
# turtle.seth(-40)						#改变画笔指向
# for i in range(4):						#设置循环次数
#     turtle.circle(40,80)
#     turtle.circle(-40,80)
# turtle.circle(40,80/2)
# turtle.fd(40)
# turtle.circle(16,180)
# turtle.fd(40*2/3)
# turtle.done()
# =============================================================================
# import turtle as t
# t.setup(1000,350,0,200)
# t.pensize(4)
# t.speed(3)
# t.pencolor("black")
# t.fillcolor("blue")
# #t.begin_fill()
# #t.goto(-400,0)
# for i in range(1,3):
#     t.penup()
#     t.goto(-50*i,-50/pow(3,0.5)*i)
#     t.pendown()
#     for _ in range(3):
#         t.fd(100*i)
#         t.left(120)
# #t.end_fill()
# for i in range(1,3):
#     t.penup()
#     t.goto(-20, -80/pow(3,0.5)*i)
#     t.pendown()
#     t.write("Edge="+str(i)+"00", font = ("Times", 12, "bold"))
# t.hideturtle()
# t.done()
# =============================================================================

# =============================================================================
# import turtle as t
# t.setup(700,650,0,50)
# t.pensize(2)
# t.speed(0)
# t.pencolor("blue")
# t.fillcolor("blue")
# t.tracer(8,25)
# t.penup()
# t.goto(-300,300)
# t.pendown()
# color_array=["black","yellow","green","blue","indigo","purple"]
# #t.begin_fill()
# # t.goto(-400,0)
# for i in range(600):
#     n=599-i
#     t.pencolor(color_array[int(n/100)])
#     t.forward(n)
#     t.fd(n/10)
#     t.right(90)
#   #  t.pencolor(color_array[int(x/20)])
# t.update()
# #t.end_fill()
# #t.penup()
# # t.pendown()
# # t.write("Mutipolygons and circle", font = ("Times", 18, "bold"))
# t.hideturtle()
# t.done()
# =============================================================================
# =============================================================================
# #绘制大耳朵兔
# from turtle import *
# speed(0)
#  
# #小兔的面部
# color("pink")
# pensize(5)
# circle(radius=100)#脸
#  
# #眼睛
# # pencolor("yellow")
# # fillcolor("red")
# color('red')
# #pen(fillcolor="red",pencolor="yellow")
# #左眼
# pu()
# goto(-45,92)
# pd()
# begin_fill()
# color((0,0,0),(0,0,0.1))
# circle(radius=15)
# #右眼
# pu()
# goto(45,92)
# pd()
# circle(radius=15)
# end_fill()
#  
# #鼻子
# pu()
# goto(20,60)
# color('pink')
# pd()
# begin_fill()
# goto(-20,60)
# goto(0,45)
# goto(20,60)
# end_fill()
#  
# #嘴
# goto(0,45)
# goto(0,40)
# seth(-90)
# circle(10,120)
# pu()
# goto(0,40)
# seth(-90)
# pd()
# circle(-10,120)
#  
#  
# #小兔的耳朵
# #左耳
# pu()
# goto(-60,180)#
# seth(200)
# pd()
# circle(radius=350,extent=90)
# goto(-98,110)
# #右耳
# pu()
# goto(60,180)#
# seth(-20)
# pd()
# circle(radius=-350,extent=90)
# goto(98,110)
#  
# #小兔的身体
# pencolor('orange')
# pu()
# goto(20,3)
# seth(-25)
# pd()
# circle(radius=-250,extent=25)
# circle(radius=-135,extent=260)
# seth(50)
# circle(radius=-250,extent=25)
#  
# ##小兔的胳膊
# #左臂
# pu()
# seth(180)
# goto(-30,-3)
# pd()
# #小短胳膊
# ##circle(radius=270,extent=20)
# ##circle(radius=20,extent=190)
# circle(radius=248,extent=30)
# circle(radius=29,extent=185)
# #右臂
# pu()
# seth(0)
# goto(30,-3)
# pd()
# circle(radius=-248,extent=30)
# circle(radius=-27,extent=184)
#  
# ##小兔的脚
# ##左脚
# pu()
# goto(-162,-260)#
# pd()
# seth(0)
# circle(radius=41)
# #右脚
# pu()
# goto(164,-260)
# pd()
# circle(radius=41)
#  
# done()
# =============================================================================
# =============================================================================
# import turtle as t
# t.pensize(2)
# t.speed(0)
# t.color("pink")
# t.tracer(8,25)
# for x in range(120):
#     for i in range(4):
#         t.fd(100)
#         t.left(90)
#     t.left(3)
# n=pow(2,1.0/2.0)
# t.penup()
# t.goto(0,-100*n)
# t.pendown()
# t.color("purple")
# t.circle(100*n)
# t.penup()
# t.goto(-50,-125*n)
# t.pendown()
# t.color("blue")
# t.write("Figure: Square Spiral", font = ("Arial", 28, ""))
# t.update()
# t.hideturtle()
# t.done
# =============================================================================
