# Don't forget to pip install pyzbar and pip install PILLOW

import from pyzbar.pyzbar import decode
import PIL import Image

# open the QR code image
img = Image.open('QRCode.png')

# decode its data - can also be used for barcodes
decodedData = decode(img)

# Display it
print(decodedData)