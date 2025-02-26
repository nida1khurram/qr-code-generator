# pip install qrcode

import qrcode
data = 'Qr code generator'
img = qrcode.make(data)
with open('D:\learning\q3\qr-code-generator/abc.png', 'wb') as f:
    img.save(f)






# if need
    # pip install qrcode[pil]