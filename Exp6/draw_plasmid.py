#Author：Alex.Zhang
from PIL import Image, ImageDraw,ImageFont
import math
#创建一个图像
PLASMID_LENGTH = 4471
SIZE = (500, 500)
CENTER = (250, 250)
#‘RGB’表示该图像采用红绿蓝配色方案，元组size取值(500, 500)
# 在RGB中，红色（255,0，0），绿色（0,255,0），蓝色（0,0,255）
# white可以为（255,255,255）或者‘#ffffff’，黑色（0,0,0）或‘#000000’
#表示图像的x和y的尺寸为多少像素，‘white’设置背景色为白色
pTRXFUS = Image.new('RGB', SIZE, 'white')
#激活绘图工具
DRAW = ImageDraw.Draw(pTRXFUS)
#定义三个函数
def get_angle(bp, length=PLASMID_LENGTH):
    """质粒碱基的位置转换为角度"""
    return bp * 360 / length

def coord(angle, center, radius):
    """ 返回圆上点坐标 (x,y) 坐标说明： 例如point(100,100)，是距左边框100像素，距顶部100像素的一个点 box(100,100,150,150),距顶部和左侧边框各100像素的50像素宽的一个方形框 """
    #角度转弧度
    rad = math.radians(angle)
    x = int(center[0] + math.cos(rad) * radius)
    y = int(center[1] + math.sin(rad) * radius)
    return x, y

def draw_arrow_tip(start, direction, color):
    """根据起始的角度位置画一个三角形"""
    p1 = coord(start + direction, CENTER, 185)
    p2 = coord(start, CENTER, 160)
    p3 = coord(start, CENTER, 210)
    DRAW.polygon((p1, p2, p3), fill=color)
#绘制质粒
TET_START, TET_END = get_angle(101), get_angle(1161)
AMP_START, AMP_END = get_angle(3161), get_angle(4112)
ORI_START, ORI_END = get_angle(2459), get_angle(3087)


BOX = (50, 50, 450, 450)
#画一个灰色的圆
DRAW.pieslice(BOX, 0, 360, fill='gray')
#填充一个扇形，TET_START为起始角度， TET_END终止角度，0度角在时钟的3:00位置
DRAW.pieslice(BOX, TET_START, TET_END, fill='pink')
#绘制一个白色圆
DRAW.pieslice((80, 80, 420, 420), 0, 360, fill='white')
#添加箭头
draw_arrow_tip(TET_END, 10, 'pink')
draw_arrow_tip(AMP_START, 10, 'yellow')
draw_arrow_tip(ORI_START, -10, 'darkmagenta')
#添加文本
arial16 = ImageFont.truetype('D:\\Remain\\7.python及其生物信息学应用\\实践\\实践6\\Arial.ttf',16)
DRAW.text((150, 130), "ori", fill=(0, 0, 0),font=arial16)
DRAW.text((340, 130), "amp", fill=(0, 0, 0),font=arial16)
DRAW.text((300, 380), "tet", fill=(0, 0, 0),font=arial16)
#pTRXFUS.save('plasmid_pTRXFUS.png')
pTRXFUS.save('plasmid_pTRXFUS.jpg')
#pTRXFUS.save('plasmid_pTRXFUS.tif')