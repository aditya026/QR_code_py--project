# module qrcode import
import qrcode


img= qrcode.make("hey' there")

img.save("my_qr.png")
