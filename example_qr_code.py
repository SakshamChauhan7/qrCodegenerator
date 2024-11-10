import qrcode


# img = qrcode.make('Some data here')
# print(type(img))
# img.save("some_file.png")


qr = qrcode.QRCode(
    version=2,
    box_size=20,
    border=2,
)
<<<<<<< HEAD
print("Enter the the origin/link for Qr code generator: ")
data= input()
qr.add_data(data)

print("Whats the file name you want to save: ")
name = input()
fileName = name + ".png"
img = qr.make_image(fill_color = "green", back_color = "black")

img.save(fileName)
=======
link = "https://sakshamchauhan7.github.io/"
name = "oldResumeWeb.png"
qr.add_data(link)

img = qr.make_image(fill_color = "green", back_color = "black")

img.save(name)
>>>>>>> 0fbe62feeb4e8cf3937ee08e62cb00576be134ce
