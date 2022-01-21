import pyqrcode

code = pyqrcode.create('LINK DE REFERENCIA')  # você pode colocar qualquer link dentro das aspas para gerar seu QR Code
code.png('QRcode.png', scale=6)  # você pode colocar qualquer nome para seu arquivo, desde que termine com ".png"

if code != 0:
    print("QR Code gerado!")
