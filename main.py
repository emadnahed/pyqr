import pyqrcode 
from pyqrcode import QRCode 
  
# Taking user input
Contact = input("Enter your Phone number:")
  
# Generate QR code
qr = pyqrcode.create(int(Contact)) 
  
# Create and save the png file naming "myqr.png" 
qr.svg("myContactQR.svg", scale = 8)