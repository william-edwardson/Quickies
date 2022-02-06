# Be sure to pip install qrcode
# before you import this
import qrcode

# data in the QR code
data = 'Some currently-useless encoded data ~ F.'

# extra image properties
qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr.add_data(data)
qr.make(fit = True)

# make an image with the required foreground and background colours
img = qr.make_image(fill_color = 'green', back_color = 'white')

img.save('QRCode.png')