import qrcode
import image

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=10,
)

link = 'https://github.com/artemmokinn/qr-code-generator'  # write a link here

qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill="black", back_color="white")
img.save("qr-code.png")
