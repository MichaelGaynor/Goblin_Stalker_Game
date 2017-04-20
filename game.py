# Include pygame which we got from pip
import pygame

# In order to use pygame with have to run the init method
pygame.init()

# Create a screen with a size (this one is a dictionary)
screen = {
  "height": 512,
  "width": 480
}

keys = {
  "right": 275,
  "left": 276,
  "up": 273,
  "down": 274
}

keys_down = {
  "right": False,
  "left": False,
  "up": False,
  "down": False
}

hero = {
  "x": 100,
  "y": 100,
  "speed": 20
}

# screen_size is a tuple here so it won't ever be changed
screen_size = (screen["height"], screen["width"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Stalker")
background_image = pygame.image.load("images/background.png")
hero_image = pygame.image.load("images/hero.png")

# /////////////////////////////////////////////////////////////
# ////////////////////////MAIN GAME LOOP///////////////////////
# ////////////////////////MAIN GAME LOOP///////////////////////
# /////////////////////////////////////////////////////////////
game_on = True
# Create the game loop (while 1)

while game_on:
  # we are inside the main game loo. It will run as long as game_on is True

  # ------EVENT!------
  for event in pygame.event.get():
    # Looping through all events that happened this game loop cycle

    if event.type == pygame.QUIT:
      # The user clicked on the red X to quit the game

      game_on = False
      # Update our boolean so pygame can escape the loop

    elif event.type == pygame.KEYDOWN:
      if event.key == keys["up"]:
        keys_down["up"] = True
      elif event.key == keys["down"]: 
        keys_down["down"] = True
      if event.key == keys["right"]:
        keys_down["right"] = True
      elif event.key == keys["left"]:
        keys_down["left"] = True

    elif event.type == pygame.KEYUP:
      if event.key == keys["up"]:
        keys_down["up"] = False
      elif event.key == keys["down"]:
        keys_down["down"] = False
      if event.key == keys["right"]:
        keys_down["right"] = False
      elif event.key == keys["left"]:
        keys_down["left"] = False


  # -----Update Hero Position------
  if keys_down["up"]:
    hero["y"] -= hero["speed"]
  elif keys_down["down"]:
    hero["y"] += hero["speed"]
  if keys_down["right"]:
    hero["x"] += hero["speed"]
  elif keys_down["left"]:
    hero["x"] -= hero["speed"]



  # -----RENDER!------
  # blit takes two arguments
  # 1. What
  # 2. Where
  pygame_screen.blit(background_image, [0,0])

  # draw the hero
  pygame_screen.blit(hero_image, [hero["x"],hero["y"]])

  # Clear the screen for next time
  pygame.display.flip()







