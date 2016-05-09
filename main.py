import pygame
import itertools

class main():
  # Initialize the module  
  pygame.init()
  
  # Sets display caption
  pygame.display.set_caption("Default template")

  # Create the screen
  screen=pygame.display.set_mode((720,540))

  # Defines the background sprite and tiles it
  background=pygame.image.load("grass.png")
  background_width, background_height=background.get_width(), background.get_height()
  for x,y in itertools.product(range(0,720,background_width),range(0,540,background_height)):
    screen.blit(background, (x,y))

  location_x=0
  location_y=0

  # Function for movement inputs on the keyboard
  def movement(self, event, location_x, location_y):
    if event.type==pygame.KEYDOWN:
      if event.key==pygame.K_a:
        location_x-=5
      elif event.key==pygame.K_d:
        location_x+=5
      elif event.key==pygame.K_w:
        location_y+=5
      elif event.key==pygame.K_s:
        location_y-=5

  # Defines the player sprite so it can be drawn to the screen
  def sprite(window,location_x,location_y):
    sprite_image=pygame.image.load("emot-downs.png")
    window.blit(sprite_image, (location_x,location_y))

  # Controls the main loop to keep the window running
  running=True

  # Main loop
  while running:
    # Gets all events from the eventqueue
    for event in pygame.event.get():
      # Only do something when the event involves QUIT
      if event.type==pygame.QUIT:
        # Changes running to False, breaking the loop
        running=False
      # Updates the display
      else:
        movement(sprite(screen,location_x,location_y), event, location_x, location_y)
        print location_x
        print location_y
        pygame.display.flip()

# Runs the main function only if this module is executed as the main script (if this module is imported, nothing is executed)
if __name__=="__main__":
  main()
