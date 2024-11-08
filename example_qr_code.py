import qrcode


# img = qrcode.make('Some data here')
# print(type(img))
# img.save("some_file.png")


qr = qrcode.QRCode(
    version=2,
    box_size=20,
    border=2,
)
link = "https://sakshamchauhan7.github.io/"
name = "oldResumeWeb.png"
qr.add_data(link)

img = qr.make_image(fill_color = "green", back_color = "black")

img.save(name)