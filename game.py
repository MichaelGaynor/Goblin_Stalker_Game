# Include pygame which we got from pip
import pygame


# bring in the math module so we can use absolute value
from math import fabs

# get the random module
from random import randint

# In order to use pygame with have to run the init method
pygame.init()

# Create a screen with a size (this one is a dictionary)
screen = {
  "width": 685,
  "height": 420
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
  "speed": 5,
  "wins": 0,
  "losses": 0
}

king_ghidorah = {
  "x": 300,
  "y": 100,
  "speed": 3
}

anguirus = {
  "x": 100,
  "y": 300,
  "speed": 2
}

edible_man = {
  "x": 2,
  "y": screen["height"]-100
}

# screen_size is a tuple here so it won't ever be changed
screen_size = (screen["width"], screen["height"])
pygame_screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Goblin Stalker")
background_image = pygame.image.load("images/background2.png")
hero_image = pygame.image.load("images/godzilla_WHAT.png")
king_ghidorah_image = pygame.image.load("images/king_ghidorah.png")
anguirus_image = pygame.image.load("images/anguirus.png")
edible_man_image = pygame.image.load("images/edible_man.gif")
edible_man_image_scale = pygame.transform.scale(edible_man_image, (100,100))
hero_image_scale = pygame.transform.scale(hero_image, (100,100))
king_ghidorah_image_scale = pygame.transform.scale(king_ghidorah_image, (100,80))
anguirus_image_scale = pygame.transform.scale(anguirus_image, (75,60))


# -----Adding Sound-----
pygame.mixer.music.load("sounds/island_music_x.wav")
pygame.mixer.music.play(-1)
win_sound = pygame.mixer.Sound("sounds/zilla3.wav")
lose_sound = pygame.mixer.Sound("sounds/lose.wav")
speed_boost_sound = pygame.mixer.Sound("sounds/win.wav")

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
  if (hero["x"] > screen["width"]-100):
    hero["x"] = 0
  elif (hero["x"] < 0):
    hero["x"] = screen["width"]-100
  if (hero["y"] > screen["height"]-100):
    hero["y"] = 0
  elif (hero["y"] < 0):
    hero["y"] = screen["height"]-100

  # ------Inventing Time
  # max_time = 3
  # start_time = time.time()  # remember when we started
  

  # COLLISION DETECTION!!!
# king_ghidorah and hero collisions-------
  distance_between = fabs(hero["x"] - king_ghidorah["x"]) + fabs(hero["y"] - king_ghidorah["y"])
  if (distance_between < 100):
    # Generate a random X > 0, X < screen["width"]
    # Generate a random Y > 0, Y < screen["height"]
    rand_x = randint(0, screen["width"]-100)
    rand_y = randint(0, screen["height"]-100)
    king_ghidorah["x"] = rand_x
    king_ghidorah["y"] = rand_y
    hero["wins"] += 1
    win_sound.play()


# -------King Ghidorah Motion

  elif (distance_between >=100):
    current_location = [king_ghidorah["x"],king_ghidorah["y"]]
    rand_co_x = randint(0, screen["width"]-100)
    rand_co_y = randint(0, screen["height"]-100)
    # rand_co_x = 0
    # rand_co_y = randint(100, screen["width"]-100)
    rand_location = [rand_co_x,rand_co_y]
    distance_between_co = fabs(rand_co_x - king_ghidorah["x"]) + fabs(rand_co_y - king_ghidorah["y"])
    if (distance_between_co > 20):
      # king_ghidorah["x"] = rand_co_x
      if (king_ghidorah["x"] < rand_co_x):
        king_ghidorah["x"] += king_ghidorah["speed"]
      if (king_ghidorah["x"] > rand_co_x):
        king_ghidorah["x"] -= king_ghidorah["speed"]
      if (king_ghidorah["y"] < rand_co_y):
        king_ghidorah["y"] += king_ghidorah["speed"]
      if (king_ghidorah["y"] > rand_co_y):
        king_ghidorah["y"] -= king_ghidorah["speed"]
    else:
      rand_co_x = randint(0, screen["width"]-100)
      rand_co_y = randint(0, screen["height"]-100)

    # rand_dist_x = randint(1,200)
    # rand_dist_y = randint(1,200)
    # if (rand_dist_x < 50):
    #   king_ghidorah["x"] -= king_ghidorah["speed"]
    # elif (rand_dist_x > 50):
    #   king_ghidorah["x"] += king_ghidorah["speed"]
    # if (rand_dist_y < 50):
    #   king_ghidorah["y"] -= king_ghidorah["speed"]
    # elif (rand_dist_y > 50):
    #   king_ghidorah["y"] += king_ghidorah["speed"]


  if (king_ghidorah["x"] > screen["width"]-100):
    king_ghidorah["x"] = 0
  elif (king_ghidorah["x"] < 0):
    king_ghidorah["x"] = screen["width"]-100
  if (king_ghidorah["y"] > screen["height"]-100):
    king_ghidorah["y"] = 0
  elif (king_ghidorah["y"] < 0):
    king_ghidorah["y"] = screen["height"]-100

# anguirus and hero collisions-------
  distance_between = fabs(hero["x"] - anguirus["x"]) + fabs(hero["y"] - anguirus["y"])
  if (distance_between < 100):
    # Generate a random X > 0, X < screen["width"]
    # Generate a random Y > 0, Y < screen["height"]
    rand_x = randint(0, screen["width"]-100)
    rand_y = randint(0, screen["height"]-100)
    hero["x"] = rand_x
    hero["y"] = rand_y
    hero["losses"] += 1
    hero["speed"] = 10
    lose_sound.play()
  # elif (distance_between >=100):
    # max_time = 1
    # start_time = time.time()

# ----------Anguirus Motion

  elif (distance_between >=100):
    current_location2 = [anguirus["x"],anguirus["y"]]
    rand_co_x2 = hero["x"]
    rand_co_y2 = hero["y"]
    rand_location2 = [rand_co_x2,rand_co_y2]
    distance_between_co2 = fabs(rand_co_x2 - anguirus["x"]) + fabs(rand_co_y2 - anguirus["y"])
    if (distance_between_co2 > 20):
      if (anguirus["x"] < rand_co_x2):
        anguirus["x"] += anguirus["speed"]
      if (anguirus["x"] > rand_co_x2):
        anguirus["x"] -= anguirus["speed"]
      if (anguirus["y"] < rand_co_y2):
        anguirus["y"] += anguirus["speed"]
      if (anguirus["y"] > rand_co_y2):
        anguirus["y"] -= anguirus["speed"]
    else:
      rand_location2 = [randint(0, screen["width"]-100),randint(0, screen["height"]-100)]

    # rand_dist_x = randint(1,2)
    # rand_dist_y = randint(1,2)
    # if (rand_dist_x < 2):
    #   anguirus["x"] -= anguirus["speed"]
    # elif (rand_dist_x > 1):
    #   anguirus["x"] += anguirus["speed"]
    # if (rand_dist_y < 2):
    #   anguirus["y"] -= anguirus["speed"]
    # elif (rand_dist_y > 1):
    #   anguirus["y"] += anguirus["speed"]

  if (anguirus["x"] > screen["width"]-100):
    anguirus["x"] = 0
  elif (anguirus["x"] < 0):
    anguirus["x"] = screen["width"]-100
  if (anguirus["y"] > screen["height"]-100):
    anguirus["y"] = 0
  elif (anguirus["y"] < 0):
    anguirus["y"] = screen["height"]-100

# edible_man and hero collisions-------
  distance_between = fabs(hero["x"] - edible_man["x"]) + fabs(hero["y"] - edible_man["y"])
  if (distance_between < 100):
    # Generate a random X > 0, X < screen["width"]
    # Generate a random Y > 0, Y < screen["height"]
    rand_x = randint(0, screen["width"]-100)
    rand_y = screen["height"]-100
    edible_man["x"] = rand_x
    edible_man["y"] = rand_y
    hero["speed"] += 1
    speed_boost_sound.play()


  # -----RENDER!------
  # blit takes two arguments
  # 1. What
  # 2. Where
  # pygame_screen.blit(None, [0,0])
  pygame_screen.blit(background_image, [0,0])

  # Draw the hero wins on the screen
  font = pygame.font.Font(None, 50)
  wins_text = font.render("wins %d" % (hero["wins"]), True, (255,155,100))
  loss_text = font.render("losses %d" % (hero["losses"]), True, (255,155,100))
  pygame_screen.blit(wins_text, [40,40])
  pygame_screen.blit(loss_text, [300,40])

  # draw the hero
  pygame_screen.blit(hero_image_scale, [hero["x"],hero["y"]])
  pygame_screen.blit(king_ghidorah_image_scale, [king_ghidorah["x"],king_ghidorah["y"]])
  pygame_screen.blit(anguirus_image_scale, [anguirus["x"],anguirus["y"]])
  pygame_screen.blit(edible_man_image_scale, [edible_man["x"],edible_man["y"]])

  # Clear the screen for next time
  pygame.display.flip()







