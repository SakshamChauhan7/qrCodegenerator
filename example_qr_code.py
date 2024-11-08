import qrcode
img = qrcode.make('Some data here')
type(img)
img.save("some_file.png")