#Makes a canvas to draw the picture to
def setup():
  size(1980,1080)

  noLoop()

#Loads source image and then repaints with the words
def draw():
    #source.jpg is the image that is used for the draw porcess
  image(loadImage("source.jpg"),0,0)
  #This makes the picture black and white to make life easier
  filter(THRESHOLD,.8)
  loadPixels()
   
  #Insert the text you want in the picture here 
  words =  "INSERT WORDS HERE"
  font_size = 3
  myFont = createFont("Georgia", font_size)
  textFont(myFont)
    
  x = 0
  y = 0
    
  boxes = []
  cords = []
  #Seperates the picture in to boxes the same size as a character in the font
  for i in range(1080/font_size):
      
      for q in range(1980/font_size):
          boxes.append(get(x,y,font_size,font_size))
          cords.append([x,y])
          x += font_size
      y += font_size
      x = 0
  my_boxes = []
  place = 0
  #If the box is more than a given percent black it replaces that section of the picture with a character
  #If it is less than the given percent black it leaves it white
  for rec in boxes:
      colored = 0
      for pixel in rec.pixels:
          if pixel == color(255,255,255):
                           colored += 1
      if colored > (font_size * font_size)/2:
          my_boxes.append(cords[place])
      place += 1

    
  letter = 0
  clear()   
  for rec in my_boxes:
      text(words[letter],rec[0],rec[1])
      letter += 1
  #filter(INVERT)
  #Saves the picture to destination.png
  saveFrame("destination.png")
      
          

