from PIL import Image, ImageFilter, ImageEnhance
img = Image.open('opencv_frame_0.jpg')
enc_img = img.filter(ImageFilter.DETAIL)
img_con = ImageEnhance.Contrast(img)

img_con.enhance(1.3).show("30% more contrast ")
#img.show()
#enc_img.show()