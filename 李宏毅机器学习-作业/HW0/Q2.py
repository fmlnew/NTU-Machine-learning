# 20190720
from PIL import Image

# Image 为pyton基本的图像处理模块 类似于matlab

#读取一张图片：
lena = Image.open("lena.png")
# im=Image.open('/home/Picture/test.jpg')
lena_modified = Image.open("lena_modified.png")

#查看图像信息：
# im.format格式如png,jpg, im.size应是像素大小, im.mode似乎是模式，比如灰度模式、多通道模式等【？】
w, h = lena.size

for j in range(h):
    for i in range(w):
    	# 对lena图片中的每一个像素，判断：若lena图片和lena_modified图片点的像素一致，则更改后者像素为白色
    	# im.getpixel((1,2)) 获得该坐标点对应像素的RGB颜色值
    	# im.getpixel((1,2)，255) 指定该坐标点对应像素的RGB颜色值
        if lena.getpixel((i, j)) == lena_modified.getpixel((i, j)):
            lena_modified.putpixel((i, j), 255)
# 显示图片：
lena_modified.show()
# 保存图片
# im.save("save.gif","GIF") #保存图像为gif格式
lena_modified.save("ans_two.png")
