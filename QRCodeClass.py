"""
@Goal    :    To generate QR code of the given input string

@Author  :    Sushilkumar Lokhande

@Date    :    Friday, July 9, 2021

"""

import sys
import qrcode
import datetime

class GenerateQRCode():
    #constructor
    def __init__(self, inputString):
        self.inputString = inputString

    def ConvertStringToQRCode(self):
        
        print("Input string to convert to QR code is: " + self.inputString)
        fileExtension = '.png'

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        
        qr.add_data(self.inputString)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        #Get image name as per current date time
        imageName = str(datetime.datetime.now())
        
        imageName = imageName.replace(":", "_").replace(".", "_").replace("-", "_").replace(" ", "_")
        imageName = self.inputString.replace("https://", "").replace(".", "_").replace(".", "_").replace("/", "_")

        # save image
        img.save(imageName + fileExtension)

def main():
    inputString = input("Enter string to generate QR code: ")
    objGenerateQRCode = GenerateQRCode(inputString)
    objGenerateQRCode.ConvertStringToQRCode()

main()
