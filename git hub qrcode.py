import qrcode
link='https://www.youtube.com/watch?v=HhjHYkPQ8F0&list=RDm9ezpAUvMC8&index=2'
qr=qrcode.make(link)
qr.save("qrcode.jpg")
print("QR Code is created")