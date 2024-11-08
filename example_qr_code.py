import qrcode


# img = qrcode.make('Some data here')
# print(type(img))
# img.save("some_file.png")


qr = qrcode.QRCode(
    version=2,
    box_size=20,
    border=2,
)

qr.add_data("https://github.com/SakshamChauhan7")

img = qr.make_image(fill_color = "green", back_color = "black")

img.save("gitProfile.png")