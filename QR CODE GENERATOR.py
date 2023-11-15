'''   by imporing module specificly for QR CODE generation 
https://pypi.org/project/qrcode/


functions from qrcode module 

1. make -- for making qr code
2. save  -- for saving qr code in png

* for creating simple qr code we can use make and save functions but for creating
        qr code with additional features like with colors and borders etcs then we need to 
        import PIL.Image module and using functions from Image class QRCode to change
        border of qr code and fixing errors 

'''

import qrcode # module for generating qr code
from PIL import Image

print("************      QR CODE GENERATOR       **************",end="\n\n\n")
URL=input("Please Enter the URL for creating its QR code : ")
print("\n")
QR_Code_Name=input("Please Enter the file name for QR code : ")
QR_Code_Name=QR_Code_Name+".png"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=5,
    border=4,
)

qr.add_data(URL)
qr.make(fit=True)
img= qr.make_image(fill_color="red",back_color="blue")
img.save(QR_Code_Name)

image_path=f"{QR_Code_Name}"
Image.open(image_path).show()