from pyzbar.pyzbar import decode
from PIL import Image

print("Welcame QR Code Scanner\n")
di = input("Enter the Path of Files.")
Img = input("Enter the Image Name.")

dec = decode(Image.open(di+"/"+Img))
print(dec[0].data.decode())