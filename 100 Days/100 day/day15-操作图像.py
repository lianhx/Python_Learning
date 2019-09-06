from PIL import Image, ImageFilter

image = Image.open('./res/guido.jpg')
print(image.format, image.size, image.mode)
# image.show()  # 打开图像
rect = 80, 20, 310, 360  # 裁剪图像
# image.crop(rect).show()
image.filter(ImageFilter.CONTOUR).show()
