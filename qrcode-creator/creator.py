import qrcode
img = qrcode.make('https://github.com/Dants0')
type(img)
img.save("some_file.png")