import qrcode


# img = qrcode.make('Some data here')
# print(type(img))
# img.save("some_file.png")


qr = qrcode.QRCode(
    version=2,
    box_size=20,
    border=2,
)
print("Enter the the origin/link for Qr code generator: ")
data= input()
qr.add_data(data)

print("Whats the file name you want to save: ")
name = input()
fileName = name + ".png"
img = qr.make_image(fill_color = "green", back_color = "black")

img.save(fileName)