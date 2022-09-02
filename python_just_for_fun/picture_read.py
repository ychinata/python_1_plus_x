from PIL import Image    # Pillow                    9.0.0
import pillow_avif       # pillow-avif-plugin        1.2.2
# 以上只是其中一个可用版本，并非必须
# 必须先安装pip install pillow-avif-plugin才能使用
# reviewed: hx
# date: 2022.8.26
# 版权声明：本文为CSDN博主「KonohaYuminaga」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/Vioshine/article/details/125949655

AVIFfilename = 'test.avif'
AVIFimg = Image.open(AVIFfilename)
AVIFimg.save(AVIFfilename.replace("avif",'jpg'),'JPEG')
# 也可以是png等任意格式，但是转换的png有点大

# 反向
# JPGfilename = 'test.jpg'
# JPGimg = Image.open(JPGfilename)
# JPGimg.save(JPGfilename.replace("jpg",'avif'),'AVIF')


