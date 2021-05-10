from tkinter import *
from tkinter import colorchooser
from PIL import Image

x, y = 0, 0  # coordinates
color = 'black'
bgColor = 'white'


def createCanvas():
  # TODO: fix background color for new canvas
  canvas.delete('all')
  showPalette()


def deleteCanvas(event):
  canvas.delete('all')
  showPalette()


def draw(event):
  x, y = event.x, event.y
  x1, y1 = (x - 1), (y - 1)
  x2, y2 = (x + 1), (y + 1)
  canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color,
                          width=getScaleValue())


def eraseLine():
  global color
  color = "white"


def getColor():
  global color
  hex = colorchooser.askcolor(title="Edit colors")
  color = hex[1]
  return color


def getScaleValue():
  brushSize = str(var.get())
  return brushSize


def hidePalette():
  global canvas, blackRectangle, grayRectangle, brownRectangle, redRectangle, orangeRectangle, yellowRectangle, greenRectangle, blueRectangle, purpleRectangle, whiteRectangle
  canvas.itemconfig(blackRectangle, state=HIDDEN)
  canvas.itemconfig(grayRectangle, state=HIDDEN)
  canvas.itemconfig(brownRectangle, state=HIDDEN)
  canvas.itemconfig(redRectangle, state=HIDDEN)
  canvas.itemconfig(orangeRectangle, state=HIDDEN)
  canvas.itemconfig(yellowRectangle, state=HIDDEN)
  canvas.itemconfig(greenRectangle, state=HIDDEN)
  canvas.itemconfig(blueRectangle, state=HIDDEN)
  canvas.itemconfig(purpleRectangle, state=HIDDEN)
  canvas.itemconfig(whiteRectangle, state=HIDDEN)


def saveImage():
  hidePalette()
  canvas.postscript(colormode='color', file="sketch.eps")
  image = Image.open("sketch.eps")
  image.save("sketch.png")
  showPalette()


# def sendImage():
#   # TODO: implement method
#   Chat.text_field.insert(0, "img: C:/Users/Li Ting Luong/BACnet/21-fs-ias-lec/groups/02-ChatApplikationSketch/sketch.png")
#   Chat.send_button.invoke()


def showColor(newColor):
  global color
  color = newColor


def showPalette():
  global blackRectangle, grayRectangle, brownRectangle, redRectangle, orangeRectangle, yellowRectangle, greenRectangle, blueRectangle, purpleRectangle, whiteRectangle
  blackRectangle = canvas.create_rectangle((10, 10, 30, 30), fill='black')
  canvas.tag_bind(blackRectangle, '<Button-1>', lambda x: showColor('black'))

  grayRectangle = canvas.create_rectangle((10, 40, 30, 60), fill='gray')
  canvas.tag_bind(grayRectangle, '<Button-1>', lambda x: showColor('gray'))

  brownRectangle = canvas.create_rectangle((10, 70, 30, 90), fill='brown4')
  canvas.tag_bind(brownRectangle, '<Button-1>', lambda x: showColor('brown4'))

  redRectangle = canvas.create_rectangle((10, 100, 30, 120), fill='red')
  canvas.tag_bind(redRectangle, '<Button-1>', lambda x: showColor('red'))

  orangeRectangle = canvas.create_rectangle((10, 130, 30, 150), fill='orange')
  canvas.tag_bind(orangeRectangle, '<Button-1>', lambda x: showColor('orange'))

  yellowRectangle = canvas.create_rectangle((10, 160, 30, 180), fill='yellow')
  canvas.tag_bind(yellowRectangle, '<Button-1>', lambda x: showColor('yellow'))

  greenRectangle = canvas.create_rectangle((10, 190, 30, 210), fill='green')
  canvas.tag_bind(greenRectangle, '<Button-1>', lambda x: showColor('green'))

  blueRectangle = canvas.create_rectangle((10, 220, 30, 240), fill='blue')
  canvas.tag_bind(blueRectangle, '<Button-1>', lambda x: showColor('blue'))

  purpleRectangle = canvas.create_rectangle((10, 250, 30, 270), fill='purple')
  canvas.tag_bind(purpleRectangle, '<Button-1>', lambda x: showColor('purple'))

  whiteRectangle = canvas.create_rectangle((10, 280, 30, 300), fill='white')
  canvas.tag_bind(whiteRectangle, '<Button-1>', lambda x: showColor('white'))


def sketchWindow():
  global canvas, var, eraserImage, bucketImage
  window = Toplevel()

  window.title('Sketch')

  window.rowconfigure(0, weight=1)
  window.columnconfigure(0, weight=1)

  menubar = Menu(window)
  window.config(menu=menubar)
  submenu = Menu(menubar, tearoff=0)

  menubar.add_cascade(label='New Canvas', command=createCanvas)
  menubar.add_cascade(label='Save Image', command=saveImage)
  # menubar.add_cascade(label='Send Image', command=sendImage)

  canvas = Canvas(window, background=bgColor, width=700, height=600)
  canvas.grid(row=0, column=0, sticky='nsew')

  var = IntVar()
  scale = Scale(window, from_=0, to=50, orient=HORIZONTAL, variable=var)
  scale.place(x=10, y=320)
  scale.set(10)

  paletteButton = Button(window, text="Edit colors", command=getColor)
  paletteButton.place(x=10, y=380)

  canvas.bind('<B1-Motion>', draw)
  canvas.bind('<B3-Motion>', deleteCanvas)

  photoEraser = PhotoImage(file=r"eraser.png")
  eraserImage = photoEraser.subsample(7, 7)
  eraser = Button(window, image=eraserImage, command=eraseLine)
  eraser.place(x=10, y=420)

  photoBucket = PhotoImage(file=r"colorBucket.png")
  bucketImage = photoBucket.subsample(7, 7)
  fill = Button(window, image=bucketImage,
                command=lambda: canvas.configure(bg=color))
  fill.place(x=10, y=470)

  showPalette()
